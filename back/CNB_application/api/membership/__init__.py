from CNB_application.api import api

from .family import Family

api.add_resource(Family, "/family")
