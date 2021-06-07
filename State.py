from enum import Enum

class State(Enum):
    START = 0
    INNUM = 1
    INID = 2
    INASSIGN = 3
    INCOMMENT = 4
    END = 5
