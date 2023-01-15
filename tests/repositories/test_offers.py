import pytest
import unittest
from flaskats.models import Offer, OfferStatus
from flaskats.repositories import SQLAlchemyOffersRepository


class TestSQLAlchemyOffersRepository(unittest.TestCase):

    # def setUp(self, test_client_db):
    #     with app.app_context():
    #         db.create_all()

    #         new_offer = Offer(title=offer_dto.title,
    #                 code=offer_dto.code,
    #                 repository_id=offer_dto.repository_id,
    #                 description=offer_dto.description,
    #                 requirements=offer_dto.requirements,
    #                 salary_range=offer_dto.salary_range,
    #                 status=OfferStatus.DRAFT)
    #         Offer

    # def tearDown(self, app):
        
    # @pytest.mark.unit
    # def test_get_offers(self, app):

    #     with app.app_context():
    #         db.create_all()

    #         new_offer = Offer(title=offer_dto.title,
    #                 code=offer_dto.code,
    #                 repository_id=offer_dto.repository_id,
    #                 description=offer_dto.description,
    #                 requirements=offer_dto.requirements,
    #                 salary_range=offer_dto.salary_range,
    #                 status=OfferStatus.DRAFT)
    #         Offer

    #         per_page = 5
    #         page = 1
            
    #         subject = SQLAlchemyOffersRepository()
    #         result = subject.get_offers(per_page=per_page, page=page)
            
    #         assert len(result.items) == 2

    # def get_published_offers(self, per_page=2, page=1):
    #     return Offer.query.filter_by(status=OfferStatus.PUBLISHED)\
    #                         .paginate(per_page=per_page, page=page)

    # def create_offer(self, offer_dto):
    #     new_offer = Offer(title=offer_dto.title,
    #                 code=offer_dto.code,
    #                 repository_id=offer_dto.repository_id,
    #                 description=offer_dto.description,
    #                 requirements=offer_dto.requirements,
    #                 salary_range=offer_dto.salary_range,
    #                 status=OfferStatus.DRAFT)
    #     db.session.add(new_offer)
    #     db.session.commit()
    #     return new_offer

    # def get_offer(self, id):
    #     return Offer.query.get(id)

    # def update_offer(self, offer_dto):
    #     updated_offer = Offer.query.get(offer_dto.id)
    #     updated_offer.title=offer_dto.title
    #     updated_offer.code=offer_dto.code
    #     updated_offer.repository_id=offer_dto.repository_id
    #     updated_offer.description=offer_dto.description
    #     updated_offer.requirements=offer_dto.requirements
    #     updated_offer.salary_range=offer_dto.salary_range
    #     updated_offer.status=offer_dto.status
    #     db.session.commit()
    #     return updated_offer

    # def publish_offer(self, id):
    #     updated_offer = Offer.query.get(id)
    #     updated_offer.status=OfferStatus.PUBLISHED
    #     db.session.commit()
    #     return updated_offer  

    # def get_offer_by_code(self, code):
    #     return Offer.query.filter_by(code=code).first()

    # def get_offer_by_repository_id(self, repository_id):
    #     return Offer.query.filter_by(repository_id=repository_id).first()

    # def delete_offer(self, code):
    #     offer_to_delete = self.get_offer_by_code(code)
    #     db.session.delete(offer_to_delete)
    #     db.session.commit()
    #     return True
    ...