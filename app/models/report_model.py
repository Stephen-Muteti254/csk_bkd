from datetime import datetime
from app.extensions import db


class Report(db.Model):
    __tablename__ = "csk_reports"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    student_id = db.Column(
        db.Integer,
        db.ForeignKey("csk_students.id"),
        nullable=False
    )

    category = db.Column(
        db.String(100),
        nullable=False
    )

    description = db.Column(
        db.Text,
        nullable=False
    )

    status = db.Column(
        db.String(30),
        nullable=False,
        default="Pending"
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    student = db.relationship(
        "Student",
        backref="reports"
    )

    def to_dict(self):
        return {
            "id": str(self.id),
            "student_id": self.student_id,
            "csk_id": self.student.csk_id,
            "studentName": self.student.name,
            "universityName": self.student.university.name,
            "category": self.category,
            "description": self.description,
            "status": self.status,
            "createdAt": self.created_at.isoformat(),
            "updatedAt": self.updated_at.isoformat()
        }