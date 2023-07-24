from typing import List

import pydantic

from define import *


class PreferenceItem(pydantic.BaseModel):
    house_name: str
    score: float

    @pydantic.validator("house_name")
    @classmethod
    def check_house_name(cls, v):
        if v not in HOUSE_NAMES:
            raise ValueError("house_name must be in HOUSE_NAMES")
        return v


class StudentAgent(object):
    next_candidate = 0

    def __init__(self, id, name, house_preference: List[PreferenceItem]):
        self.id = id
        self.name = name
        self.house_preference = house_preference
        self.house_preference_dict = {item.house_name: item.score for item in house_preference}

    def get_next_candidate(self):
        if self.next_candidate >= len(self.house_preference):
            raise IndexError("No more candidate")
        candidate = self.house_preference[self.next_candidate]
        self.next_candidate += 1
        return candidate
