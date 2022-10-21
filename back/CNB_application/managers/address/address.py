from __future__ import annotations

from CNB_application.exceptions import AddressNotFound
from CNB_application.models.address.address import Address
from CNB_application.models.membership.family import Family
from peewee import DoesNotExist


def get_address(family_id: str) -> Address:
    try:
        address = Address.get(Address.family == family_id)
        return address
    except DoesNotExist:
        raise AddressNotFound


def get_all_addresses() -> list[Address]:
    addresses = []
    query = Address.select()

    for addresses in query:
        family, address, city, zip_code, country = addresses.get_data()  # type: ignore
        addresses.append(
            {
                'family': family,
                'address': address,
                'city': city,
                'zip_code': zip_code,
                'country': country,
            },
        )

    return addresses


def update_address(
    family_id: str,
    address: str | None,
    city: str | None,
    zip_code: int | None,
    country: str | None,
) -> Address:
    address_object = get_address(family_id)
    address_object.update_address(
        address=address,
        city=city,
        zip_code=zip_code,
        country=country,
    )
    return address_object


def create_address(
    family: Family,
    address: str,
    city: str,
    zip_code: int,
    country: str,
) -> Address:
    address_object = Address.create(
        family=family,
        address=address,
        city=city,
        zip_code=zip_code,
        country=country,
    )
    return address_object


def delete_address(family: Family) -> bool:
    try:
        family.address.delete_instance(recursive=True)
        return True
    except DoesNotExist:
        raise AddressNotFound
