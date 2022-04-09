from flight_class import *
from datetime import time

# Helper Functions

def convert_to_float(dt):
    return dt.hour+dt.minute/60.0

def convert_to_time(ft):
    return '{0:02.0f}:{1:02.0f}'.format(*divmod(ft * 60, 60))

#Airports are the Vertices of the Grapg
airportE=Vertex('E',[])
airportD=Vertex('D',[airportE])
airportB=Vertex('B',[airportE])
airportC=Vertex('C',[airportB])
airportA=Vertex('A',[airportB,airportC,airportD])

vertices=[airportA,airportB,airportC,airportD,airportE]

#Flights are the edges of the graph
#Flight(Name, Origin, Desitination, Arrival, Departure)
flights = [
    Flight('F1', airportA, airportB, convert_to_float(time(6,30)), convert_to_float(time(2,0))),
    Flight('F2', airportA, airportB, convert_to_float(time(8,30)), convert_to_float(time(3,30))),
    Flight('F3', airportA, airportC, convert_to_float(time(4,0)), convert_to_float(time(2,0))),
    Flight('F4', airportA, airportD, convert_to_float(time(5,0)), convert_to_float(time(1,30))),
    Flight('F5', airportB, airportE, convert_to_float(time(9,15)), convert_to_float(time(7,15))),
    Flight('F6', airportC, airportB, convert_to_float(time(5,0)), convert_to_float(time(4,30))),
    Flight('F7', airportD, airportE, convert_to_float(time(17,0)), convert_to_float(time(13,0))),
    Flight('F8', airportD, airportE, convert_to_float(time(12,0)), convert_to_float(time(10,0)))
]

graph=Graph(vertices,flights)

if __name__=="__main__":
    #Starting Point/ Source
    startVertex=airportA
    # End Point/ Destination
    endVertex=airportE
    #Start Time
    startTime=convert_to_float(time(2,0))

    #Applying Dijkstra's Shortest Path Alogrithm
    shortestRoute = FlightAgency(graph, startVertex, endVertex, startTime)

    #Displaying the result
    print("Vertices in the Graph")
    for vertex in vertices:
        print(str(vertex))
    print("Edges in the Graph")
    for flight in flights:
        print(str(flight))
    if shortestRoute['arrival'] != float('inf'):
        print(f'The earliest arrival time from airport {startVertex} to the airport {endVertex} is {convert_to_time(shortestRoute["arrival"])} using the route {shortestRoute["pred"]}')
    else:
        print(f'There are no available flights from airport {startVertex} to airport {endVertex} after {convert_to_time(startTime)}')
   