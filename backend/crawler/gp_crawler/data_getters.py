from dataclasses import dataclass


@dataclass
class ReviewData:
    id: str
    user_name: str
    content: str
    score: int
