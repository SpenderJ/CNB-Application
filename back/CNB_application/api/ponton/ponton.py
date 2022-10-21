from __future__ import annotations

from CNB_application.auth import authenticated
from CNB_application.managers.membership import family
from CNB_application.managers.ponton import ponton
from flask import request
from flask_restful import Resource


class Ponton(Resource):
    @authenticated
    def get(self):
        ponton_id = request.args.get('ponton_id')
        ponton_object = ponton.get_ponton(ponton_id=ponton_id)
        return {'msg': 'success', 'ponton': ponton_object}

    @authenticated
    def get_by_family(self):
        family_id = request.args.get('family_id')
        ponton_objects = ponton.get_pontons_by_family(family_id=family_id)
        return {'msg': 'success', 'pontons': ponton_objects}

    @authenticated
    def put(self):
        ponton_id = request.args.get('ponton_id')
        ponton_object = ponton.update_ponton(
            ponton_id=ponton_id,
            boat_size=request.args.get('boat_size'),
            date_start=request.args.get('date_start'),
            date_end=request.args.get('date_end'),
        )
        return {'msg': 'success', 'ponton': ponton_object}

    @authenticated
    def post(self):
        family_id = request.args.get('family_id')
        family_object = family.get_family_via_id(family_id=family_id)
        ponton_object = ponton.create_ponton(
            family=family_object,
            boat_size=request.args.get('boat_size'),
            date_start=request.args.get('date_start'),
            date_end=request.args.get('date_end'),
        )
        return {'msg': 'success', 'membership': ponton_object}

    @authenticated
    def delete(self):
        ponton.delete_ponton(request.args.get('ponton_id'))
        return {'msg': 'success'}
