
class BotResult:
    cooperated: bool
    score: int

class MatchResult:
    botA: BotResult
    botB: BotResult

class BotData:
    submitterName: str
    botName: str
    assignment: str
    oppAssignment: str