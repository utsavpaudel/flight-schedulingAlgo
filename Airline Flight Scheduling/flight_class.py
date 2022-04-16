import heapq

class Vertex:
    def __init__(self, name, adjacentVertices):
        self.name=name
        self.adjacentVertices=adjacentVertices

    def __str__(self):
        return f'Airport {self.name} with neighbours {self.adjacentVertices}'

    def __repr__(self):
        return self.name

class Flight:
    def __init__(self,name,origin,destination,arrival,departure):
        self.name=name
        self.origin=origin
        self.destination=destination
        self.arrival=arrival
        self.departure=departure
    
    def __str__(self):
        return f'Flight: {self.name} | Airport({repr(self.origin)}-{repr(self.destination)}) | Arrival: {self.arrival} | Departure: {self.departure}'

    def __repr__(self):
        return self.name

class Graph:
    def __init__(self,vertices,edges):
        self.vertices=vertices
        self.edges=edges
    
#Dijkstra's Algorithm
def FlightAgency(graph, source, destination, start_time):
    node_data={v:{'arrival':float('inf'),'pred':[]} for v in graph.vertices}
    node_data[source]['arrival']=start_time
    queue=[]

    for vertex in graph.vertices:
        #Insert the vertex and time calculated into the min heap
        queue.append((node_data[vertex]['arrival'],id(vertex), vertex))
    heapq.heapify(queue)

    while queue:
        print(queue)
        #While the queue is not empty pop the vertex with minimum arrival time
        v=heapq.heappop(queue)[-1]
        # For all the adjacent vertices of the popped vertex
        for adjacentVertex in v.adjacentVertices:
            # If the adjacent vertex is present in the queue, then the vertex is yet to be visited, else the vertex is visited
            if (node_data[adjacentVertex]['arrival'],id(adjacentVertex),adjacentVertex) in queue:
                flight_queue=[]
                #determining the next flight
                for flight in graph.edges:
                    if (flight.origin==v and flight.destination==adjacentVertex):
                        #check if the departure time of the flight is greater than the arrival time of the origin
                        if(flight.departure>=node_data[v]['arrival']):
                            flight_queue.append((id(flight),flight.arrival))

                heapq.heapify(flight_queue)
                temp_time=float('inf')
                initial_time=0
                if flight_queue:
                    temp_time=flight_queue[0][1]
                
                if temp_time<node_data[adjacentVertex]['arrival']:
                    initial_time= node_data[adjacentVertex]['arrival']
                    node_data[adjacentVertex]['arrival']=temp_time
                    node_data[adjacentVertex]['pred']=node_data[v]['pred']+list(v.name)
                    queue.remove((initial_time, id(adjacentVertex), adjacentVertex))
                    queue.append((node_data[adjacentVertex]['arrival'],id(adjacentVertex),adjacentVertex))
                    heapq.heapify(queue)
            else:
                break
    node_data[destination]['pred']=node_data[destination]['pred']+list(destination.name)
    return node_data[destination]
    

                    



    
    

