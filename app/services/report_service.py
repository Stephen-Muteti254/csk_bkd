from app.extensions import db
from app.models.report_model import Report
from app.models.student_model import Student
from app.services.email_service import (
    send_report_status_update_email,
    send_report_creation_email
)

class ReportService:

    @staticmethod
    def get_all():
        return Report.query.order_by(
            Report.created_at.desc()
        ).all()

    @staticmethod
    def get_by_id(report_id):
        return Report.query.get_or_404(report_id)

    @staticmethod
    def create(data):

        student = Student.query.filter_by(
            csk_id=data["csk_id"]
        ).first()

        if not student:
            raise ValueError("Invalid CSK ID")

        report = Report(
            student_id=student.id,
            category=data["category"],
            description=data["description"]
        )

        db.session.add(report)
        db.session.commit()


        # TO DO
        # Send a report creation success email to the student

        return report

    @staticmethod
    def update_status(report_id, status):

        report = Report.query.get_or_404(report_id)

        report.status = status

        db.session.commit()

        # TO DO
        # Send a report status update email to the student

        return report

    @staticmethod
    def delete(report_id):

        report = Report.query.filter_by(
            id=int(report_id)
        ).first_or_404()

        db.session.delete(report)
        db.session.commit()