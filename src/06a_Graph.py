from collections import deque
# from typing import Optional


# Option 1: Using adjacency list
class Graph_AdjacencyList:
    def __init__(self, num_vertices: int) -> None:
        self.num_vertices = num_vertices
        self.next_id = num_vertices  # Tracks the highest ID ever issued
        self.free_ids = []

        # Initialize adjacency list
        # Consider `defaultdict(list)` if node labels are arbitrary
        self.adjacency_list = {i: [] for i in range(num_vertices)}

        # Print the graph
        self.display()

    def display(self) -> None:
        """Print the adjacency list. O(V + E) time."""
        for vertex in self.adjacency_list:
            print(vertex, ":", self.adjacency_list[vertex])

    def add_edge(self, start: int, end: int) -> None:
        """Add a directed edge. O(V) time."""
        if start not in self.adjacency_list or end not in self.adjacency_list:
            raise ValueError("Vertices are out of bounds")

        if end not in self.adjacency_list[start]:
            # For weighted graphs, store each edge as a tuple: (neighbor, weight)
            self.adjacency_list[start].append(end)

        # Uncomment for undirected graph (but be aware that methods like topological_sort will not work)
        # if start not in self.adjacency_list[end]:
        #     self.adjacency_list[end].append(start)

    def remove_edge(self, start: int, end: int) -> None:
        """Remove a directed edge. O(V) time."""
        if start not in self.adjacency_list or end not in self.adjacency_list:
            raise ValueError("Vertices are out of bounds")

        if end in self.adjacency_list[start]:
            self.adjacency_list[start].remove(end)

        # Uncomment for undirected graph (but be aware that methods like topological_sort will not work)
        # if start in self.adjacency_list[end]:
        #     self.adjacency_list[end].remove(start)

    def add_vertex(self) -> None:
        """Add a new vertex. O(1) time."""
        if self.free_ids:
            new_id = self.free_ids.pop()
        else:
            new_id = self.next_id
            self.next_id += 1
        self.adjacency_list[new_id] = []
        self.num_vertices += 1

    def remove_vertex(self, vertex: int) -> None:
        """Remove a vertex and all its edges. O(V + E) time."""
        if vertex not in self.adjacency_list:
            raise ValueError("Vertex does not exist")

        del self.adjacency_list[vertex]
        self.free_ids.append(vertex)
        self.num_vertices -= 1

        for key in self.adjacency_list:
            if vertex in self.adjacency_list[key]:
                self.adjacency_list[key].remove(vertex)

    # # Recursive DFS approach
    # def topological_sort_dfs_rec(self) -> list[int]:
    #     """Return topological ordering using recursive DFS. O(V + E) time."""
    #     visited = set()
    #     rec_stack = set()  # Only needed if we want to detect cycles
    #     stack = []

    #     def dfs(vertex):
    #         # Only needed if we want to detect cycles
    #         if vertex in rec_stack:
    #             raise ValueError("Graph has a cycle")

    #         visited.add(vertex)
    #         rec_stack.add(vertex)   # Only needed if we want to detect cycles
    #         for neighbor in self.adjacency_list[vertex]:
    #             if neighbor not in visited:
    #                 dfs(neighbor)
    #         rec_stack.remove(vertex)    # Only needed if we want to detect cycles
    #         stack.append(vertex)

    #     for vertex in self.adjacency_list:
    #         if vertex not in visited:
    #             dfs(vertex)

    #     return stack[::-1]

    # Iterative BFS approach -> Kahn's Algorithm
    def topological_sort_bfs_it(self) -> list[int]:
        """Return topological ordering using Kahn's algorithm. O(V + E) time."""
        in_degree = {vertex: 0 for vertex in self.adjacency_list}

        # Calculate in-degree of each vertex
        for vertex in self.adjacency_list:
            for neighbor in self.adjacency_list[vertex]:
                in_degree[neighbor] += 1

        # Initialize queue with vertices having in-degree 0
        queue = deque([vertex for vertex in in_degree if in_degree[vertex] == 0])
        stack = []

        while queue:
            vertex = queue.popleft()
            stack.append(vertex)

            # Update in-degree of neighbors
            for neighbor in self.adjacency_list[vertex]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        if len(stack) != self.num_vertices:
            raise ValueError("Graph has a cycle")

        return stack

    # # Recursive DFS approach
    # def get_paths_dfs_rec(self, start: int, end: int, path: Optional[list[int]] = None) -> list[list[int]]:
    #     """Find all paths from start to end via recursive DFS. O(V! * V) worst case."""
    #     if start not in self.adjacency_list or end not in self.adjacency_list:
    #         return []

    #     if path is None:
    #         path = []

    #     path = path + [start]

    #     if start == end:
    #         return [path]

    #     paths = []
    #     for vertex in self.adjacency_list[start]:
    #         if vertex not in path:
    #             new_paths = self.get_paths_dfs_rec(vertex, end, path)
    #             for p in new_paths:
    #                 paths.append(p)

    #     return paths

    # Iterative BFS approach
    def get_paths_bfs_it(self, start: int, end: int) -> list[list[int]]:
        """Find all paths from start to end via BFS. O(V! * V) worst case."""
        if start not in self.adjacency_list or end not in self.adjacency_list:
            return []

        paths = []
        queue = deque([(start, [start])])  # (current_vertex, current_path)

        while queue:
            vertex, path = queue.popleft()

            if vertex == end:
                paths.append(path)
            else:
                for neighbor in self.adjacency_list[vertex]:
                    if neighbor not in path:
                        queue.append((neighbor, path + [neighbor]))

        return paths

    # # Recursive DFS approach
    # def get_shortest_path_dfs_rec(self, start: int, end: int, path: Optional[list[int]] = None) -> list[int]:
    #     """Find shortest path via recursive DFS. O(V! * V) worst case."""
    #     if start not in self.adjacency_list or end not in self.adjacency_list:
    #         return []

    #     if path is None:
    #         path = []

    #     path = path + [start]

    #     if start == end:
    #         return path

    #     shortest_path = None
    #     for vertex in self.adjacency_list[start]:
    #         if vertex not in path:
    #             sp = self.get_shortest_path_dfs_rec(vertex, end, path)
    #             if sp and (shortest_path is None or len(sp) < len(shortest_path)):
    #                     shortest_path = sp

    #     return shortest_path if shortest_path else []

    # Iterative BFS approach
    def get_shortest_path_bfs_it(self, start: int, end: int) -> list[int]:
        """Find shortest path via iterative BFS. O(V + E) worst case."""
        if start not in self.adjacency_list or end not in self.adjacency_list:
            return []

        queue = deque([(start, [start])])
        visited = set()
        visited.add(start)

        while queue:
            vertex, path = queue.popleft()

            if vertex == end:
                return path

            for neighbor in self.adjacency_list[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))

        return []

    # # Recursive DFS approach
    # def is_connected_dfs_rec(self, start: int, end: int, visited: Optional[set[int]] = None) -> bool:
    #     """Check if a path exists via recursive DFS. O(V + E) time."""
    #     if start not in self.adjacency_list or end not in self.adjacency_list:
    #         return False

    #     if visited is None:
    #         visited = set()

    #     if start == end:
    #         return True

    #     visited.add(start)

    #     for neighbor in self.adjacency_list[start]:
    #         if neighbor not in visited and self.is_connected_dfs_rec(neighbor, end, visited):
    #             return True

    #     return False

    # Iterative DFS approach (preferred)
    def is_connected_dfs_it(self, start: int, end: int) -> bool:
        """Check if a path exists from start to end via DFS. O(V + E) time."""
        if start not in self.adjacency_list or end not in self.adjacency_list:
            return False

        visited = set()
        visited.add(start)
        stack = deque([start])

        while stack:
            vertex = stack.pop()

            if vertex == end:
                return True

            for neighbor in self.adjacency_list[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)

        return False

    # # Recursive BFS approach
    # Is skipped because it would be very complex to code
    # As iterative BFS is also more efficient, the recursive BFS is strongly not recommended

    # # Iterative BFS approach
    # def is_connected_bfs_it(self, start: int, end: int) -> bool:
    #     """Check if a path exists via iterative BFS. O(V + E) time."""
    #     if start not in self.adjacency_list or end not in self.adjacency_list:
    #         return False

    #     visited = set()
    #     visited.add(start)
    #     queue = deque([start])

    #     while queue:
    #         vertex = queue.popleft()

    #         if vertex == end:
    #             return True

    #         for neighbor in self.adjacency_list[vertex]:
    #             if neighbor not in visited:
    #                 visited.add(neighbor)
    #                 queue.append(neighbor)

    #     return False


