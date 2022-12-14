from __future__ import annotations

from CNB_application.auth import authenticated
from CNB_application.managers.social import users
from flask import jsonify
from flask_jwt_extended import get_jwt_identity


@authenticated
def me():
    me_id = get_jwt_identity()['id']
    user = users.get(me_id)
    profile, account_activated, first_login = user.get_data()
    return jsonify(
        {
            'profile': profile,
            'account_activated': account_activated,
            'first_login': first_login,
        },
    )
