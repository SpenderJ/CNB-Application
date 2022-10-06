from flask import request
from flask_restful import Resource

from CNB_application.auth import authenticated
from CNB_application.managers.membership import family
from CNB_application.managers.membership import membership


class Membership(Resource):
    @authenticated
    def get(self):
        membership_id = request.args.get("membership_id")
        membership_object = membership.get_membership(membership_id=membership_id)
        return {"msg": "success", "membership": membership_object}

    @authenticated
    def get_by_family(self):
        family_id = request.args.get("family_id")
        membership_objects = membership.get_memberships_by_family(family_id=family_id)
        return {"msg": "success", "memberships": membership_objects}

    @authenticated
    def put(self):
        membership_id = request.args.get("membership_id")
        membership_object = membership.get_membership(membership_id=membership_id)
        membership_object = membership.update_membership(
            membership=membership_object,
            membership_type=request.args.get("membership_type"),
            date_start=request.args.get("date_start"),
        )
        return {"msg": "success", "membership": membership_object}

    @authenticated
    def post(self):
        family_id = request.args.get("family_id")
        family_object = family.get_family_via_id(family_id=family_id)
        membership_object = membership.create_membership(
            family=family_object,
            membership_type=request.args.get("membership_type"),
            date_start=request.args.get("date_start"),
        )
        return {"msg": "success", "membership": membership_object}

    @authenticated
    def delete(self):
        membership.delete_membership(request.args.get("membership_id"))
        return {"msg": "success"}
