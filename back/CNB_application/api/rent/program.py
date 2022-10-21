from __future__ import annotations

from CNB_application.auth import authenticated
from CNB_application.managers.membership import family
from CNB_application.managers.rent import program
from flask import request
from flask_restful import Resource


class Program(Resource):
    @authenticated
    def get(self):
        program_id = request.args.get('program_id')
        program_object = program.get_program(program_id=program_id)
        return {'msg': 'success', 'program': program_object}

    @authenticated
    def get_by_family(self):
        family_id = request.args.get('family_id')
        program_objects = program.get_programs_by_family(family_id=family_id)
        return {'msg': 'success', 'programs': program_objects}

    @authenticated
    def put(self):
        program_id = request.args.get('rent_id')
        program_object = program.update_program(
            program_id=program_id,
            sailing_program=request.args.get('sailing_program'),
            date_start=request.args.get('date_start'),
        )
        return {'msg': 'success', 'program': program_object}

    @authenticated
    def post(self):
        family_id = request.args.get('family_id')
        family_object = family.get_family_via_id(family_id=family_id)
        program_object = program.create_program(
            family=family_object,
            sailing_program=request.args.get('sailing_program'),
            date_start=request.args.get('date_start'),
        )
        return {'msg': 'success', 'membership': program_object}

    @authenticated
    def delete(self):
        program.delete_program(request.args.get('program_id'))
        return {'msg': 'success'}
