import smtplib
from email.message import EmailMessage
from flask import current_app, render_template
from datetime import datetime
from app.utils.mailer import send_email
from app.models.user import User

COMPANY_NAME = "Campus Support Kenya"

from markupsafe import Markup

def send_report_creation_email(student, report):
	onboarding_url = f"{current_app.config['FRONTEND_URL']}"
	try:
        send_email(
            to=student.email,
            subject="Your Report has been received",
            html=render_template(
                "emails/report_received.html",
                title=report.category,
                full_name=user.name,
                onboarding_url=onboarding_url,
                company_name=COMPANY_NAME,
                year=datetime.utcnow().year,
            ),
        )
    except Exception as e:
        current_app.logger.error(
            f"Failed to send report creation email to {user.email}: {e}"
        )

def send_report_status_update_email(student, report):
	onboarding_url = f"{current_app.config['FRONTEND_URL']}"
	try:
        send_email(
            to=student.email,
            subject="Your report status has been updated",
            html=render_template(
                "emails/report_update.html",
                title=report.category,
                full_name=user.name,
                onboarding_url=onboarding_url,
                company_name=COMPANY_NAME,
                year=datetime.utcnow().year,
            ),
        )
    except Exception as e:
        current_app.logger.error(
            f"Failed to send report update email to {user.email}: {e}"
        )

def send_student_update_email(student):
	onboarding_url = f"{current_app.config['FRONTEND_URL']}"
	try:
        send_email(
            to=student.email,
            subject="Your CSK profile has been updated",
            html=render_template(
                "emails/student_update.html",
                title="Welcome to CSK",
                full_name=user.name,
                onboarding_url=onboarding_url,
                company_name=COMPANY_NAME,
                year=datetime.utcnow().year,
            ),
        )
    except Exception as e:
        current_app.logger.error(
            f"Failed to send student update email to {user.email}: {e}"
        )

def send_student_creation_email(student):
	onboarding_url = f"{current_app.config['FRONTEND_URL']}"
	try:
        send_email(
            to=student.email,
            subject="Your writer application has been approved",
            html=render_template(
                "emails/application_approved.html",
                title="Application Approved",
                full_name=user.name,
                onboarding_url=onboarding_url,
                company_name=COMPANY_NAME,
                year=datetime.utcnow().year,
            ),
        )
    except Exception as e:
        current_app.logger.error(
            f"Failed to send approval email to {user.email}: {e}"
        )