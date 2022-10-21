from __future__ import annotations

from datetime import datetime

from CNB_application.exceptions import UserNotFound
from CNB_application.exceptions import InvalidDateFormat
from CNB_application.exceptions import RentingTypeNotFound
from CNB_application.exceptions import RentNotFound
from CNB_application.models.membership import Family
from CNB_application.models.rent import Rent
from CNB_application.models.rent import RentingType
from peewee import DoesNotExist


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
                'family': family,
                'renting_type': renting_type,
                'date': date,
                'time_in_minutes': time_in_minutes,
            },
        )
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
                'family': family,
                'renting_type': renting_type,
                'date': date,
                'time_in_minutes': time_in_minutes,
            },
        )
    return rents


def create_rent(
    family: Family,
    renting_type: str,
    date: str,
    time_in_minutes: int,
) -> Rent:
    try:
        date = datetime.strptime(date, '%Y-%m-%d')  # type: ignore
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
    renting_type: str | None,
    date: str | None,
    time_in_minutes: str | None,
) -> Rent:
    rent = get_rent(rent_id)
    rent.update_rent(renting_type, date, time_in_minutes)
    return rent


def delete_rent(rent_id: str) -> bool:
    try:
        rent = Rent.get(Rent.id == rent_id)
        rent.delete_instance(recursive=True)
        return True
    except DoesNotExist:
        raise RentNotFound
