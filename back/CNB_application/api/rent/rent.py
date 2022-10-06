from flask import request
from flask_restful import Resource

from CNB_application.auth import authenticated
from CNB_application.managers.membership import family
from CNB_application.managers.rent import rent


class Ponton(Resource):
    @authenticated
    def get(self):
        rent_id = request.args.get("rent_id")
        rent_object = rent.get_rent(rent_id=rent_id)
        return {"msg": "success", "rent": rent_object}

    @authenticated
    def get_by_family(self):
        family_id = request.args.get("family_id")
        rent_objects = rent.get_rents_by_family(family_id=family_id)
        return {"msg": "success", "rents": rent_objects}

    @authenticated
    def put(self):
        rent_id = request.args.get("rent_id")
        rent_object = rent.update_rent(
            rent_id=rent_id,
            renting_type=request.args.get("renting_type"),
            date=request.args.get("date"),
            time_in_minutes=request.args.get("time_in_minutes"),
        )
        return {"msg": "success", "rent": rent_object}

    @authenticated
    def post(self):
        family_id = request.args.get("family_id")
        family_object = family.get_family_via_id(family_id=family_id)
        rent_object = rent.create_ponton(
            family=family_object,
            renting_type=request.args.get("renting_type"),
            date=request.args.get("date"),
            time_in_minutes=request.args.get("time_in_minutes"),
        )
        return {"msg": "success", "membership": rent_object}

    @authenticated
    def delete(self):
        rent.delete_rent(request.args.get("rent_id"))
        return {"msg": "success"}
