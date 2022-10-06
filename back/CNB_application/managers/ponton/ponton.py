from peewee import DoesNotExist
from datetime import datetime
from typing import Optional

from CNB_application.exceptions import *
from CNB_application.models.ponton.ponton import Ponton
from CNB_application.models.membership import Family


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
        pontons.append(
            {
                "family": family,
                "date_start": date_start,
                "date_end": date_end,
                "boat_size": boat_size,
            }
        )
    logger.debug(
        "Get all ponton objects from db. Number of ponton objects : {}".format(
            len(pontons)
        )
    )

    return pontons


def get_pontons_by_family(family_id: str) -> list[Ponton]:
    pontons = []
    query = Ponton.select().where((Ponton.family.id == family_id))

    if len(query == 0):
        raise UserNotFound
    for ponton in query:
        family, date_start, date_end, boat_size = ponton.get_data()
        pontons.append(
            {
                "family": family,
                "date_start": date_start,
                "date_end": date_end,
                "boat_size": boat_size,
            }
        )
    logger.debug(
        "Get all pontons for family {}. Number of pontons : {}".format(
            family.last_name, len(pontons)
        )
    )
    return pontons


def create_ponton(
    family: Family, boat_size: int, date_start: str, date_end: str
) -> Ponton:
    try:
        date_start = datetime.strptime(date_start, "%Y-%m-%d")
        date_end = datetime.strptime(date_end, "%Y-%m-%d")
    except (ValueError, TypeError):
        raise InvalidDateFormat
    ponton_object = Ponton.create(
        family=family, boat_size=boat_size, date_start=date_start, date_end=date_end
    )
    ponton_object.save()
    return ponton_object


def update_ponton(
    ponton_id: str,
    boat_size: Optional[int],
    date_start: Optional[str],
    date_end: Optional[str],
) -> Ponton:
    ponton = get_ponton(ponton_id)
    ponton.update_ponton(boat_size=boat_size, date_start=date_start, date_end=date_end)
    return ponton


def delete_ponton(ponton_id: str) -> bool:
    try:
        ponton = Ponton.get(Ponton.id == ponton_id)
        ponton.delete_instance(recursive=True)
        return True
    except DoesNotExist:
        raise PontonNotFound
