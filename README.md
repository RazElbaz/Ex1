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
The algorithm will be able to execute the most efficient program and will plan the operation of the elevator without any expected changes. Therefore, this algorithm is more efficient in terms of getting passengers to the destination at the best speed without delays and will have long waiting times or duplications in elevator calls.

Offline algorithm design:
The algorithm will pre-determine the number of elevators in the building, the inputs, minimum and maximum floor, different times of elevator operations — such as elevator 
opening / closing time, and elevator speed. At each input, the algorithm will receive the data: time, current floor and target floor. First, the algorithm will look at the inputs times received in advance, set a minimum time to respond to requests for the same destination floor and direction, and create a to-do list for each elevator. For example, if two inputs are known for a particular floor by a predetermined minimum difference, the algorithm will know to unite the two requests in the first place and assign them the same elevator without providing two different elevators and cause a reduction in efficiency.
Second, the algorithm will define elevators for ascent and descent according to the execution list, as well as for late requests for elevators that are not in operation, the algorithm will know the router to the floor from which you will have to move. The algorithm will execute all requests with minimum time and maximum efficiency by taking into account all the information received in advance and thus, be able to plan the operation of each elevator without sudden changes or new requests.
