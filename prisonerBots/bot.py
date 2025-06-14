from typing import Callable

class Bot:
    def __init__(self, submitterName: str, botName: str,funct: Callable[[dict], bool]):
        self.submitterName = submitterName
        self.botName = botName
        self.assignment = ""
        self.oppAssignment = ""
        self.funct = funct  

    def getAction(self, currentRoundHistory: dict): 
        self.funct(currentRoundHistory)
