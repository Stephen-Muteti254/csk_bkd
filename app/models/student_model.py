from datetime import datetime
from app.extensions import db


class Student(db.Model):
    __tablename__ = "csk_students"

    id = db.Column(db.Integer, primary_key=True)

    csk_id = db.Column(
        db.String(30),
        unique=True,
        nullable=False,
        index=True
    )

    name = db.Column(
        db.String(255),
        nullable=False
    )

    email = db.Column(
        db.String(255),
        unique=True,
        nullable=False
    )

    phone = db.Column(
        db.String(20),
        nullable=False
    )

    university_id = db.Column(
        db.String(36),
        db.ForeignKey("csk_universities.id"),
        nullable=False
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

    university = db.relationship(
        "University",
        back_populates="students"
    )

    def to_dict(self):
        return {
            "id": self.id,
            "csk_id": self.csk_id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "universityId": self.university_id,
            "universityName": self.university.name if self.university else None,
            "created_at": self.created_at.isoformat()
        }