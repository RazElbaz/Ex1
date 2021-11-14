import json
from Elevators import Elevator


class Building:



 def __init__(self) -> None:

            self._minFloor=0
            self._maxFloor=0
            self.elevators = []
            self.size=len(self.elevators)


 def add(self, elev: Elevator):
            self.elevators.append(elev)

 def load_json(self, file_name):

    try:
        with open(file_name, "r+") as f:
                build = json.load(f)
                self._minFloor = build["_minFloor"]
                self._maxFloor = build["_maxFloor"]
                self.elevators = build["_elevators"]
                self.size=len(self.elevators)
    except IOError as e:
            print(e)

 def _str_(self) -> str:
        return f"minFloor:{self._minFloor}\n maxFloor:{self._maxFloor}\n {self.elevators}"

 def getElev(self):
     return self.elevators


 def getMaxFloor(self):
    return self._maxFloor


 def getMinFloor(self):
    return self._minFloor


