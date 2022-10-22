from __future__ import annotations

from CNB_application.exceptions import FamilyNotFound
from CNB_application.exceptions import FamilyIDNotFound
from CNB_application.models.membership.family import Family
from peewee import DoesNotExist


def get_family_via_id(family_id: str) -> Family:
    print("HELLO JULES")
    print(family_id)
    print("HELLO JULES")
    try:
        family = Family.get(Family.id == family_id)
        return family
    except DoesNotExist:
        raise FamilyIDNotFound


def get_family(first_name: str, last_name: str) -> Family:
    try:
        family = (
            Family.select()
            .where((Family.first_name == first_name) & (Family.last_name == last_name))
            .get()
        )
        return family
    except DoesNotExist:
        raise FamilyNotFound


def get_all_families() -> list[Family]:
    families = []
    query = Family.select()

    for family in query:
        (
            first_name,
            last_name,
            email,
            phone_number,
            benefactor_member,
            parking,
        ) = family.get_data()
        families.append(
            {
                'first_name': first_name,
                'last_name': last_name,
                'email': email,
                'phone_number': phone_number,
                'benefactor_member': benefactor_member,
                'parking': parking,
            },
        )
    return families


def create_family(
    first_name: str,
    last_name: str,
    email: str,
    phone_number: str,
    benefactor_member: bool,
    parking: bool,
) -> Family:
    family = Family.create(
        first_name=first_name,
        last_name=last_name,
        email=email,
        phone_number=phone_number,
        benefactor_member=benefactor_member,
        parking=parking,
    )
    return family


def update_field_info(family_id: str, field: str, info: str) -> Family:
    family = get_family_via_id(family_id)
    setattr(family, field, info)
    family.save()
    return family


def update_family(
    family_id: str,
    first_name: str | None,
    last_name: str | None,
    email: str | None,
    phone_number: str | None,
    benefactor_member: bool | None,
    parking: bool | None,
) -> Family:
    family = get_family_via_id(family_id)
    family.update_family(
        first_name=first_name,
        last_name=last_name,
        email=email,
        phone_number=phone_number,
        benefactor_member=benefactor_member,
        parking=parking,
    )
    return family


def delete_family(family_id: str) -> bool:
    try:
        family = Family.get(Family.id == family_id)
        family.delete_instance(recursive=True)
        return True
    except DoesNotExist:
        raise FamilyNotFound
