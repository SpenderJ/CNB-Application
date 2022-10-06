from peewee import DoesNotExist
from typing import Optional
from datetime import datetime

from CNB_application.exceptions import *
from CNB_application.models.rent import Rent
from CNB_application.models.rent import RentingType
from CNB_application.models.membership import Family


def get_rent(rent_id: str) -> Rent:
    try:
        rent = Rent.get(Rent.id == rent_id)
        return rent
    except DoesNotExist:
        raise RentNotFound


def get_all_rents() -> list[Rent]:
    rents = []
    query = Rent.select()

    for rent in query:
        family, renting_type, date, time_in_minutes = rent.get_data()
        rents.append(
            {
                "family": family,
                "renting_type": renting_type,
                "date": date,
                "time_in_minutes": time_in_minutes,
            }
        )
    logger.debug("Get all rents from db. Number of rents : {}".format(len(rents)))

    return rents


def get_rents_by_family(family_id: str) -> list[Rent]:
    rents = []
    query = Rent.select().where(Rent.family.id == family_id)

    if len(query == 0):
        raise UserNotFound
    for rent in query:
        family, renting_type, date, time_in_minutes = rent.get_data()
        rents.append(
            {
                "family": family,
                "renting_type": renting_type,
                "date": date,
                "time_in_minutes": time_in_minutes,
            }
        )
    logger.debug(
        "Get all rents for family {}. Number of rents : {}".format(
            family.last_name, len(rents)
        )
    )
    return rents


def create_ponton(
    family: Family, renting_type: str, date: str, time_in_minutes: int
) -> Rent:
    try:
        date = datetime.strptime(date, "%Y-%m-%d")
    except (ValueError, TypeError):
        raise InvalidDateFormat
    if renting_type and renting_type not in RentingType:
        raise RentingTypeNotFound
    rent_object = Rent.create(
        family=family,
        renting_type=renting_type,
        date=date,
        time_in_minutes=time_in_minutes,
    )
    rent_object.save()
    return rent_object


def update_rent(
    rent_id: str,
    renting_type: Optional[str],
    date: Optional[str],
    time_in_minutes: Optional[str],
) -> Rent:
    rent = get_rent(rent_id)
    rent.update_rent(renting_type, date, time_in_minutes)
    return rent


def delete_rent(rent_id) -> bool:
    try:
        rent = Rent.get(Rent.id == rent_id)
        rent.delete_instance(recursive=True)
        return True
    except DoesNotExist:
        raise RentNotFound