# Option 2: Using adjacency matrix
class Graph_AdjacencyMatrix:
    def __init__(self, num_vertices: int) -> None:
        self.num_vertices = num_vertices

        # Initialize adjacency matrix
        # `self.adjacency_matrix[i][j]`: Stores weight of edge from node `i` to node `j`
        # No Edge: Use `float('inf')`, `-1`, or `0` (select based on your use case)
        self.adjacency_matrix = [[0] * num_vertices for _ in range(num_vertices)]

        # Print the graph
        self.display()

    def display(self) -> None:
        """Print the adjacency matrix. O(V^2) time."""
        for row in self.adjacency_matrix:
            print(row)

    def add_edge(self, start: int, end: int) -> None:
        """Add a directed edge. O(1) time."""
        if (
            start >= self.num_vertices
            or end >= self.num_vertices
            or start < 0
            or end < 0
        ):
            raise ValueError("Vertices are out of bounds")

        self.adjacency_matrix[start][end] = 1

        # Uncomment for undirected graph (but be aware that methods like topological_sort will not work)
        # self.adjacency_matrix[end][start] = 1

    def remove_edge(self, start: int, end: int) -> None:
        """Remove a directed edge. O(1) time."""
        if (
            start >= self.num_vertices
            or end >= self.num_vertices
            or start < 0
            or end < 0
        ):
            raise ValueError("Vertices are out of bounds")

        self.adjacency_matrix[start][end] = 0

        # Uncomment for undirected graph (but be aware that methods like topological_sort will not work)
        # self.adjacency_matrix[end][start] = 0

    def add_vertex(self) -> None:
        """Add a new vertex. O(V) time (extends each row)."""
        self.num_vertices += 1

        for row in self.adjacency_matrix:
            row.append(0)
        self.adjacency_matrix.append([0] * self.num_vertices)

    def remove_vertex(self, vertex: int) -> None:
        """Remove a vertex and all its edges. O(V^2) time."""
        # Note: shifts indices of all vertices > vertex, invalidating external references
        if vertex >= self.num_vertices or vertex < 0:
            raise ValueError("Vertex does not exist")

        for row in self.adjacency_matrix:
            row.pop(vertex)
        self.adjacency_matrix.pop(vertex)

        self.num_vertices -= 1

    # # Recursive DFS approach
    # def topological_sort_dfs_rec(self) -> list[int]:
    #     """Return topological ordering using recursive DFS. O(V^2) time."""
    #     visited = set()
    #     rec_stack = set()  # Only needed if we want to detect cycles
    #     stack = []

    #     def dfs(vertex):
    #         # Only needed if we want to detect cycles
    #         if vertex in rec_stack:
    #             raise ValueError("Graph has a cycle")

    #         visited.add(vertex)
    #         rec_stack.add(vertex)   # Only needed if we want to detect cycles
    #         for neighbor in range(self.num_vertices):
    #             if self.adjacency_matrix[vertex][neighbor] == 1 and neighbor not in visited:
    #                 dfs(neighbor)
    #         rec_stack.remove(vertex)    # Only needed if we want to detect cycles
    #         stack.append(vertex)

    #     for vertex in range(self.num_vertices):
    #         if vertex not in visited:
    #             dfs(vertex)

    #     return stack[::-1]

    # Iterative BFS approach -> Kahn's Algorithm
    def topological_sort_bfs_it(self) -> list[int]:
        """Return topological ordering using Kahn's algorithm. O(V^2) time."""
        in_degree = {i: 0 for i in range(self.num_vertices)}

        # Calculate in-degree of each vertex
        for vertex in range(self.num_vertices):
            for neighbor in range(self.num_vertices):
                if self.adjacency_matrix[vertex][neighbor] == 1:
                    in_degree[neighbor] += 1

        # Initialize queue with vertices having in-degree 0
        queue = deque([vertex for vertex in in_degree if in_degree[vertex] == 0])
        stack = []

        while queue:
            vertex = queue.popleft()
            stack.append(vertex)

            # Update in-degree of neighbors
            for neighbor in range(self.num_vertices):
                if self.adjacency_matrix[vertex][neighbor] == 1:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        queue.append(neighbor)

        if len(stack) != self.num_vertices:
            raise ValueError("Graph has a cycle")

        return stack

    # # Recursive DFS approach
    # def get_paths_dfs_rec(self, start: int, end: int, path: Optional[list[int]] = None) -> list[list[int]]:
    #     """Find all paths from start to end via recursive DFS. O(V! * V) worst case."""
    #     if (
    #         start >= self.num_vertices
    #         or end >= self.num_vertices
    #         or start < 0
    #         or end < 0
    #     ):
    #         return []

    #     if path is None:
    #         path = []

    #     path = path + [start]

    #     if start == end:
    #         return [path]

    #     paths = []
    #     for vertex in range(self.num_vertices):
    #         if self.adjacency_matrix[start][vertex] == 1 and vertex not in path:
    #             new_paths = self.get_paths_dfs_rec(vertex, end, path)
    #             for p in new_paths:
    #                 paths.append(p)

    #     return paths

    # Iterative BFS approach
    def get_paths_bfs_it(self, start: int, end: int) -> list[list[int]]:
        """Find all paths from start to end via BFS. O(V! * V) worst case."""
        if (
            start >= self.num_vertices
            or end >= self.num_vertices
            or start < 0
            or end < 0
        ):
            return []

        paths = []
        queue = deque([(start, [start])])  # (current_vertex, current_path)

        while queue:
            vertex, path = queue.popleft()

            if vertex == end:
                paths.append(path)
            else:
                for neighbor in range(self.num_vertices):
                    if (
                        self.adjacency_matrix[vertex][neighbor] == 1
                        and neighbor not in path
                    ):
                        queue.append((neighbor, path + [neighbor]))

        return paths

    # # Recursive DFS approach
    # def get_shortest_path_dfs_rec(self, start: int, end: int, path: Optional[list[int]] = None) -> list[int]:
    #     """Find shortest path via recursive DFS. O(V! * V) worst case."""
    #     if (
    #         start >= self.num_vertices
    #         or end >= self.num_vertices
    #         or start < 0
    #         or end < 0
    #     ):
    #         return []

    #     if path is None:
    #         path = []

    #     path = path + [start]

    #     if start == end:
    #         return path

    #     shortest_path = None
    #     for vertex in range(self.num_vertices):
    #         if self.adjacency_matrix[start][vertex] == 1 and vertex not in path:
    #             sp = self.get_shortest_path_dfs_rec(vertex, end, path)
    #             if sp and (shortest_path is None or len(sp) < len(shortest_path)):
    #                     shortest_path = sp

    #     return shortest_path if shortest_path else []

    # Iterative BFS approach
    def get_shortest_path_bfs_it(self, start: int, end: int) -> list[int]:
        """Find shortest path via iterative BFS. O(V^2) worst case."""
        if (
            start >= self.num_vertices
            or end >= self.num_vertices
            or start < 0
            or end < 0
        ):
            return []

        queue = deque([(start, [start])])
        visited = set()
        visited.add(start)

        while queue:
            vertex, path = queue.popleft()

            if vertex == end:
                return path

            for neighbor in range(self.num_vertices):
                if (
                    self.adjacency_matrix[vertex][neighbor] == 1
                    and neighbor not in visited
                ):
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))

        return []

    # # Recursive DFS approach
    # def is_connected_dfs_rec(self, start: int, end: int, visited: Optional[set[int]] = None) -> bool:
    #     """Check if a path exists via recursive DFS. O(V^2) time."""
    #     if (
    #         start >= self.num_vertices
    #         or end >= self.num_vertices
    #         or start < 0
    #         or end < 0
    #     ):
    #         return False

    #     if visited is None:
    #         visited = set()

    #     if start == end:
    #         return True

    #     visited.add(start)

    #     for neighbor in range(self.num_vertices):
    #         if self.adjacency_matrix[start][neighbor] == 1 and neighbor not in visited:
    #             if self.is_connected_dfs_rec(neighbor, end, visited):
    #                 return True

    #     return False

    # Iterative DFS approach (preferred)
    def is_connected_dfs_it(self, start: int, end: int) -> bool:
        """Check if a path exists from start to end via DFS. O(V^2) time."""
        if (
            start >= self.num_vertices
            or end >= self.num_vertices
            or start < 0
            or end < 0
        ):
            return False

        visited = set()
        visited.add(start)
        stack = [
            start
        ]  # list: O(1) amortized; deque: O(1) worst-case but slower in practice

        while stack:
            vertex = stack.pop()

            if vertex == end:
                return True

            for neighbor in range(self.num_vertices):
                if (
                    self.adjacency_matrix[vertex][neighbor] == 1
                    and neighbor not in visited
                ):
                    visited.add(neighbor)
                    stack.append(neighbor)

        return False

    # # Recursive BFS approach
    # Is skipped because it would be very complex to code
    # As iterative BFS is also more efficient, the recursive BFS is strongly not recommended

    # # Iterative BFS approach
    # def is_connected_bfs_it(self, start: int, end: int) -> bool:
    #     """Check if a path exists via iterative BFS. O(V^2) time."""
    #     if (
    #         start >= self.num_vertices
    #         or end >= self.num_vertices
    #         or start < 0
    #         or end < 0
    #     ):
    #         return False

    #     visited = set()
    #     visited.add(start)
    #     queue = deque([start])

    #     while queue:
    #         vertex = queue.popleft()

    #         if vertex == end:
    #             return True

    #         for neighbor in range(self.num_vertices):
    #             if self.adjacency_matrix[vertex][neighbor] == 1 and neighbor not in visited:
    #                 visited.add(neighbor)
    #                 queue.append(neighbor)

    #     return False


