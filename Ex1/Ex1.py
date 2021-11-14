import csv
from Building import Building
from Calls import Call




def allocate(call):
    ans = 0
    numOfElev = b1.size
    best = 10000
    flag1 = 0
    flag2 = 0
    if numOfElev == 1:
        callsElevators[0].append(call)
        return 0

    if numOfElev > 1:
        # if type(call) == 1 or type(call) == -1:
        #     for i in range(0,numOfElev):
        #         if pos(i) < call.srcFloor:
        #             cnt = calculator(call, i)
        #             best = min(cnt, best)
        #             if cnt == best:
        #                 flag1 = 1
        #                 ans = i
        for i in range(0,numOfElev):
            FinalTime = checkTheTime(callsElevators[i], i, call)
            if best>FinalTime:
                best =FinalTime
                ans=i
        finalElev=callsElevators[ans]
        position=findPosition(call, finalElev,ans)
        callsElevators[ans].insert(position,call)


    return ans



# def calculator(call, i):
#     elev = Building.Building.getElev()
#     current = elev[i]
#     speed = current["_speed"]
#     OperationTime = current["_stopTime"] + current["_openTime"] + current["_closeTime"] + current["_startTime"]
#     arrivalTime = abs(call.srcFloor - pos(i)) / speed + OperationTime
#     return arrivalTime
def calculator2calls(call,call_2,i):
    elev = b1.elevators
    current = elev[i]
    speed = current["_speed"]
    OperationTime = current["_stopTime"] + current["_openTime"] + current["_closeTime"] + current["_startTime"]
    arrivalTime = abs(int(call[2]) - int(call_2[2])) / speed + OperationTime
    return arrivalTime



def checkTheTime(calls, i,call):
    elev = b1.elevators
    current = elev[i]
    speed = current["_speed"]
    OperationTime = current["_stopTime"] + current["_openTime"]  + current["_startTime"]
    ans=10000000
    arrivalTime =0
    for j in range(0,len(calls)):
        src=calculator2calls(call,calls[j],i)
        dest=abs(int(call[2])-int(call[3]))/speed+OperationTime
        arrivalTime = arrivalTime+src+dest
        ans=min(ans,arrivalTime)
    return ans





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



def pos(i):
    ans=callsElevators[i][0].call.srcFloor
    return ans

def findPosition(call, finalElev,i):
    elev = b1.elevators
    current = elev[i]
    speed = current["_speed"]
    OperationTime = current["_stopTime"] + current["_openTime"] + current["_closeTime"] + current["_startTime"]
    best=10000
    position=0
    for j in range(0,len(finalElev)):
        arrivalTime = abs(int(call[2]) - int(finalElev[j][2])) / speed + OperationTime
        if  best>arrivalTime:
            best=arrivalTime
            position=j
    return position

if __name__ == '__main__':
    file_name = str(input('Enter file name'))
    rows = []
    oly = []
    size = 0
    with open(file_name) as file:
        csvreader = csv.reader(file)

        for row in csvreader:
            o = Call(str=row[0], time=float(row[1]), srcFloor=int(row[2]), destFloor=int(row[3]), status=int(row[4]), assign=int(row[5]))
            oly.append(o)
            rows.append(row)

        print(rows)
        file_ = str(input('Enter file name'))
        b1 = Building()
        b1.load_json(file_)
        Building.add(b1,b1.elevators)
        calls = []
        callsElevators = []
        numOfElev =b1.size
        for i in range(0, numOfElev):
            callsElevators.append(calls)

    for i in range(0,len(rows)):
            c=rows[i]
            ans = allocate(c)
            rows[i] = Call(str=rows[i][0], time=float(rows[i][1]), srcFloor=int(rows[i][2]), destFloor=int(rows[i][3]), status=int(rows[i][4]),assign=int(ans))
            print(rows[i])



