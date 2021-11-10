import csv
import Building
from Calls import Call

# if __name__ == '__main__':
#     rows=[]
#     oly=[]
#     with open("Calls_a.csv") as file:
#         csvreader = csv.reader(file)
#
#         for row in csvreader:
#             o=Call(str=row[0],time=float(row[1]),srcFloor=int(row[2]),destFloor=int(row[3]),status=int(row[4]),assign=int(row[5]))
#             oly.append(o)
#             rows.append(row)
#
#         print(rows)


 if __name__ == '__main__':
    file_name = str(input('Enter file name'))
    rows = []
    oly = []
    size = 0
    with open(file_name) as file:
        csvreader = csv.reader(file)

        for row in csvreader:
            o = Call(str=row[0], time=float(row[1]), srcFloor=int(row[2]), destFloor=int(row[3]), status=int(row[4]), assign=int(row[5]))
            size = size + 1
            oly.append(o)
            rows.append(row)

        print(rows)
        calls = []
        callsElev = []
        numOfElev = Building.Building.size()
        for i in range(0, numOfElev):
            callsElev.append(calls)

        while size != 0:
            call = row[0]
            ans = allocate(call)
            AssignElevator(call, ans)
            rows[0].remove()
            size = size - 1


def allocate(call):
    ans = 0
    numOfElev = Building.Building.size()
    best = 10000
    flag1 = 0
    flag2 = 0
    if numOfElev == 1:
        callsElev[0].append(call)
        return 0

    if numOfElev > 1:
        elev = Building.elevators
        if type(call) == 1 or type(call) == -1:
            for i in range(numOfElev):
                if pos(i) < call.srcFloor:
                    cnt = calculator(call, i)
                    best = min(cnt, best)
                    if cnt == best:
                        flag1 = 1
                        ans = i
        for i in range(numOfElev):
            current = elev[i]
            FinalTime = checkTheTime(callsElev[i], i, call)
            best = min(FinalTime, best)
            if FinalTime == best:
                flag2 = 1;
                ans = i


    if flag1 == 1 and flag2 == 0:
        callsElev[ans].append(0, call)
        return ans
    else:
        callsElev[ans].append(call)

    return ans







def calculator(call, i):
    elev = Building.elevators
    current = elev[i]
    speed = current('_speed')
    OperationTime = current('_stopTime') + current('_openTime') + current('_closeTime') + current('_startTime')
    arrivalTime = abs(call.srcFloor - pos(current)) / speed + OperationTime
    return arrivalTime


def checkTheTime(calls, i,call):
    elev = Building.elevators
    current = elev[i]
    speed = current('_speed')
    OperationTime = current('_stopTime') + current('_openTime')  + current('_startTime')
    for i in range(0,len(calls)):
        src=calculator(call,i)
        dest=abs(call.srcFloor-call.destFloor)/speed+OperationTime
        arrivalTime = arrivalTime+src+dest
    return arrivalTime

def AssignElevator(ans,call):




def typeCall(call):
    dest = call[3]
    src = call[2]
    type = dest - src
    if type > 0:  # if the elevator is UP
        return 1
    elif type < 0:  # if the elevator is DOWN
        return -1
    else:  # if the elevator is LEVEL
        return 0



def pos(i):
    ans=callsElev[i][0].call.srcFloor
    return ans
