import json
from Elevators import Elevator


class Building:

    def _init_(self) -> None:

        self._minFloor = 0
        self._maxFloor = 0
        self.elevators = []
        self.size = len(self.elevators)

    def add(self, elev: Elevator):
        self.elevators.append(elev)

    def load_json(self, file_name):

        try:
            with open(file_name, "r+") as f:
                build = json.load(f)
                self._minFloor = build["_minFloor"]
                self._maxFloor = build["_maxFloor"]
                self.elevators = build["_elevators"]
                self.size = len(self.elevators)
        except IOError as e:
            print(e)

    def str(self) -> str:
        return f"minFloor:{self._minFloor}\n maxFloor:{self._maxFloor}\n {self.elevators}"

