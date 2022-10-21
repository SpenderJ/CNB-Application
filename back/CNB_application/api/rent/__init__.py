from __future__ import annotations

from CNB_application.api import api

from .program import Program
from .rent import Rent

api.add_resource(Program, '/program')
api.add_resource(Rent, '/rent')
