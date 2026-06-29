from flask import Blueprint, request

from app.services.student_service import StudentService

bp = Blueprint(
    "student",
    __name__,
    url_prefix="/api/v1/admin/students"
)

@bp.get("")
def get_students():

    students = StudentService.get_all()

    return {
        "success": True,
        "data": [
            student.to_dict()
            for student in students
        ]
    }, 200

@bp.get("/<string:csk_id>")
def get_student(csk_id):

    student = StudentService.get_by_csk_id(csk_id)

    if not student:
        return {
            "success": False,
            "message": "Student not found"
        }, 404

    return {
        "success": True,
        "data": student.to_dict()
    }, 200

@bp.post("")
def create_student():

    data = request.get_json()

    student = StudentService.create(data)

    return {
        "success": True,
        "message": "Student created successfully",
        "data": student.to_dict()
    }, 201

@bp.put("/<string:csk_id>")
def update_student(csk_id):

    data = request.get_json()

    student = StudentService.update(
        csk_id,
        data
    )

    return {
        "success": True,
        "message": "Student updated successfully",
        "data": student.to_dict()
    }, 200

@bp.delete("/<string:csk_id>")
def delete_student(csk_id):

    StudentService.delete(csk_id)

    return {
        "success": True,
        "message": "Student deleted successfully"
    }, 200