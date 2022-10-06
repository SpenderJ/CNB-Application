from peewee import DoesNotExist
from typing import Optional
from datetime import datetime

from CNB_application.exceptions import *
from CNB_application.models.rent.program import SailingProgram
from CNB_application.models.rent.program import SailingProgramType
from CNB_application.models.membership import Membership
from CNB_application.models.membership import Family


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
        programs.append(
            {
                "family": family,
                "sailing_program": sailing_program,
                "date_start": date_start,
            }
        )
    logger.debug(
        "Get all programs from db. Number of programs : {}".format(len(programs))
    )

    return programs


def get_programs_by_family(family_id: str) -> list[SailingProgram]:
    programs = []
    query = SailingProgram.select().where(SailingProgram.family.id == family_id)

    if len(query == 0):
        raise UserNotFound
    for program in query:
        family, sailing_program, date_start = program.get_data()
        programs.append(
            {"family": family, "renting_type": sailing_program, "date": date_start}
        )
    logger.debug(
        "Get all programs for family {}. Number of programs : {}".format(
            family.last_name, len(programs)
        )
    )
    return programs


def create_program(
    family: Family, sailing_program: str, date_start: str
) -> SailingProgram:
    try:
        date_start = datetime.strptime(date_start, "%Y-%m-%d")
    except (ValueError, TypeError):
        raise InvalidDateFormat
    if sailing_program and sailing_program not in SailingProgramType:
        raise RentingTypeNotFound
    program_object = SailingProgram.create(
        family=family,
        sailing_program=sailing_program,
        date_start=date_start,
    )
    program_object.save()
    return program_object


def update_program(
    program_id: str, sailing_program: Optional[str], date_start: Optional[str]
) -> SailingProgram:
    program = get_program(program_id)
    if sailing_program:
        program.update_sailing_program(sailing_program)
    if date_start:
        query = Membership.select().where((Membership.family.id == program.family.id))
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
