from dataclasses import dataclass
from dataclasses_json import dataclass_json
from datetime import datetime
from flaskats.models import ApplicationStatus


@dataclass_json
@dataclass
class Application:

    name: str
    email: str
    job: str
    disqualify_reason: str = ''
    hired_at: str = ""
    date: str = datetime.now().isoformat()
    status: str = ApplicationStatus.INBOX
    notified: bool = False
    
