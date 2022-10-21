from __future__ import annotations

from CNB_application.api import api

from .family import Family
from .family import FamilySearch
from .membership import Membership

api.add_resource(FamilySearch, '/family')
api.add_resource(Family, '/family/<family_id>')
api.add_resource(Membership, '/membership')
