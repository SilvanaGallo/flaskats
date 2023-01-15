import pytest
from flaskats.models import Offer, OfferStatus


class TestOfferStatus:

    @pytest.mark.unit
    def test_draft_creation_and_print(self):
        app_status = OfferStatus.DRAFT
        assert str(app_status) == "DRAFT"
        assert app_status.value == 1

    @pytest.mark.unit
    def test_published_creation_and_print(self):
        app_status = OfferStatus.PUBLISHED
        assert str(app_status) == "PUBLISHED"
        assert app_status.value == 2


class TestOffer:

    @pytest.mark.unit
    def test_offer_creation_and_print(self):
        created_offer = Offer(repository_id=123456,
                              title="An offer",
                              code="ABC-123",
                              salary_range="1000-2000",
                              description="a text description",
                              requirements="many requirements",
                              status=OfferStatus.DRAFT)
        str_version = str(created_offer)
        assert "Offer" in str_version
        assert str(created_offer.repository_id) in str_version
        assert created_offer.title in str_version

    def test_published(self) -> bool:
        created_offer = Offer(repository_id=123456,
                              title="An offer",
                              code="ABC-123",
                              salary_range="1000-2000",
                              description="a text description",
                              requirements="many requirements",
                              status=OfferStatus.PUBLISHED)
        assert created_offer.status == OfferStatus.PUBLISHED
        assert created_offer.published()
