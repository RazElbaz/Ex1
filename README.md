# Ex1
Several relevant links-Literature survey:
Link Number 1:
https://elevation.fandom.com/wiki/Destination_dispatch  

Link Number 2: 
http://co-at-work.zib.de/berlin2009/downloads/2009-10-01/2009-10-01-1100-BH-Online-Optimization.pdf

Link Number 3:
https://www.youtube.com/watch?v=MJhXqAbQ23I&t=2s

Problem space:
An offline algorithm is an optimal algorithm that stamps the user inputs further, pre-calculating the answers in it based on the input given.
The algorithm will be able to execute the most efficient program and will plan the operation of the elevator without any expected changes. Therefore, this algorithm is more efficient in terms of getting passengers to the destination at the best speed without delays like long waiting times or duplications in elevator calls.

Offline algorithm design:
The algorithm will assign the call to the elevator which will perform it in the shortest time.
The algorithm will pre-determine the number of elevators in the building, the inputs, minimum and maximum floor, different times of elevator operations — such as elevator 
opening and closing time,start and stop time and elevator speed. At each input, the algorithm will receive the data: time, current floor and target floor. First, the algorithm will look at the inputs times received in advance, set a minimum time to respond to requests for the same destination floor and direction, and create a to-do list for each elevator. For example, if two inputs are known for a particular floor by a predetermined minimum difference, the algorithm will know to unite the two requests in the first place and assign them the same elevator without providing two different elevators and cause a reduction in efficiency.
Second, the algorithm will define elevators for ascent and descent according to the execution list, as well as for late requests for elevators that are not in operation, the algorithm will know the router to the floor from which you will have to move. The algorithm will execute all requests with minimum time and maximum efficiency by taking into account all the information received in advance and thus, be able to plan the operation of each elevator without sudden changes or new requests.

Explanation of the Class:

Elevator - a class that maintains an elevator has the following values: minimum and maximum floors, speeds, and more. Receives the information from the list of elevators received from the building.
Building - a class that defines a building, receives the data: minimum and maximum floor and a list of existing elevators from the building, receives the information from the JSON file.
Calls - a class that keeps read and receives the following values: time, target floor and source, and more. receives its information from a CSV file.
Ex1 - The algorithm we recorded, gets a JSON file of a building, a CSV file of calls and an output CSV file. The algorithm goes through each calls and creates a list for each elevator of its readings, each call is embedded in the elevator that will perform the reading in the shortest time and then the algorithm records the output (the elevator that will perform the reading) to the output file.

Example of running to building 5 with calls D (if we want to run something else we will change the names):
Go to the folder where all the documents are and we will write the following line in cmd :
First we need to put in a list with the names:
python3 Ex1 B5.json Calls_d.csv d5.csv
java -jar Ex1_checker_V1.2_obf.jar 209399294,207276775 B5.json d5t.csv log.log

The output we get: 
the lines of all the readings
And the final answer:
Code Owners, 209399294,207276775, Building_file, B5.json, Calls, d5.csv
Total waiting time: 136574.37365999998, average waiting time per call: 136.57437366, unCompleted calls, 10, certificate, -480815520 
