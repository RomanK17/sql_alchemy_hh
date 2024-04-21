from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict

from models import Workload


class WorkersAddDTO(BaseModel):
    username: str

class WorkersDTO(WorkersAddDTO):
    id: int

