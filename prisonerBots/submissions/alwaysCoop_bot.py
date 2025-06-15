from matchResults import MatchResult
from bot import Bot

def funct(self, currentMatchHistory: list[MatchResult]) -> bool:
# This strategy will always defect
    willCooperate: bool = False
    return willCooperate

strategy = Bot(
    "Westley Huston",
    "Always defect",
    funct
)