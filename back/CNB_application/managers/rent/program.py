from __future__ import annotations

from datetime import datetime

from CNB_application.exceptions import ProgramNotFound
from CNB_application.exceptions import UserNotFound
from CNB_application.exceptions import InvalidDateFormat
from CNB_application.exceptions import RentingTypeNotFound
from CNB_application.exceptions import NoMembershipForSelectedDate
from CNB_application.models.membership import Family
from CNB_application.models.membership import Membership
from CNB_application.models.rent.program import SailingProgram
from CNB_application.models.rent.program import SailingProgramType
from peewee import DoesNotExist


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
                'family': family,
                'sailing_program': sailing_program,
                'date_start': date_start,
            },
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
            {'family': family, 'renting_type': sailing_program, 'date': date_start},
        )
    return programs


def create_program(
    family: Family,
    sailing_program: str,
    date_start: str,
) -> SailingProgram:
    try:
        date_start = datetime.strptime(date_start, '%Y-%m-%d')  # type: ignore
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
    program_id: str,
    sailing_program: str | None,
    date_start: str | None,
) -> SailingProgram:
    program = get_program(program_id)
    if sailing_program:
        program.update_sailing_program(sailing_program)
    if date_start:
        query = Membership.select().where(Membership.family.id == program.family.id)
        for membership in query:
            if membership.verify_membership_status(date_start):
                program.update_program_date(date_start)
                return program
        raise NoMembershipForSelectedDate
    return program


def delete_program(program_id: str) -> bool:
    try:
        program = SailingProgram.get(SailingProgram.id == program_id)
        program.delete_instance(recursive=True)
        return True
    except DoesNotExist:
        raise ProgramNotFound
