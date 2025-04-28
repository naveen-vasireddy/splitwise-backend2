from pydantic import BaseModel
from typing import List
from datetime import date

class Group(BaseModel):
    groupId: str
    groupName: str
    userIds: List[str]
    creationDate: date

# its working, lets look at other things
# so fetching group by userid is working.
# 