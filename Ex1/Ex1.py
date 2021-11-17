import csv
import sys
from Building import Building
from Calls import Call
from Elevators import Elevator


def allocate(call): #return the int of the elevator that be answer on the call
    ans = 0
    numOfElev = b1.size
    best = 10000
    flag1 = 0
    flag2 = 0
    if numOfElev == 1: #if there one elevator in the building
        callsElevators[0].append(call) #add the call to the only elevator in the building
        return 0 #return the index of the elevator
    if numOfElev > 1:#if there is more than one elevator
        if type(call) == 1 or type(call) == -1:#if the type of the call is UP or DOWN
            for i in range(numOfElev):
                if current_floor[i] < int(call[2]): #if the elevator position is low then the src of the call
                    cnt = calculator(call, i) #calculate the time of answer on the call of i elevator
                    best = min(cnt, best) #check who is the fastest
                    if cnt == best:
                        flag1 = 1
                        ans = i
        for i in range(numOfElev):
            FinalTime = checkTheTime(callsElevators[i], i, call) #calculate the time of answer on the call of every elevator list
            best = min(FinalTime, best) #check who is the fastest
            if FinalTime == best:
                flag2 = 1;
                ans = i

    if flag1 == 1 and flag2 == 0:
        callsElevators[ans].append(call) #adding the call to the elevator we found the best for answer the call
        return ans #return the index of the elevator that need to answer the call
    else:
        callsElevators[ans].append(call) #adding the call to the elevator we found the best for answer the call
    current_floor[ans] = (int(call[3]))
    return ans #return the index of the elevator that need to answer the call


def calculator(call, i): #function that calculate the time of  i elevator to go the src of the call c
    elev = b1.elevators
    current = elev[i] #get elevator in index elev
    if int(call[2]) == current_floor[i]:
        return 0
    speed = current['_speed']
    OperationTime = current['_stopTime'] + current['_openTime'] + current['_startTime'] + current['_closeTime'] #amount of elevator start time
    arrivalTime = (abs(int(call[2]) - current_floor[i]))/speed + OperationTime #calculate the time of  i elevator to go the src of the call c
    return arrivalTime # the time of  i elevator to go the src of the call c


def checkTheTime(calls, i, call):
    elev = b1.elevators
    current = elev[i] #get elevator in index elev
    arrivalTime = 0 #variable that saving the time of the elevator to arrival
    speed = current['_speed']
    OperationTime = current['_stopTime'] + current['_openTime'] + current['_startTime'] #amount of elevator start time
    for j in range(0, len(calls)):
        src = calculator(call, i) #check src of call to the pos of the elevator time
        dest = abs((int(call[2]) - int(call[3])))/speed  #check src-dst time
        arrivalTime = arrivalTime + src + dest
    return arrivalTime + OperationTime


def typeCall(call):
    dest = int(call[3])
    src = int(call[2])
    type = dest - src
    if type > 0:  # if the elevator is UP
        return 1
    elif type < 0:  # if the elevator is DOWN
        return -1
    else:  # if the elevator is LEVEL
        return 0


if __name__ == '__main__':
    file_=sys.argv[1]
    file_name = sys.argv[2]
    out_name = sys.argv[3]
    rows = []
    cnt = []
    size = 0
    #reader from csv
    with open(file_name) as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            o = Call(str=row[0], time=float(row[1]), srcFloor=int(row[2]), destFloor=int(row[3]), status=int(row[4]),
                     assign=int(row[5]))
            cnt.append(o)
            rows.append(row)

        b1 = Building()
        b1.load_json(file_)
        Building.add(b1, b1.elevators)
        calls = []
        callsElevators = []
        numOfElev = b1.size
        # list of calls
        for i in range(0, numOfElev):
            callsElevators.append(calls)
        # list of current_floor of the elevators
        current_floor = []
        for t in range(0, numOfElev):
            current_floor.append(0)
    # write from csv
    for i in range(0, len(rows)):
        c = rows[i]
        ans = allocate(c)
        rows[i] = Call(str=rows[i][0], time=float(rows[i][1]), srcFloor=int(rows[i][2]), destFloor=int(rows[i][3]),status=int(rows[i][4]), assign=int(ans))
        print(rows[i])
        with open(out_name, 'w') as csv_file:
            for i in rows:
                csv_file.write(str(i) + '\n')
