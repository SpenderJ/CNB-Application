from peewee import DoesNotExist
from typing import Optional

from CNB_application.exceptions import *
from CNB_application.models.address.address import Address
from CNB_application.models.membership.family import Family


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
        family, address, city, zip_code, country = addresses.get_data()
        addresses.append(
            {
                "family": family,
                "address": address,
                "city": city,
                "zip_code": zip_code,
                "country": country,
            }
        )
    logger.debug(
        "Get all address objects from db. Number of address objects : {}".format(
            len(addresses)
        )
    )

    return addresses


def update_address(
    family_id: str,
    address: Optional[str],
    city: Optional[str],
    zip_code: Optional[int],
    country: Optional[str],
) -> Address:
    address_object = get_address(family_id)
    address_object.update_address(
        address=address, city=city, zip_code=zip_code, country=country
    )
    return address_object


def create_address(
    family: Family, address: str, city: str, zip_code: int, country: str
) -> Address:
    address_object = Address.create(
        family=family, address=address, city=city, zip_code=zip_code, country=country
    )
    address_object.save()
    return address_object


def delete_address(family: Family) -> bool:
    try:
        family.address.delete_instance(recursive=True)
        return True
    except DoesNotExist:
        raise AddressNotFound
