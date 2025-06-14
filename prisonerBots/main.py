import os
from bot import Bot

class BotResult:
    cooperated: bool
    score: int

class MatchResult:
    botA: BotResult
    botB: BotResult

def getOutputFilePath():
    def ensureOutputFile():
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_dir, "output.txt")
        if not os.path.exists(file_path):
            with open(file_path, 'w') as f:
                pass  # just create the file
        return file_path
    return ensureOutputFile()
        
outputFile = getOutputFilePath()

def simulateRound(actionA: bool, actionB: bool):
    results = [0, 0]
    match [actionA, actionB]:
        case [True, True]:
            results = [3,3]
        case [False, False]:
            results = [1,1]
        case [True, False]:
            results = [0,5]
        case [False, True]:
            results = [5,0]
    return results

def simulateMatch(botA: Bot, botB: Bot, totalRounds: int):
    matchHistory = []
    for i in range(totalRounds):
        botAAction = botA.getAction(),
        botBAction = botB.getAction(),
        roundResults = simulateRound(botAAction, botBAction)
        thisRound = {
            "botAAction": botAAction,
            "botBAction": botBAction,
            "botAScore": roundResults[0],
            "botBScore":roundResults[1],
        }