if __name__ == "__main__":
    # Test Adjacency List implementation
    graph_1 = Graph_AdjacencyList(5)
    graph_1.add_edge(0, 1)
    graph_1.add_edge(1, 2)
    graph_1.add_edge(2, 3)
    graph_1.add_edge(3, 4)

    # Test get_paths_bfs_it
    assert graph_1.get_paths_bfs_it(0, 4) == [[0, 1, 2, 3, 4]], "Should find path 0->4"
    assert graph_1.get_paths_bfs_it(0, 2) == [[0, 1, 2]], "Should find path 0->2"
    assert graph_1.get_paths_bfs_it(4, 0) == [], "No path from 4 to 0 (directed)"

    # Test get_shortest_path_bfs_it
    assert graph_1.get_shortest_path_bfs_it(0, 4) == [0, 1, 2, 3, 4], (
        "Shortest path 0->4"
    )
    assert graph_1.get_shortest_path_bfs_it(0, 2) == [0, 1, 2], "Shortest path 0->2"

    # Test is_connected_dfs_it
    assert graph_1.is_connected_dfs_it(0, 4), "0 should be connected to 4"
    assert not graph_1.is_connected_dfs_it(4, 0), "4 should not reach 0 (directed)"

    # Test topological_sort_bfs_it
    topo = graph_1.topological_sort_bfs_it()
    assert topo == [0, 1, 2, 3, 4], "Topological order should be 0,1,2,3,4"

    # Test error handling
    try:
        graph_1.add_edge(0, 10)
        assert False, "Should raise ValueError for out of bounds"
    except ValueError:
        pass

    # Test Adjacency Matrix implementation
    graph_2 = Graph_AdjacencyMatrix(5)
    graph_2.add_edge(0, 1)
    graph_2.add_edge(1, 2)
    graph_2.add_edge(2, 3)
    graph_2.add_edge(3, 4)

    # Test get_paths_bfs_it
    assert graph_2.get_paths_bfs_it(0, 4) == [[0, 1, 2, 3, 4]], "Should find path 0->4"
    assert graph_2.get_paths_bfs_it(0, 2) == [[0, 1, 2]], "Should find path 0->2"

    # Test get_shortest_path_bfs_it
    assert graph_2.get_shortest_path_bfs_it(0, 4) == [0, 1, 2, 3, 4], (
        "Shortest path 0->4"
    )
    assert graph_2.get_shortest_path_bfs_it(0, 2) == [0, 1, 2], "Shortest path 0->2"

    # Test is_connected_dfs_it
    assert graph_2.is_connected_dfs_it(0, 4), "0 should be connected to 4"
    assert not graph_2.is_connected_dfs_it(4, 0), "4 should not reach 0 (directed)"

    # Test topological_sort_bfs_it
    topo2 = graph_2.topological_sort_bfs_it()
    assert topo2 == [0, 1, 2, 3, 4], "Topological order should be 0,1,2,3,4"

    print("All tests passed!")
