from flask import Blueprint

from controllers.post_controller import (
    create_post,
    get_posts,
    like_post,
    comment_post
)

post_bp = Blueprint(
    "post_bp",
    __name__
)

post_bp.route(
    "/create-post",
    methods=["POST"]
)(create_post)

post_bp.route(
    "/posts",
    methods=["GET"]
)(get_posts)

post_bp.route(
    "/like-post/<post_id>",
    methods=["PUT"]
)(like_post)

post_bp.route(
    "/comment-post/<post_id>",
    methods=["POST"]
)(comment_post)