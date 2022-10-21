from __future__ import annotations

from CNB_application.api import api
from CNB_application.api import api_bp

from .me import me
from .users import ProfilePicture
from .users import User
from .users import Users

api_bp.add_url_rule('/me', 'me', me)
api.add_resource(Users, '/users')
api.add_resource(User, '/users/<user_id>')
api.add_resource(ProfilePicture, '/users/<user_id>/profile-picture')
