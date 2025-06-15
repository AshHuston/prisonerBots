from matchResults import MatchResult
from bot import Bot

def funct(self, currentMatchHistory: list[MatchResult]) -> bool:
# This strategy will always cooperate
    willCooperate: bool = True
    return willCooperate

strategy = Bot(
    "Westley Huston",
    "Always cooperate",
    funct
)