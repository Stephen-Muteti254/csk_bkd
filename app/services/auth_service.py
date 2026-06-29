from app.models.admin_user import AdminUser
from flask_jwt_extended import create_access_token, create_refresh_token
from datetime import timedelta
from flask import current_app

class AuthService:

    @staticmethod
    def login(email, password):

        user = AdminUser.query.filter(
            AdminUser.email == email.lower(),
            AdminUser.password == password
        ).first()

        if not user:
            raise ValueError("Invalid email or password")

        if not user.is_active:
            raise ValueError("Account disabled")

        access, refresh = AuthService.generate_tokens_for_user(user)

        return {
            "access_token": access,
            "refresh_token": refresh,
            "user": user.to_dict()
        }


    @staticmethod
    def generate_tokens_for_user(user):
        access = create_access_token(
            identity=user.id,
            expires_delta=timedelta(
                seconds=current_app.config.get("ACCESS_EXPIRES", 86400)
            )
        )

        refresh = create_refresh_token(
            identity=user.id,
            expires_delta=timedelta(
                seconds=current_app.config.get("REFRESH_EXPIRES", 604800)
            )
        )

        return access, refresh