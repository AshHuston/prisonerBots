from matchResults import MatchResult
from bot import Bot

# You can store and access any variables you want to persist between rounds with the dict self.additionalVars
# These will be scoped only to the current itertation of the tournament.

def funct(self, currentMatchHistory: list[MatchResult]) -> bool:
    willCooperate: bool = None

    #
    # Your code here
    #

    return willCooperate

strategy = Bot(
    "Author name",  # <-- Change this
    "Bot name",     # <-- Change this
    funct
)