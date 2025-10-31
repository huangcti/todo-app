from __future__ import annotations
from pydantic import BaseModel, Field, ConfigDict
from typing import Literal
from datetime import datetime

class Task(BaseModel):
    model_config = ConfigDict(
        json_schema_extra={
            "examples": [{"id": 1, "text": "買牛奶", "status": "pending"}]
        }
    )

    id: int
    text: str = Field(min_length=1, max_length=1000)
    status: Literal["pending", "done"] = "pending"
    created_at: str
    updated_at: str | None = None
