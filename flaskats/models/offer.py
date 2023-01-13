from flaskats import db
from enum import Enum


class OfferStatus(Enum):
    DRAFT = 1
    PUBLISHED = 2

    def __str__(self):
        return str(self.name)


class Offer(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    repository_id = db.Column(db.Integer, unique=True, nullable=True)
    title = db.Column(db.String(50), unique=False, nullable=False)
    code = db.Column(db.String(10), unique=True, nullable=True)
    salary_range = db.Column(db.String(50), unique=False, nullable=False)
    description = db.Column(db.Text, nullable=False)
    requirements = db.Column(db.Text, nullable=False)
    status = db.Column(db.Enum(OfferStatus))

    def __repr__(self):
        return f"Offer({self.repository_id},{self.title})"

    def published(self) -> bool:
        return self.status == OfferStatus.PUBLISHED
