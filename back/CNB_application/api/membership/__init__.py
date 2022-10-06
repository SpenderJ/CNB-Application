from CNB_application.api import api

from .family import Family
from .membership import Membership

api.add_resource(Family, "/family")
api.add_resource(Membership, "/membership")
