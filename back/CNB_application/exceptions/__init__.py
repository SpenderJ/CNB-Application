from __future__ import annotations

from CNB_application.core import logger


class APIError(Exception):
    status_code = 500

    def __init__(self, prefix, message, status_code=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        logger.warning(f'{prefix} error : {message}')

    def to_dict(self):
        return {'error': self.message}


from .users import *  # noqa: F401
from .passwords import *  # noqa: F401
