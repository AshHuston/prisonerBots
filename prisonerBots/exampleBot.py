from main import MatchResult, BotData

myBot: BotData = {
    "submitterName": "Ash Huston",
    "botName": "Tit for Tat",
    "assignment":  "",
    "oppAssignment": "",
}

def getAction(currentMatchHistory: list[MatchResult]) -> bool:
# This strategy is simple. We start with cooperating, then we just do whatever the opponent did last round.
    willCooperate: bool = True
    if len(currentMatchHistory) > 0:
        willCooperate = currentMatchHistory[-1][myBot["oppAssignment"]]["cooperated"]

    return willCooperate
