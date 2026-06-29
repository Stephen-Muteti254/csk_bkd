from app.extensions import db
from app.models.university import University

class UniversityService:

    @staticmethod
    def create(data):

        existing = University.query.filter(
            db.func.lower(University.name)
            == data["name"].lower()
        ).first()

        if existing:
            raise ValueError("University already exists")

        university = University(
            name=data["name"],
            short_name=data.get("short_name"),
            location=data.get("location"),
        )

        db.session.add(university)
        db.session.commit()

        return university


    @staticmethod
    def update(university_id, data):

        university = University.query.get(university_id)

        if not university:
            raise ValueError("University not found")

        university.name = data["name"]
        university.short_name = data.get("short_name")
        university.location = data.get("location")

        db.session.commit()

        return university

    @staticmethod
    def delete(university_id):

        university = University.query.get(university_id)

        if not university:
            raise ValueError("University not found")

        db.session.delete(university)

        db.session.commit()

        return True


    @staticmethod
    def get(university_id):
        return University.query.get(university_id)


    @staticmethod
    def list(page=1, per_page=20, search=None):

        query = University.query

        if search:
            search = f"%{search}%"

            query = query.filter(
                db.or_(
                    University.name.ilike(search),
                    University.short_name.ilike(search),
                    University.location.ilike(search),
                )
            )

        pagination = query.order_by(
            University.name.asc()
        ).paginate(
            page=page,
            per_page=per_page,
            error_out=False
        )

        return pagination