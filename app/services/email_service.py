from datetime import datetime
from flask import current_app, render_template
from app.utils.mailer import send_email

COMPANY_NAME = "Campus Support Kenya"


def send_report_creation_email(student, report):
    try:
        send_email(
            to=student.email,
            subject="We've received your support request",
            html=render_template(
                "emails/report_received.html",
                title="Support Request Received",
                full_name=student.name,
                report=report,
                company_name=COMPANY_NAME,
                year=datetime.utcnow().year,
            ),
        )
    except Exception as e:
        current_app.logger.error(
            f"Failed to send report creation email to {student.email}: {e}"
        )


def send_report_status_update_email(student, report):
    try:
        send_email(
            to=student.email,
            subject="Update on your support request",
            html=render_template(
                "emails/report_update.html",
                title="Support Request Updated",
                full_name=student.name,
                report=report,
                company_name=COMPANY_NAME,
                year=datetime.utcnow().year,
            ),
        )
    except Exception as e:
        current_app.logger.error(
            f"Failed to send report update email to {student.email}: {e}"
        )


def send_student_creation_email(student):
    try:
        send_email(
            to=student.email,
            subject="Welcome to Campus Support Kenya",
            html=render_template(
                "emails/student_registered.html",
                title="Registration Successful",
                full_name=student.name,
                student=student,
                company_name=COMPANY_NAME,
                year=datetime.utcnow().year,
            ),
        )
    except Exception as e:
        current_app.logger.error(
            f"Failed to send registration email to {student.email}: {e}"
        )


def send_student_update_email(student):
    try:
        send_email(
            to=student.email,
            subject="Your CSK profile has been updated",
            html=render_template(
                "emails/student_updated.html",
                title="Profile Updated",
                full_name=student.name,
                student=student,
                company_name=COMPANY_NAME,
                year=datetime.utcnow().year,
            ),
        )
    except Exception as e:
        current_app.logger.error(
            f"Failed to send profile update email to {student.email}: {e}"
        )