from peewee import DoesNotExist
from typing import Optional
from datetime import datetime

from CNB_application.exceptions import *
from CNB_application.models.membership import Membership
from CNB_application.models.membership import Family
from CNB_application.models.membership import MembershipType


def get_membership(membership_id: str) -> Membership:
    try:
        membership = Membership.get(Membership.id == membership_id)
        return membership
    except DoesNotExist:
        raise MembershipNotFound


def get_all_memberships() -> list[Membership]:
    memberships = []
    query = Membership.select()

    for membership in query:
        family, membership_type, date_start, date_end = membership.get_data()
        memberships.append(
            {
                "family": family,
                "membership_type": membership_type,
                "date_start": date_start,
                "date_end": date_end,
            }
        )
    logger.debug(
        "Get all memberships from db. Number of memberships : {}".format(
            len(memberships)
        )
    )

    return memberships


def get_memberships_by_family(family_id: str) -> list[Membership]:
    memberships = []
    query = Membership.select().where((Membership.family.id == family_id))

    if len(query == 0):
        raise UserNotFound
    for membership in query:
        family, membership_type, date_start, date_end = membership.get_data()
        memberships.append(
            {
                "family": family,
                "membership_type": membership_type,
                "date_start": date_start,
                "date_end": date_end,
            }
        )
    logger.debug(
        "Get all memberships for family {}. Number of memberships : {}".format(
            family.last_name, len(memberships)
        )
    )
    return memberships


def create_membership(family: Family, membership_type: str, date_start: str):
    try:
        date_start = datetime.strptime(date_start, "%Y-%m-%d")
    except (ValueError, TypeError):
        raise InvalidDateFormat
    if membership_type not in MembershipType:
        raise MembershipTypeNotFound
    membership_object = Membership.create(
        family=family, membership_type=membership_type, date_start=date_start
    )
    membership_object.set_end_date()
    return membership_object


def update_membership(
    membership: Membership, membership_type: Optional[str], date_start: Optional[str]
) -> Membership:
    membership.update_membership(membership_type=membership_type, date_start=date_start)
    return membership


def delete_membership(membership_id: str) -> bool:
    try:
        membership = Membership.get(Membership.id == membership_id)
        membership.delete_instance(recursive=True)
        return True
    except DoesNotExist:
        raise MembershipNotFound
