import json

from flask import request
from flask_restful import Resource
from peewee import DoesNotExist
from playhouse.shortcuts import model_to_dict

from CNB_application.exceptions import *
from CNB_application.auth import authenticated
from CNB_application.managers.membership import family
from CNB_application.managers.address import address


class FamilySearch(Resource):
    @authenticated
    def get(self):
        first_name = request.args.get("first_name")
        last_name = request.args.get("last_name")
        response = family.get_family(first_name=first_name, last_name=last_name)
        return {"msg": f"Family found {last_name}", "family": model_to_dict(response)}


class Family(Resource):
    @authenticated
    def get(self, family_id):
        response = family.get_family_via_id(family_id=family_id)
        return {"family": model_to_dict(response)}

    @authenticated
    def post(self):
        query = json.loads(request.data.decode("utf-8"))
        family_object = family.create_family(
            first_name=query.get("first_name"),
            last_name=query.get("last_name"),
            email=query.get("email"),
            phone_number=query.get("phone_number"),
            benefactor_member=query.get("benefactor_member"),
            parking=query.get("parking"),
        )
        address.create_address(
            family=family_object,
            address=query.get("address"),
            city=query.get("city"),
            zip_code=query.get("zip_code"),
            country=query.get("country"),
        )
        return {"msg": "Family created", "status": 200}

    @authenticated
    def put(self):
        family_id = request.args.get("family_id")
        family.update_family(
            family_id=family_id,
            first_name=request.args.get("first_name"),
            last_name=request.args.get("last_name"),
            email=request.args.get("email"),
            phone_number=request.args.get("phone_number"),
            benefactor_member=request.args.get("benefactor_member"),
            parking=request.args.get("parking"),
        )
        address.update_address(
            family_id=family_id,
            address=request.args.get("address"),
            city=request.args.get("city"),
            zip_code=request.args.get("zip_code"),
            country=request.args.get("country"),
        )
        return {"msg": "success", "family": family}

    @authenticated
    def delete(self):
        try:
            family_id = request.args.get("family_id")
            family_object = family.get_family_via_id(family_id=family_id)
            family_object.delete_instance(recursive=True)
            return True
        except DoesNotExist:
            raise FamilyNotFound
