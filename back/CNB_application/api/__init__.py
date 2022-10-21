from __future__ import annotations

import time

from CNB_application.api.errors import register_errors
from CNB_application.core import db
from CNB_application.core import logger
from flask import Blueprint
from flask import current_app
from flask import g
from flask import request
from flask_restful import Api

api_bp = Blueprint('api', __name__)


class AdvancedApi(Api):
    def handle_error(self, e):
        for val in current_app.error_handler_spec.values():
            for handler in val.values():
                registered_error_handlers = list(
                    filter(lambda x: isinstance(e, x), handler.keys()),
                )
                if len(registered_error_handlers) > 0:
                    raise e
        return super().handle_error(e)


api = AdvancedApi(api_bp)


def register_api(app):
    @api_bp.before_request
    def before_request():
        g.start = time.time()
        db.connect(reuse_if_open=True)

    @api_bp.teardown_request
    def after_request(exception=None):
        db.close()
        diff = time.time() - g.start
        logger.info(
            '[Request time] Path : {} {} | Time : {}s'.format(
                request.method,
                request.full_path,
                diff,
            ),
        )

    import CNB_application.api.address  # noqa: F401
    import CNB_application.api.membership  # noqa: F401
    import CNB_application.api.social  # noqa: F401
    import CNB_application.api.utils  # noqa: F401

    register_errors(api_bp)

    app.register_blueprint(api_bp, url_prefix='/api/v1')

    logger.debug('Blueprints successfully registered.')
