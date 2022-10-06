from CNB_application.api import api

from .address import Address

api.add_resource(Address, "/address")
