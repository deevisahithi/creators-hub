from flask import Blueprint

from controllers.profile_controller import (
    create_profile,
    get_profiles
)

profile_bp = Blueprint(
    "profile_bp",
    __name__
)

profile_bp.route(
    "/create-profile",
    methods=["POST"]
)(create_profile)

profile_bp.route(
    "/profiles",
    methods=["GET"]
)(get_profiles)