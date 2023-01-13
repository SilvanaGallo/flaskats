from dataclasses import dataclass
from dataclasses_json import dataclass_json
from flaskats.models import OfferStatus


@dataclass_json
@dataclass
class Offer:

    repository_id: int
    title: str
    code: str
    salary_range: str
    description: str
    requirements: str
    status: OfferStatus = OfferStatus.DRAFT
