from peewee import DoesNotExist

from CNB_application.exceptions import *
from CNB_application.models.ponton.ponton import Ponton
from CNB_application.models.membership.membership import Membership


def get_ponton(ponton_id: str) -> Ponton:
    try:
        ponton = Ponton.get(Ponton.id == ponton_id)
        return ponton
    except DoesNotExist:
        raise PontonNotFound


def get_all_pontons() -> list[Ponton]:
    pontons = []
    query = Ponton.select()

    for ponton in query:
        family, date_start, date_end, boat_size = ponton.get_data()
        pontons.append({'family': family, 'date_start': date_start, 'date_end': date_end, 'boat_size': boat_size})
    logger.debug('Get all ponton objects from db. Number of ponton objects : {}'.format(len(pontons)))

    return pontons


def get_pontons_by_family(family_id: str) -> list[Ponton]:
    pontons = []
    query = Ponton.select().where(
        (Ponton.family.id == family_id))

    if len(query == 0):
        raise UserNotFound
    for ponton in query:
        family, date_start, date_end, boat_size = ponton.get_data()
        pontons.append({'family': family, 'date_start': date_start, 'date_end': date_end, 'boat_size': boat_size})
    logger.debug('Get all pontons for family {}. Number of pontons : {}'.format(family.last_name, len(pontons)))
    return pontons


def update_boat_size(ponton_id: str, boat_size: int) -> Ponton:
    ponton = get_ponton(ponton_id)
    ponton.boat_size = boat_size
    ponton.save()
    return ponton


def update_ponton_date(ponton_id: str, date_start: str, date_end: str, family_id: str) -> Ponton:
    ponton = get_ponton(ponton_id)
    query = Membership.select().where(
        (Membership.family.id == family_id))
    for membership in query:
        if membership.verify_membership_status(date_start) and membership.verify_membership_status(date_end):
            ponton.update_ponton_date(date_start, date_end)
            return ponton
    raise NoMembershipForSelectedDate


def delete_ponton(ponton_id: str) -> bool:
    try:
        ponton = Ponton.get(Ponton.id == ponton_id)
        ponton.delete_instance(recursive=True)
        return True
    except DoesNotExist:
        raise PontonNotFound
