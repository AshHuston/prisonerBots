from main import MatchResult
from bot import Bot

def funct(currentMatchHistory: list[MatchResult]) -> bool:
# This strategy is simple. We start with cooperating, then we just do whatever the opponent did last round.
# Strategies could be much more complex. Maybe even simpler.
    willCooperate: bool = True
    if len(currentMatchHistory) > 0:
        willCooperate = currentMatchHistory[-1][myBot["oppAssignment"]]["cooperated"]
    print(willCooperate)
    return willCooperate

myBot = Bot(
    "Ash Huston",
    "Tit for Tat",
    funct
)

print(myBot.getAction([]))