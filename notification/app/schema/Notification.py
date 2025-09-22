from pydantic import BaseModel, Field

class Notification(BaseModel):
    message: str = Field(..., min_length=1, description="Message to send")