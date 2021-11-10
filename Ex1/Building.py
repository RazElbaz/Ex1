from Elevators import Elevator
import json

class Building:

    def __init__(self) -> None:

        self._minFloor=0
        self._maxFloor=0
        self.elevators = {}

    def add(self, elev: Elevator):
            self.elevators[elev._id] = elev

        



    def load_json(self, file_name):

        try:
            with open(file_name,"r+") as f:
                new_elev={}
                my_d=json.load(f)
                self._minFloor=my_d["_minFloor"]
                self._maxFloor = my_d["_maxFloor"]
                pe_d=my_d["_elevators"]
                for k,v in pe_d.items():
                    elev=Elevator(**v)
                    new_elev[elev.id]=elev
                self.elevators=new_elev
        except IOError as e:
            print(e)

    def __str__(self) -> str:
        return "{self.elevators}\n_minFloor: {self._minFloor}\n _maxFloor: {self._maxFloor}"

    def getElev(self):
        return self.elevators
    def getMaxFloor(self):
        return self._maxFloor
    def getMinFloor(self):
        return self._minFloor
    def size(self):
        return len(self.elevators)


