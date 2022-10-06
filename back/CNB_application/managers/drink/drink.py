from peewee import DoesNotExist
from typing import Optional

from CNB_application.exceptions import *
from CNB_application.models.drink.drink import Drink
from CNB_application.models.membership.family import Family


def get_drink_card(family_id: str) -> Drink:
    try:
        drink = Drink.get(Drink.family == family_id)
        return drink
    except DoesNotExist:
        raise DrinkNotFound


def get_all_drink_cards() -> list[Drink]:
    drinks = []
    query = Drink.select()

    for drink in query:
        family, drinks_left, number_of_card = drink.get_data()
        drinks.append({'family': family, 'drinks_left': drinks_left, 'number_of_card': number_of_card})
    logger.debug('Get all drink objects from db. Number of drink objects : {}'.format(len(drinks)))

    return drinks


def create_drink(family: Family, drinks_left: Optional[int] = 0, number_of_card: Optional[int] = 0) -> Drink:
    drink_card = Drink.create(family=family,
                              drinks_left=drinks_left,
                              number_of_card=number_of_card)
    drink_card.save()
    return Drink


def update_drink(family_id: str, drinks_left: Optional[int], number_of_card: Optional[int]) -> Drink:
    drink_card = get_drink_card(family_id)
    drink_card.update_drink_card(drinks_left, number_of_card)
    return drink_card


def delete_drink(family: Family) -> bool:
    try:
        family.drink.delete_instance(recursive=True)
        return True
    except DoesNotExist:
        raise AddressNotFound
