from peewee import DoesNotExist

from CNB_application.exceptions import *
from CNB_application.models.drink.drink import Drink


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


def update_number_of_drink(family_id: str, drinks_left: int) -> Drink:
    drink = get_drink_card(family_id)
    drink.drinks_left = drinks_left
    drink.save()
    return drink


def update_number_of_card(family_id: str, number_of_card: int) -> Drink:
    drink = get_drink_card(family_id)
    drink.number_of_card = number_of_card
    drink.save()
    return drink
