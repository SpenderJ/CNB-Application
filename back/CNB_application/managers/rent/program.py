from peewee import DoesNotExist
from typing import Optional

from CNB_application.exceptions import *
from CNB_application.models.rent.program import SailingProgram
from CNB_application.models.membership.membership import Membership


def get_program(program_id: str) -> SailingProgram:
    try:
        program = SailingProgram.get(SailingProgram.id == program_id)
        return program
    except DoesNotExist:
        raise ProgramNotFound


def get_all_programs() -> list[SailingProgram]:
    programs = []
    query = SailingProgram.select()

    for program in query:
        family, sailing_program, date_start = program.get_data()
        programs.append({'family': family, 'sailing_program': sailing_program, 'date_start': date_start})
    logger.debug('Get all programs from db. Number of programs : {}'.format(len(programs)))

    return programs


def get_programs_by_family(first_name: str, last_name: str) -> list[SailingProgram]:
    programs = []
    query = SailingProgram.select().where(
        (SailingProgram.family.first_name == first_name) &
        (SailingProgram.family.last_name == last_name))

    if len(query == 0):
        raise UserNotFound
    for program in query:
        family, sailing_program, date_start = program.get_data()
        programs.append({'family': family, 'renting_type': sailing_program, 'date': date_start})
    logger.debug('Get all programs for family {}. Number of programs : {}'.format(last_name, len(programs)))
    return programs


def update_program_type(program_id: str, sailing_program: Optional[str], date_start: Optional[str]) -> SailingProgram:
    program = get_program(program_id)
    if sailing_program:
        program.update_sailing_program(sailing_program)
    if date_start:
        query = Membership.select().where(
            (Membership.family.id == program.family.id))
        for membership in query:
            if membership.verify_membership_status(date_start):
                program.update_program_date(date_start)
                return program
        raise NoMembershipForSelectedDate
    return program


def delete_program(program_id) -> bool:
    try:
        program = SailingProgram.get(SailingProgram.id == program_id)
        program.delete_instance(recursive=True)
        return True
    except DoesNotExist:
        raise ProgramNotFound
