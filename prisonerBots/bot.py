from typing import Callable

class Bot:
    def __init__(self, submitterName: str, botName: str,funct: Callable[['Bot', dict], bool]):
        self.submitterName = submitterName
        self.botName = botName
        self.funct = funct  
        self.assignment = ""
        self.oppAssignment = ""
        self.additionalVars = {}

    def getAction(self, currentRoundHistory: dict): 
        return self.funct(self, currentRoundHistory)
    
    
