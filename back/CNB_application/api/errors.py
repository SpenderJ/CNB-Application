from __future__ import annotations

from CNB_application.exceptions import APIError
from elasticsearch import NotFoundError
from flask import jsonify
from peewee import DoesNotExist


def register_errors(api):
    @api.errorhandler(APIError)
    def handle_invalid_usage(error):
        response = jsonify(error.to_dict())
        response.status_code = error.status_code
        return response

    @api.errorhandler(DoesNotExist)  # type: ignore
    def handle_invalid_usage(error):  # noqa: F811
        resource = error.args[0].split('>')[0].split(' ')[1]
        response = jsonify({'msg': f'{resource} not found'})
        response.status_code = 404
        return response

    @api.errorhandler(NotFoundError)  # type: ignore
    def handle_invalid_usage(error):  # noqa: F811
        response = jsonify(
            {
                'msg': '{} {} not found'.format(
                    error.info['_index'].capitalize(),
                    error.info['_id'],
                ),
            },
        )
        response.status_code = 404
        return response
