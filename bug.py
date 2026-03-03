import uuid
from datetime import datetime

class Bug:
    def __init__(self, title, description, priority):
        self.id = str(uuid.uuid4())
        self.title = title
        self.description = description
        self.priority = priority
        self.status = "Open"
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
            "status": self.status,
            "created_at": self.created_at
        }
    

    