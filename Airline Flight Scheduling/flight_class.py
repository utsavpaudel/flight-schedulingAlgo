import heapq

class Vertex:
    def __init__(self, name, adjacentVertices):
        self.name=name
        self.adjacentVertices=adjacentVertices

    def __repr__(self):
        return self.name

class Flight:
    def __init__(self,name,origin,destination,arrival,departure):
        self.name=name
        self.origin=origin
        self.destination=destination
        self.arrival=arrival
        self.departure=departure
    
    def __repr__(self):
        return self.name

class Graph:
    def __init__(self,vertices):
        self.vertices=vertices
    
#Dijkstra's Algorithm
def FlightAgency(flights, graph, source, destination, start_time):
    # Initializing the arrival time
    T={}
    T[source]=start_time

    # for all vertices which are not source set T[vertex]=infinity
    for vertex in graph.vertices:
        if vertex is not source:
            T[vertex]=float('inf')

    queue=[]

    for vertex in graph.vertices:
        #Insert the vertex and time calculated into the min heap
        heapq.heappush(queue,(T[vertex],id(vertex), vertex))

    while queue:
        #While the queue is not empty pop the vertex with minimum arrival time
        v=heapq.heappop(queue)[-1]
        # For all the adjacent vertices of the popped vertex
        for adjacentVertex in v.adjacentVertices:
            # If the adjacent vertex is present in the queue, then the vertex is yet to be visited, else the vertex is visited
            if (T[adjacentVertex],id(adjacentVertex),adjacentVertex) in queue:
                flight_queue=[]
                #determining the next flight
                for flight in flights:
                    if (flight.origin==v and flight.destination==adjacentVertex):
                        #check if the departure time of the flight is greater than the arrival time of the origin
                        if(flight.departure>=T[v]):
                            heapq.heappush(flight_queue,(id(flight),flight.arrival))
                        
                temp_time=float('inf')
                
                if flight_queue:
                    temp_time=flight_queue[0][1]
                
                if temp_time<T[adjacentVertex]:
                    T[adjacentVertex]=temp_time
                    heapq.heappush(queue,(T[adjacentVertex],id(adjacentVertex),adjacentVertex))
            else:
                break
    
    return T[destination]
    

                    



    
    

