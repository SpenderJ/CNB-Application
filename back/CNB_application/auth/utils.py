from __future__ import annotations

from functools import wraps

from CNB_application.core import logger
from flask import request
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import verify_jwt_in_request


def authenticated(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        me = get_jwt_identity()
        user = me.get('email')
        if user is None:
            user = me.get('id')
        logger.info(
            '[Request] Path : {} {} | User : {}'.format(
                request.method,
                request.full_path,
                user,
            ),
        )
        return fn(*args, **kwargs)

    return wrapper
