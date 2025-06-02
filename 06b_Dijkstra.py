import heapq


# Using adjacency list
# Assuming static vertices
# Dynamic vertices would require tracking "self.free_ids"
class Graph_AdjacencyList:
    def __init__(self, num_vertices: int) -> None:
        self.num_vertices = num_vertices
        self.adjacency_list = {i: [] for i in range(num_vertices)}

    def add_edge(self, u: int, v: int, weight: float) -> None:
        if u >= self.num_vertices or v >= self.num_vertices or u < 0 or v < 0:
            raise ValueError("Vertices are out of bounds")

        self.adjacency_list[u].append((v, weight))
        self.adjacency_list[v].append((u, weight))  # If the graph is undirected

    def dijkstra(self, start: int) -> dict[int, float]:
        distances = {i: float('inf') for i in range(self.num_vertices)}
        distances[start] = 0
        pq = [(0, start)]  # (distance, vertex)
        
        while pq:
            curr_dist, vertex = heapq.heappop(pq)
            
            if curr_dist > distances[vertex]:
                continue
            
            for neighbor, weight in self.adjacency_list[vertex]:
                distance = curr_dist + weight
                
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))
        
        return distances
    

# Using adjacency matrix
class Graph_AdjacencyMatrix:
    def __init__(self, num_vertices: int) -> None:
        self.num_vertices = num_vertices
        self.adjacency_matrix = [[0] * num_vertices for _ in range(num_vertices)]

    def add_edge(self, u: int, v: int, weight: float) -> None:
        if u >= self.num_vertices or v >= self.num_vertices or u < 0 or v < 0:
            raise ValueError("Vertices are out of bounds")
        
        self.adjacency_matrix[u][v] = weight
        self.adjacency_matrix[v][u] = weight  # If the graph is undirected

    def dijkstra(self, start: int) -> list[float]:
        distances = [float('inf')] * self.num_vertices
        distances[start] = 0
        visited = set()

        for _ in range(self.num_vertices):
            # Find the unvisited vertex with the smallest distance
            min_vertex = -1
            min_distance = float('inf')
            for vertex in range(self.num_vertices):
                if vertex not in visited and distances[vertex] < min_distance:
                    min_vertex = vertex
                    min_distance = distances[vertex]
            
            # No reachable vertices left
            if min_vertex == -1:
                break  

            visited.add(min_vertex)

            # Update distances to neighboring vertices
            for neighbor in range(self.num_vertices):
                weight = self.adjacency_matrix[min_vertex][neighbor]
                if weight > 0 and neighbor not in visited:
                    new_distance = distances[min_vertex] + weight
                    if new_distance < distances[neighbor]:
                        distances[neighbor] = new_distance

        return distances