from __future__ import annotations

from CNB_application.api import api

from .address import Address

api.add_resource(Address, '/address')
