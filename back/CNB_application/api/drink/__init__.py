from __future__ import annotations

from CNB_application.api import api

from .drink import Drink

api.add_resource(Drink, '/drink')
