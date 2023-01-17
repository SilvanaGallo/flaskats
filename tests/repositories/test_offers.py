import pytest
import unittest
from flaskats.models import Offer, OfferStatus
from flaskats.repositories import SQLAlchemyOffersRepository


class TestSQLAlchemyOffersRepository(unittest.TestCase):

    @pytest.mark.unit
    def test_get_offers(self, app):
        assert False
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

    @pytest.mark.unit
    def test_get_published_offers(self, per_page=2, page=1):
        assert False
    #     return Offer.query.filter_by(status=OfferStatus.PUBLISHED)\
    #                         .paginate(per_page=per_page, page=page)

    @pytest.mark.unit
    def test_create_offer(self, test_client_db, offer_dto):
        assert False
        # with test_client_db() as client:
        #     client.create_offer(offer_dto)

        #     assert 

    @pytest.mark.unit
    def test_get_offer(self, id):
        assert False
    #     return Offer.query.get(id)

    @pytest.mark.unit
    def test_update_offer(self, offer_dto):
        assert False
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

    @pytest.mark.unit
    def test_publish_offer(self, id):
        assert False
    #     updated_offer = Offer.query.get(id)
    #     updated_offer.status=OfferStatus.PUBLISHED
    #     db.session.commit()
    #     return updated_offer  

    @pytest.mark.unit
    def test_get_offer_by_code(self, code):
        assert False
    #     return Offer.query.filter_by(code=code).first()

    @pytest.mark.unit
    def test_get_offer_by_repository_id(self, repository_id):
        assert False
    #     return Offer.query.filter_by(repository_id=repository_id).first()

    @pytest.mark.unit
    def test_delete_offer(self, code):
        assert False
    #     offer_to_delete = self.get_offer_by_code(code)
    #     db.session.delete(offer_to_delete)
    #     db.session.commit()
    #     return True
    