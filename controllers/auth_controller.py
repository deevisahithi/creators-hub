from flask import request, jsonify

from utils.db import users_collection

from utils.password_helper import (
    hash_password,
    verify_password
)

from utils.jwt_helper import generate_token


def signup():

    data = request.json

    existing_user = users_collection.find_one(
        {
            "email":
            data["email"]
        }
    )

    if existing_user:

        return jsonify({
            "message":
            "User already exists"
        }), 400

    users_collection.insert_one({

        "name":
        data["name"],

        "email":
        data["email"],

        "password":
        hash_password(
            data["password"]
        )
    })

    return jsonify({
        "message":
        "Signup Successful"
    })


def login():

    data = request.json

    user = users_collection.find_one(
        {
            "email":
            data["email"]
        }
    )

    if not user:

        return jsonify({
            "message":
            "User Not Found"
        }), 404

    if not verify_password(
        data["password"],
        user["password"]
    ):

        return jsonify({
            "message":
            "Invalid Password"
        }), 401

    token = generate_token(
        user["email"]
    )

    return jsonify({

        "token":
        token,

        "message":
        "Login Successful"
    })