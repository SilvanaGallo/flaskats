from dataclasses import dataclass
from dataclasses_json import dataclass_json
from datetime import datetime

@dataclass_json
@dataclass
class Application:
    name: str
    email: str
    job: str
    date: str = datetime.now().isoformat()
    status: str = 'Inbox'
    notified: bool = False