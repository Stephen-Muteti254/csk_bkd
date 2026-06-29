import random
import uuid

from app.extensions import db
from app.models.student_model import Student
from app.services.email_service import (
    send_student_update_email,
    send_student_creation_email
)

class StudentService:

    @staticmethod
    def generate_csk_id():
        return f"CSK-{random.randint(100000,999999)}"

    @staticmethod
    def get_all():
        return Student.query.order_by(Student.created_at.desc()).all()

    @staticmethod
    def get_by_csk_id(csk_id):
        return Student.query.filter_by(
            csk_id=csk_id
        ).first()

    @staticmethod
    def create(data):

        student = Student(
            csk_id=StudentService.generate_csk_id(),
            name=data["name"],
            email=data["email"],
            phone=data["phone"],
            university_id=data["university_id"]
        )

        db.session.add(student)
        db.session.commit()


        # send_student_creation_email()

        return student

    @staticmethod
    def update(csk_id, data):

        student = Student.query.filter_by(
            csk_id=csk_id
        ).first_or_404()

        student.name = data["name"]
        student.email = data["email"]
        student.phone = data["phone"]
        student.university_id = data["university_id"]

        db.session.commit()

        # send_student_update_email()

        return student

    @staticmethod
    def delete(csk_id):

        student = Student.query.filter_by(
            csk_id=csk_id
        ).first_or_404()

        db.session.delete(student)
        db.session.commit()