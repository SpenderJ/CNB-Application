from __future__ import annotations

from CNB_application.api import api

from .ponton import Ponton

api.add_resource(Ponton, '/ponton')
