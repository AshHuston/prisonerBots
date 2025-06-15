from matchResults import MatchResult
from bot import Bot

def funct(self, currentMatchHistory: list[MatchResult]) -> bool:
    # This strategy is simple. We start with cooperating, then we just do whatever the opponent did last round.
    # Strategies could be much more complex. Or maybe even simpler.
    willCooperate: bool = True
    if len(currentMatchHistory) > 0:
        #print(currentMatchHistory[-1])
        willCooperate = currentMatchHistory[-1][f'{self.oppAssignment}']['action']   
    print(willCooperate) 
    return willCooperate

TitForTatBot = Bot(
    "Ash Huston",
    "Tit for Tat",
    funct
)