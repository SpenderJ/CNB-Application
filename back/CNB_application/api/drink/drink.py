from flask import request
from flask_restful import Resource

from CNB_application.auth import authenticated
from CNB_application.exceptions import *
from CNB_application.managers.membership import family
from CNB_application.managers.drink import drink


class Drink(Resource):
    @authenticated
    def get(self):
        family_id = request.args.get("family_id")
        drink_card = drink.get_drink_card(family_id=family_id)
        return {"msg": "success", "drink_card": drink_card}

    @authenticated
    def put(self):
        family_id = request.args.get("family_id")
        drink_card = drink.get_drink_card(family_id=family_id)
        drink_card.update_drink(
            family_id=family_id,
            drinks_left=request.args.get("drinks_left"),
            number_of_card=request.args.get("number_of_card"),
        )
        return {"msg": "success", "drink_card": drink_card}

    @authenticated
    def buy_new_card(self):
        family_id = request.args.get("family_id")
        drink_card = drink.get_drink_card(family_id=family_id)
        drink_card.buy_new_card()
        return {"msg": "success", "drink_card": drink_card}

    @authenticated
    def post(self):
        family_id = request.args.get("family_id")
        if drink.get_drink_card(family_id=family_id):
            raise DrinkCardAlreadyCreatedForThisAccount
        family_object = family.get_family_via_id(
            family_id=request.args.get("family_id")
        )
        drink.create_drink(
            family=family_object,
            drinks_left=request.args.get("drinks_left"),
            number_of_card=request.args.get("number_of_card"),
        )
        return {"msg": "success", "family": family}

    @authenticated
    def delete(self):
        family_object = family.get_family_via_id(
            family_id=request.args.get("family_id")
        )
        drink.delete_drink(family_object)
        return {"msg": "success"}
