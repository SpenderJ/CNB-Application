from __future__ import annotations

from CNB_application.api import api

from .tree import Tree

api.add_resource(Tree, '/tree')
