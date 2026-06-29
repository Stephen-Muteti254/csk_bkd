from flask import Blueprint, request, jsonify
from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity
)

from app.models.admin_user import AdminUser
from app.services.auth_service import AuthService


bp = Blueprint(
    "auth",
    __name__,
    url_prefix="/api/v1/auth"
)

@bp.post("/login")
def login():

    data = request.get_json()

    try:

        result = AuthService.login(
            data["email"],
            data["password"]
        )

        return jsonify({
            "success": True,
            "message": "Login successful",
            "data": result
        }), 200

    except ValueError as e:

        print(str(e))

        return jsonify({
            "success": False,
            "message": str(e)
        }), 401


@bp.get("/me")
@jwt_required()
def me():

    user_id = get_jwt_identity()

    user = AdminUser.query.get(user_id)

    if not user:
        return jsonify({
            "success": False,
            "message": "User not found"
        }), 404

    return jsonify({
        "success": True,
        "data": user.to_dict()
    })


