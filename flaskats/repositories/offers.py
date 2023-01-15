from abc import ABC, abstractmethod
from flaskats.models import Offer, OfferStatus
from flaskats import db


class OffersRepository(ABC):

    @abstractmethod
    def get_offers(self, per_page, page):
        return

    @abstractmethod
    def get_offer(self, code):
        return

    @abstractmethod
    def get_published_offers(self, per_page, page):
        return

    @abstractmethod
    def create_offer(self, offer):
        return

    @abstractmethod
    def update_offer(self, offer):
        return

    @abstractmethod
    def publish_offer(self, id):
        return

    @abstractmethod
    def get_offer_by_code(self, code):
        return
    
    @abstractmethod
    def get_offer_by_repository_id(self, repository_id):
        return

    @abstractmethod
    def delete_offer(self, code):
        return


class SQLAlchemyOffersRepository(OffersRepository):

    def get_offers(self, per_page=2, page=1):
        return Offer.query.paginate(per_page=per_page, page=page)

    def get_published_offers(self, per_page=2, page=1):
        return Offer.query.filter_by(status=OfferStatus.PUBLISHED)\
                            .paginate(per_page=per_page, page=page)

    def create_offer(self, offer_dto):
        new_offer = Offer(title=offer_dto.title,
                    code=offer_dto.code,
                    repository_id=offer_dto.repository_id,
                    description=offer_dto.description,
                    requirements=offer_dto.requirements,
                    salary_range=offer_dto.salary_range,
                    status=OfferStatus.DRAFT)
        db.session.add(new_offer)
        db.session.commit()
        return new_offer

    def get_offer(self, id):
        return Offer.query.get(id)

    def update_offer(self, offer_dto):
        updated_offer = Offer.query.get(offer_dto.id)
        updated_offer.title=offer_dto.title
        updated_offer.code=offer_dto.code
        updated_offer.repository_id=offer_dto.repository_id
        updated_offer.description=offer_dto.description
        updated_offer.requirements=offer_dto.requirements
        updated_offer.salary_range=offer_dto.salary_range
        updated_offer.status=offer_dto.status
        db.session.commit()
        return updated_offer

    def publish_offer(self, id):
        updated_offer = Offer.query.get(id)
        updated_offer.status=OfferStatus.PUBLISHED
        db.session.commit()
        return updated_offer  

    def get_offer_by_code(self, code):
        return Offer.query.filter_by(code=code).first()

    def get_offer_by_repository_id(self, repository_id):
        return Offer.query.filter_by(repository_id=repository_id).first()

    def delete_offer(self, code):
        offer_to_delete = self.get_offer_by_code(code)
        db.session.delete(offer_to_delete)
        db.session.commit()
        return True
