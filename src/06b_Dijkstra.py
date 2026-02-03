from __future__ import annotations

import heapq


# Using adjacency list
# Assuming static vertices
# Dynamic vertices would require tracking "self.free_ids"
class GraphAdjacencyList:
    def __init__(self, num_vertices: int) -> None:
        self.num_vertices = num_vertices
        self.adjacency_list = {i: [] for i in range(num_vertices)}

    def add_edge(self, u: int, v: int, weight: float) -> None:
        """Add an undirected weighted edge. O(1) time, O(1) space."""
        if u >= self.num_vertices or v >= self.num_vertices or u < 0 or v < 0:
            raise ValueError("Vertices are out of bounds")

        self.adjacency_list[u].append((v, weight))
        self.adjacency_list[v].append((u, weight))  # If the graph is undirected

    def dijkstra(self, start: int) -> dict[int, float]:
        """Find shortest distances from start to all vertices. O((V + E) log V) time, O(V) space."""
        distances = {i: float("inf") for i in range(self.num_vertices)}
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
class GraphAdjacencyMatrix:
    def __init__(self, num_vertices: int) -> None:
        self.num_vertices = num_vertices
        self.adjacency_matrix = [[float('inf')] * num_vertices for _ in range(num_vertices)]
        for i in range(num_vertices):
            self.adjacency_matrix[i][i] = 0

    def add_edge(self, u: int, v: int, weight: float) -> None:
        """Add an undirected weighted edge. O(1) time, O(1) space."""
        if u >= self.num_vertices or v >= self.num_vertices or u < 0 or v < 0:
            raise ValueError("Vertices are out of bounds")

        self.adjacency_matrix[u][v] = weight
        self.adjacency_matrix[v][u] = weight  # If the graph is undirected

    def dijkstra(self, start: int) -> list[float]:
        """Find shortest distances from start to all vertices. O(V^2) time, O(V) space."""
        distances = [float("inf")] * self.num_vertices
        distances[start] = 0
        visited = set()

        for _ in range(self.num_vertices):
            # Find the unvisited vertex with the smallest distance
            min_vertex = -1
            min_distance = float("inf")
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
                if weight != float('inf') and neighbor not in visited:
                    new_distance = distances[min_vertex] + weight
                    if new_distance < distances[neighbor]:
                        distances[neighbor] = new_distance

        return distances


if __name__ == "__main__":
    # Test graph:
    #     (4)     (2)
    #   0-----1-----2
    #   |     |     |
    #  (5)   (3)   (1)
    #   |     |     |
    #   +-----3-----+

    # Adjacency List
    g1 = GraphAdjacencyList(4)
    g1.add_edge(0, 1, 4)
    g1.add_edge(0, 3, 5)
    g1.add_edge(1, 2, 2)
    g1.add_edge(1, 3, 3)
    g1.add_edge(2, 3, 1)

    dist1 = g1.dijkstra(0)
    assert dist1[0] == 0, "Distance to self should be 0"
    assert dist1[1] == 4, "Shortest path 0->1 should be 4"
    assert dist1[2] == 6, "Shortest path 0->1->2 should be 6"
    assert dist1[3] == 5, "Shortest path 0->3 should be 5"

    # Adjacency Matrix
    g2 = GraphAdjacencyMatrix(4)
    g2.add_edge(0, 1, 4)
    g2.add_edge(0, 3, 5)
    g2.add_edge(1, 2, 2)
    g2.add_edge(1, 3, 3)
    g2.add_edge(2, 3, 1)

    dist2 = g2.dijkstra(0)
    assert dist2[0] == 0, "Distance to self should be 0"
    assert dist2[1] == 4, "Shortest path 0->1 should be 4"
    assert dist2[2] == 6, "Shortest path 0->1->2 should be 6"
    assert dist2[3] == 5, "Shortest path 0->3 should be 5"

    print("All tests passed!")
