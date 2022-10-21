from __future__ import annotations

from CNB_application.auth import authenticated
from CNB_application.exceptions import AddressAlreadyCreatedForThisAccount
from CNB_application.managers.address import address
from CNB_application.managers.membership import family
from flask import request
from flask_restful import Resource


class Address(Resource):
    @authenticated
    def get(self):
        family_id = request.args.get('family_id')
        address_object = family.get_family_via_id(family_id=family_id).address
        return {'msg': 'success', 'address': address_object}

    @authenticated
    def put(self):
        family_id = request.args.get('family_id')
        address.update_address(
            family_id=family_id,
            address=request.args.get('address'),
            city=request.args.get('city'),
            zip_code=request.args.get('zip_code'),
            country=request.args.get('country'),
        )
        return {'msg': 'success', 'family': family}

    @authenticated
    def post(self):
        family_id = request.args.get('family_id')
        if family.get_family_via_id(family_id=family_id).address:
            raise AddressAlreadyCreatedForThisAccount
        family_object = family.get_family_via_id(family_id=family_id)
        address.create_address(
            family=family_object,
            address=request.args.get('address'),
            city=request.args.get('city'),
            zip_code=request.args.get('zip_code'),
            country=request.args.get('country'),
        )
        return {'msg': 'success', 'family': family}

    @authenticated
    def delete(self):
        family_object = family.get_family_via_id(
            family_id=request.args.get('family_id'),
        )
        address.delete_address(family_object)
        return {'msg': 'success'}
