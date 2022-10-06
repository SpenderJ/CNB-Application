from peewee import DoesNotExist

from CNB_application.exceptions import *
from CNB_application.models.membership.membership import Membership


def get_program(membership_id: str) -> Membership:
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


def get_memberships_by_family(first_name: str, last_name: str) -> list[Membership]:
    memberships = []
    query = Membership.select().where(
        (Membership.family.first_name == first_name)
        & (Membership.family.last_name == last_name)
    )

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
            last_name, len(memberships)
        )
    )
    return memberships


def update_membership_date(membership_id: str, date_start: str) -> Membership:
    membership = get_program(membership_id)
    membership.update_membership_date(date_start)
    return membership


def delete_membership(membership_id: str) -> bool:
    try:
        membership = Membership.get(Membership.id == membership_id)
        membership.delete_instance(recursive=True)
        return True
    except DoesNotExist:
        raise MembershipNotFound
