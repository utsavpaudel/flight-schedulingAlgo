from status import Flight, Vertex, Graph, FlightAgency

# The airports as vertices
airportE = Vertex("E", [])
airportD = Vertex("D", [airportE])
airportB = Vertex("B", [airportD, airportE])
airportC = Vertex("C", [airportB])
airportA = Vertex("A", [airportC, airportB])


if __name__ == '__main__':
    # List the flights for airports
    flights = [
        Flight('KP Oli-1', airportA, airportB,  6, 2),
        Flight('KP Oli-2', airportA, airportC,  8, 2),
        Flight('KP Oli-3', airportB, airportD,  13, 12),
        Flight('KP Oli-4', airportB, airportE,  17, 11),
        Flight('KP Oli-5', airportC, airportB,  10, 9),
        Flight('KP Oli-6', airportC, airportD,  10, 6),
        Flight('KP Oli-7', airportD, airportE,  14, 13),
    ]

    # Graph with airports as vertices
    graph = Graph([airportA, airportB, airportC, airportD, airportE])


    '''user input'''

    # Origin Airport be airportA and destination be airportE
    startVertex = airportC
    endVertex = airportD
    # Start time be 2 (Time in 24 hour format)
    startT = 2


    earliestArrivalTime = FlightAgency(flights, graph, startVertex, endVertex, startT)
    if (earliestArrivalTime != float("inf")):
        print(f'The earliest arrival time for the airport {endVertex} from airport {startVertex} is {earliestArrivalTime}:00.')
    else:
        print(f'No flight from airport {startVertex} to airport {endVertex} after {startT}:00.')
