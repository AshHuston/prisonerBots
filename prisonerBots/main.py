import os
from matchResults import MatchResult
from bot import Bot
from alwaysCoop_bot import coopBot
from ASH_bot import TitForTatBot



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

def writeToOutput(history: list):
    f = open(outputFile, 'w')
    for lines in history:
        f.write(f'{lines}\n')
    f.close()

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
    botA.assignment = "botA"
    botB.assignment = "botB"
    botA.oppAssignment = "botB"
    botB.oppAssignment = "botA"

    for i in range(totalRounds):
        botAAction = botA.getAction(matchHistory)
        botBAction = botB.getAction(matchHistory)
        roundResults = simulateRound(botAAction, botBAction)
        thisRound = {
            "botA": {
                "action": botAAction,
                "score": roundResults[0],
            },
            "botB": {
                "action": botBAction,
                "score":roundResults[1],
            }
        }
        matchHistory.append(thisRound)
    writeToOutput(matchHistory)

simulateMatch(coopBot, TitForTatBot, 10)