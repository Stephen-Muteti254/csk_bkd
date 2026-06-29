from app.extensions import db
from datetime import datetime
import uuid


class University(db.Model):
    __tablename__ = "csk_universities"

    id = db.Column(
        db.String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )

    name = db.Column(
        db.String(255),
        nullable=False,
        unique=True,
        index=True
    )

    short_name = db.Column(
        db.String(50),
        nullable=True
    )

    location = db.Column(
        db.String(255),
        nullable=True
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False
    )

    students = db.relationship(
        "Student",
        back_populates="university",
        cascade="all, delete-orphan"
    )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "short_name": self.short_name,
            "location": self.location,
            "student_count": len(self.students),
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }