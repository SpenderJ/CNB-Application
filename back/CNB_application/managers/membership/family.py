from peewee import DoesNotExist
from typing import Optional


from CNB_application.exceptions import *
from CNB_application.models.membership.family import Family


def get_family_via_id(family_id: str) -> Family:
    try:
        family = Family.get(Family.id == family_id)
        return family
    except DoesNotExist:
        raise FamilyNotFound


def get_family(first_name: str, last_name: str) -> Family:
    try:
        family = Family.get(Family.first_name == first_name, Family.last_name == last_name)
        return family
    except DoesNotExist:
        raise FamilyNotFound


def get_all_families() -> list[Family]:
    families = []
    query = Family.select()

    for family in query:
        first_name, last_name, email, phone_number, benefactor_member, parking = family.get_data()
        families.append({'first_name': first_name, 'last_name': last_name, 'email': email,
                         'phone_number': phone_number, 'benefactor_member': benefactor_member, 'parking': parking})
    logger.debug('Get all familys from db. Number of families : {}'.format(len(families)))

    return families


def create_family(first_name: str, last_name: str, email: str, phone_number: str, benefactor_member: bool, parking: bool) -> Family:
    family = Family.create(first_name=first_name,
                           last_name=last_name,
                           email=email,
                           phone_number=phone_number,
                           benefactor_member=benefactor_member,
                           parking=parking)
    family.save()
    return family


def update_family(family_id: str, first_name: Optional[str], last_name: Optional[str], email: Optional[str],
                  phone_number: Optional[str], benefactor_member: Optional[bool], parking: Optional[bool]) -> Family:
    family = get_family_via_id(family_id)
    family.update_family(first_name=first_name,
                         last_name=last_name,
                         email=email,
                         phone_number=phone_number,
                         benefactor_member=benefactor_member,
                         parking=parking)
    return family


def delete_family(family_id: str) -> bool:
    try:
        family = Family.get(Family.id == family_id)
        family.delete_instance(recursive=True)
        return True
    except DoesNotExist:
        raise FamilyNotFound
