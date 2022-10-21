from __future__ import annotations

from CNB_application.exceptions import AddressNotFound
from CNB_application.exceptions import DrinkNotFound
from CNB_application.models.drink.drink import Drink
from CNB_application.models.membership.family import Family
from peewee import DoesNotExist


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
        drinks.append(
            {
                'family': family,
                'drinks_left': drinks_left,
                'number_of_card': number_of_card,
            },
        )
    return drinks


def create_drink(
    family: Family,
    drinks_left: int | None = 0,
    number_of_card: int | None = 0,
) -> Drink:
    drink_card = Drink.create(
        family=family,
        drinks_left=drinks_left,
        number_of_card=number_of_card,
    )
    drink_card.save()
    return Drink


def update_drink(
    family_id: str,
    drinks_left: int | None,
    number_of_card: int | None,
) -> Drink:
    drink_card = get_drink_card(family_id)
    drink_card.update_drink_card(drinks_left, number_of_card)
    return drink_card


def delete_drink(family: Family) -> bool:
    try:
        family.drink.delete_instance(recursive=True)
        return True
    except DoesNotExist:
        raise AddressNotFound
