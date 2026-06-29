from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

from app.services.university_service import UniversityService

bp = Blueprint(
    "universities",
    __name__,
    url_prefix="/api/v1/admin/universities"
)


@bp.post("")
@jwt_required()
def create_university():

    data = request.get_json()

    university = UniversityService.create(data)

    return jsonify({
        "success": True,
        "message": "University created",
        "data": university.to_dict()
    }), 201


@bp.get("")
@jwt_required()
def list_universities():

    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 20, type=int)

    search = request.args.get("search")

    result = UniversityService.list(
        page=page,
        per_page=per_page,
        search=search
    )

    return jsonify({
        "success": True,
        "data": [u.to_dict() for u in result.items],
        "pagination": {
            "page": result.page,
            "pages": result.pages,
            "total": result.total,
            "per_page": result.per_page
        }
    })


@bp.get("/<string:university_id>")
@jwt_required()
def get_university(university_id):

    university = UniversityService.get(university_id)

    if not university:
        return jsonify({
            "success": False,
            "message": "University not found"
        }), 404

    return jsonify({
        "success": True,
        "data": university.to_dict()
    })


@bp.put("/<string:university_id>")
@jwt_required()
def update_university(university_id):

    data = request.get_json()

    university = UniversityService.update(
        university_id,
        data
    )

    return jsonify({
        "success": True,
        "message": "University updated",
        "data": university.to_dict()
    })


@bp.delete("/<string:university_id>")
@jwt_required()
def delete_university(university_id):

    UniversityService.delete(university_id)

    return jsonify({
        "success": True,
        "message": "University deleted"
    })