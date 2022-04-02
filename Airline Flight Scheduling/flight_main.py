from flight_class import *
from datetime import time

#Airports are the Vertices of the Grapg
airportE=Vertex('E',[])
airportD=Vertex('D',[airportE])
airportB=Vertex('B',[airportE])
airportC=Vertex('C',[airportB])
airportA=Vertex('A',[airportB,airportC,airportD])

def convert_to_float(dt):
    return dt.hour+dt.minute/60.0

def convert_to_time(ft):
    return '{0:02.0f}:{1:02.0f}'.format(*divmod(ft * 60, 60))

if __name__=="__main__":
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

    graph=Graph([airportA,airportB,airportC,airportD,airportE])

    #Starting Point/ Source
    startVertex=airportA
    # End Point/ Destination
    endVertex=airportB
    #Start Time
    startTime=convert_to_float(time(4,0))

    #Applying Dijkstra's Shortest Path Alogrithm
    earliestArrivalTime = FlightAgency(flights, graph, startVertex, endVertex, startTime)

    #Displaying the result
    if (earliestArrivalTime != float("inf")):
        print(f'The earliest arrival time for the airport {endVertex} from airport {startVertex} is {convert_to_time(earliestArrivalTime)}')
    else:
        print(f'No flight from airport {startVertex} to airport {endVertex} after {convert_to_time(startTime)}')