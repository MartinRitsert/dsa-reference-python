from __future__ import annotations

from collections import deque


# Option 1: Using adjacency list
class GraphAdjacencyList:
    def __init__(self, num_vertices: int) -> None:
        self.num_vertices = num_vertices
        self.next_id = num_vertices  # Tracks the highest ID ever issued
        self.free_ids = []

        # Initialize adjacency list (list over set to preserve insertion order for deterministic traversal)
        # Consider `defaultdict(list)` if node labels are arbitrary
        self.adjacency_list = {i: [] for i in range(num_vertices)}

    def display(self) -> None:
        """Print the adjacency list. O(V + E) time, O(1) space."""
        for vertex in self.adjacency_list:
            print(vertex, ":", self.adjacency_list[vertex])

    def add_edge(self, start: int, end: int) -> None:
        """Add a directed edge. O(V) time, O(1) space."""
        if start not in self.adjacency_list or end not in self.adjacency_list:
            raise ValueError("Vertices are out of bounds")

        if end not in self.adjacency_list[start]:
            self.adjacency_list[start].append(end)

        # Uncomment for undirected graph (but be aware that methods like topological_sort will not work)
        # if start not in self.adjacency_list[end]:
        #     self.adjacency_list[end].append(start)

    def remove_edge(self, start: int, end: int) -> None:
        """Remove a directed edge. O(V) time, O(1) space."""
        if start not in self.adjacency_list or end not in self.adjacency_list:
            raise ValueError("Vertices are out of bounds")

        if end in self.adjacency_list[start]:
            self.adjacency_list[start].remove(end)

        # Uncomment for undirected graph (but be aware that methods like topological_sort will not work)
        # if start in self.adjacency_list[end]:
        #     self.adjacency_list[end].remove(start)

    def add_vertex(self) -> None:
        """Add a new vertex. O(1) time, O(1) space."""
        if self.free_ids:
            new_id = self.free_ids.pop()
        else:
            new_id = self.next_id
            self.next_id += 1
        self.adjacency_list[new_id] = []
        self.num_vertices += 1

    def remove_vertex(self, vertex: int) -> None:
        """Remove a vertex and all its edges. O(V + E) time, O(1) space."""
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
    #     """Return topological ordering using recursive DFS. O(V + E) time, O(V) space."""
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
        """Return topological ordering using Kahn's algorithm. O(V + E) time, O(V) space."""
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
    # def get_paths_dfs_rec(self, start: int, end: int) -> list[list[int]]:
    #     """Find all paths from start to end via recursive DFS. O(V! * V^2) time, O(V! * V) space."""
    #     if start not in self.adjacency_list or end not in self.adjacency_list:
    #         return []
    #
    #     paths = []
    #
    #     def dfs(vertex, path):
    #         path = path + [vertex]
    #         if vertex == end:
    #             paths.append(path)
    #             return
    #         for neighbor in self.adjacency_list[vertex]:
    #             if neighbor not in path:
    #                 dfs(neighbor, path)
    #
    #     dfs(start, [])
    #     return paths

    # Iterative BFS approach
    def get_paths_bfs_it(self, start: int, end: int) -> list[list[int]]:
        """Find all paths from start to end via BFS. O(V! * V^2) time, O(V! * V) space."""
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
    # def get_shortest_path_dfs_rec(self, start: int, end: int) -> list[int]:
    #     """Find shortest path via recursive DFS. O(V! * V^2) time, O(V^2) space."""
    #     if start not in self.adjacency_list or end not in self.adjacency_list:
    #         return []
    #
    #     def dfs(vertex, path):
    #         path = path + [vertex]
    #         if vertex == end:
    #             return path
    #         shortest_path = None
    #         for neighbor in self.adjacency_list[vertex]:
    #             if neighbor not in path:
    #                 sp = dfs(neighbor, path)
    #                 if sp and (shortest_path is None or len(sp) < len(shortest_path)):
    #                     shortest_path = sp
    #         return shortest_path
    #
    #     return dfs(start, []) or []

    # # Recursive DFS approach with backtracking and pruning
    # # Improves on the above by using in-place path mutation (append/pop) instead
    # # of list copies, reducing space from O(V^2) to O(V), and by pruning branches
    # # that cannot yield a shorter path than the current best.
    # # Note: a parallel visited set would reduce `not in path` from O(V) to O(1),
    # # bringing time from O(V! * V^2) to O(V! * V) without affecting space.
    # def get_shortest_path_dfs_rec(self, start: int, end: int) -> list[int]:
    #     """Find shortest path via recursive DFS with backtracking/pruning. O(V! * V^2) time, O(V) space."""
    #     if start not in self.adjacency_list or end not in self.adjacency_list:
    #         return []
    #
    #     shortest_path = []
    #     path = []
    #
    #     def dfs(vertex):
    #         nonlocal shortest_path
    #         if vertex == end:
    #             if not shortest_path or len(path) < len(shortest_path):
    #                 shortest_path = path[:]
    #             return
    #         for neighbor in self.adjacency_list[vertex]:
    #             if neighbor not in path:
    #                 if shortest_path and len(path) + 1 >= len(shortest_path):
    #                     continue
    #                 path.append(neighbor)
    #                 dfs(neighbor)
    #                 path.pop()
    #
    #     path.append(start)
    #     dfs(start)
    #     return shortest_path

    # Iterative BFS approach
    def get_shortest_path_bfs_it(self, start: int, end: int) -> list[int]:
        """Find shortest path via iterative BFS. O(V + E) time, O(V) space."""
        if start not in self.adjacency_list or end not in self.adjacency_list:
            return []

        queue = deque([start])
        visited = set()
        visited.add(start)
        parent = {start: None}

        while queue:
            vertex = queue.popleft()

            if vertex == end:
                path = []
                curr = end
                while curr is not None:
                    path.append(curr)
                    curr = parent[curr]
                return path[::-1]

            for neighbor in self.adjacency_list[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    parent[neighbor] = vertex
                    queue.append(neighbor)

        return []

    # # Recursive DFS approach
    # def is_connected_dfs_rec(self, start: int, end: int) -> bool:
    #     """Check if a path exists via recursive DFS. O(V + E) time, O(V) space."""
    #     if start not in self.adjacency_list or end not in self.adjacency_list:
    #         return False
    #
    #     visited = set()
    #
    #     def dfs(vertex):
    #         if vertex == end:
    #             return True
    #         visited.add(vertex)
    #         for neighbor in self.adjacency_list[vertex]:
    #             if neighbor not in visited and dfs(neighbor):
    #                 return True
    #         return False
    #
    #     return dfs(start)

    # Iterative DFS approach (preferred)
    def is_connected_dfs_it(self, start: int, end: int) -> bool:
        """Check if a path exists from start to end via DFS. O(V + E) time, O(V) space."""
        if start not in self.adjacency_list or end not in self.adjacency_list:
            return False

        visited = set()
        visited.add(start)
        stack = [start]

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
    #     """Check if a path exists via iterative BFS. O(V + E) time, O(V) space."""
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
class GraphAdjacencyMatrix:
    def __init__(self, num_vertices: int) -> None:
        self.num_vertices = num_vertices
        self.matrix_size = num_vertices  # Physical size of matrix
        self.deleted_vertices = set()  # Track deleted vertices

        # Initialize adjacency matrix
        self.adjacency_matrix: list[list[int | None]] = [
            [0] * num_vertices for _ in range(num_vertices)
        ]

    def _vertex_exists(self, vertex: int) -> bool:
        """Check if vertex exists and is not deleted. O(1) time, O(1) space."""
        return 0 <= vertex < self.matrix_size and vertex not in self.deleted_vertices

    def display(self) -> None:
        """Print the adjacency matrix. O(V^2) time, O(1) space."""
        for row in self.adjacency_matrix:
            print(row)

    def add_edge(self, start: int, end: int) -> None:
        """Add a directed edge. O(1) time, O(1) space."""
        if not self._vertex_exists(start) or not self._vertex_exists(end):
            raise ValueError("Vertex does not exist")

        self.adjacency_matrix[start][end] = 1

        # Uncomment for undirected graph (but be aware that methods like topological_sort will not work)
        # self.adjacency_matrix[end][start] = 1

    def remove_edge(self, start: int, end: int) -> None:
        """Remove a directed edge. O(1) time, O(1) space."""
        if not self._vertex_exists(start) or not self._vertex_exists(end):
            raise ValueError("Vertex does not exist")

        self.adjacency_matrix[start][end] = 0

        # Uncomment for undirected graph (but be aware that methods like topological_sort will not work)
        # self.adjacency_matrix[end][start] = 0

    def add_vertex(self) -> None:
        """Add a new vertex. O(V) time, O(V) space."""
        if self.deleted_vertices:
            # Reuse a deleted vertex ID
            reused_id = self.deleted_vertices.pop()
            for i in range(self.matrix_size):
                self.adjacency_matrix[reused_id][i] = 0
                self.adjacency_matrix[i][reused_id] = 0
        else:
            # Expand matrix
            self.matrix_size += 1
            for row in self.adjacency_matrix:
                row.append(0)
            self.adjacency_matrix.append([0] * self.matrix_size)
        self.num_vertices += 1

    def remove_vertex(self, vertex: int) -> None:
        """Remove a vertex and all its edges. O(V) time, O(1) space."""
        if not self._vertex_exists(vertex):
            raise ValueError("Vertex does not exist")

        # Mark row and column as deleted with None
        for i in range(self.matrix_size):
            self.adjacency_matrix[vertex][i] = None
            self.adjacency_matrix[i][vertex] = None

        self.deleted_vertices.add(vertex)
        self.num_vertices -= 1

    # # Recursive DFS approach
    # def topological_sort_dfs_rec(self) -> list[int]:
    #     """Return topological ordering using recursive DFS. O(V^2) time, O(V) space."""
    #     visited = set()
    #     rec_stack = set()  # Only needed if we want to detect cycles
    #     stack = []

    #     def dfs(vertex):
    #         # Only needed if we want to detect cycles
    #         if vertex in rec_stack:
    #             raise ValueError("Graph has a cycle")

    #         visited.add(vertex)
    #         rec_stack.add(vertex)   # Only needed if we want to detect cycles
    #         for neighbor in range(self.matrix_size):
    #             if neighbor in self.deleted_vertices:
    #                 continue
    #             if self.adjacency_matrix[vertex][neighbor] == 1 and neighbor not in visited:
    #                 dfs(neighbor)
    #         rec_stack.remove(vertex)    # Only needed if we want to detect cycles
    #         stack.append(vertex)

    #     for vertex in range(self.matrix_size):
    #         if vertex in self.deleted_vertices:
    #             continue
    #         if vertex not in visited:
    #             dfs(vertex)

    #     return stack[::-1]

    # Iterative BFS approach -> Kahn's Algorithm
    def topological_sort_bfs_it(self) -> list[int]:
        """Return topological ordering using Kahn's algorithm. O(V^2) time, O(V) space."""
        in_degree = {
            vertex: 0
            for vertex in range(self.matrix_size)
            if vertex not in self.deleted_vertices
        }

        # Calculate in-degree of each vertex
        for vertex in in_degree:
            for neighbor in in_degree:
                if self.adjacency_matrix[vertex][neighbor] == 1:
                    in_degree[neighbor] += 1

        # Initialize queue with vertices having in-degree 0
        queue = deque([vertex for vertex in in_degree if in_degree[vertex] == 0])
        stack = []

        while queue:
            vertex = queue.popleft()
            stack.append(vertex)

            # Update in-degree of neighbors
            for neighbor in in_degree:
                if self.adjacency_matrix[vertex][neighbor] == 1:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        queue.append(neighbor)

        if len(stack) != self.num_vertices:
            raise ValueError("Graph has a cycle")

        return stack

    # # Recursive DFS approach
    # def get_paths_dfs_rec(self, start: int, end: int) -> list[list[int]]:
    #     """Find all paths from start to end via recursive DFS. O(V! * V^2) time, O(V! * V) space."""
    #     if not self._vertex_exists(start) or not self._vertex_exists(end):
    #         return []
    #
    #     paths = []
    #
    #     def dfs(vertex, path):
    #         path = path + [vertex]
    #         if vertex == end:
    #             paths.append(path)
    #             return
    #         for neighbor in range(self.matrix_size):
    #             if neighbor in self.deleted_vertices:
    #                 continue
    #             if self.adjacency_matrix[vertex][neighbor] == 1 and neighbor not in path:
    #                 dfs(neighbor, path)
    #
    #     dfs(start, [])
    #     return paths

    # Iterative BFS approach
    def get_paths_bfs_it(self, start: int, end: int) -> list[list[int]]:
        """Find all paths from start to end via BFS. O(V! * V^2) time, O(V! * V) space."""
        if not self._vertex_exists(start) or not self._vertex_exists(end):
            return []

        paths = []
        queue = deque([(start, [start])])  # (current_vertex, current_path)

        while queue:
            vertex, path = queue.popleft()

            if vertex == end:
                paths.append(path)
            else:
                for neighbor in range(self.matrix_size):
                    if neighbor in self.deleted_vertices:
                        continue
                    if (
                        self.adjacency_matrix[vertex][neighbor] == 1
                        and neighbor not in path
                    ):
                        queue.append((neighbor, path + [neighbor]))

        return paths

    # # Recursive DFS approach
    # def get_shortest_path_dfs_rec(self, start: int, end: int) -> list[int]:
    #     """Find shortest path via recursive DFS. O(V! * V^2) time, O(V^2) space."""
    #     if not self._vertex_exists(start) or not self._vertex_exists(end):
    #         return []
    #
    #     def dfs(vertex, path):
    #         path = path + [vertex]
    #         if vertex == end:
    #             return path
    #         shortest_path = None
    #         for neighbor in range(self.matrix_size):
    #             if neighbor in self.deleted_vertices:
    #                 continue
    #             if self.adjacency_matrix[vertex][neighbor] == 1 and neighbor not in path:
    #                 sp = dfs(neighbor, path)
    #                 if sp and (shortest_path is None or len(sp) < len(shortest_path)):
    #                     shortest_path = sp
    #         return shortest_path
    #
    #     return dfs(start, []) or []

    # # Recursive DFS approach with backtracking and pruning
    # # Improves on the above by using in-place path mutation (append/pop) instead
    # # of list copies, reducing space from O(V^2) to O(V), and by pruning branches
    # # that cannot yield a shorter path than the current best.
    # # Note: a parallel visited set would reduce `not in path` from O(V) to O(1),
    # # bringing time from O(V! * V^2) to O(V! * V) without affecting space.
    # def get_shortest_path_dfs_rec(self, start: int, end: int) -> list[int]:
    #     """Find shortest path via recursive DFS with backtracking/pruning. O(V! * V^2) time, O(V) space."""
    #     if not self._vertex_exists(start) or not self._vertex_exists(end):
    #         return []
    #
    #     shortest_path = []
    #     path = []
    #
    #     def dfs(vertex):
    #         nonlocal shortest_path
    #         if vertex == end:
    #             if not shortest_path or len(path) < len(shortest_path):
    #                 shortest_path = path[:]
    #             return
    #         for neighbor in range(self.matrix_size):
    #             if neighbor in self.deleted_vertices:
    #                 continue
    #             if self.adjacency_matrix[vertex][neighbor] == 1 and neighbor not in path:
    #                 if shortest_path and len(path) + 1 >= len(shortest_path):
    #                     continue
    #                 path.append(neighbor)
    #                 dfs(neighbor)
    #                 path.pop()
    #
    #     path.append(start)
    #     dfs(start)
    #     return shortest_path

    # Iterative BFS approach
    def get_shortest_path_bfs_it(self, start: int, end: int) -> list[int]:
        """Find shortest path via iterative BFS. O(V^2) time, O(V) space."""
        if not self._vertex_exists(start) or not self._vertex_exists(end):
            return []

        queue = deque([start])
        visited = set()
        visited.add(start)
        parent = {start: None}

        while queue:
            vertex = queue.popleft()

            if vertex == end:
                path = []
                curr = end
                while curr is not None:
                    path.append(curr)
                    curr = parent[curr]
                return path[::-1]

            for neighbor in range(self.matrix_size):
                if neighbor in self.deleted_vertices:
                    continue
                if (
                    self.adjacency_matrix[vertex][neighbor] == 1
                    and neighbor not in visited
                ):
                    visited.add(neighbor)
                    parent[neighbor] = vertex
                    queue.append(neighbor)

        return []

    # # Recursive DFS approach
    # def is_connected_dfs_rec(self, start: int, end: int) -> bool:
    #     """Check if a path exists via recursive DFS. O(V^2) time, O(V) space."""
    #     if not self._vertex_exists(start) or not self._vertex_exists(end):
    #         return False
    #
    #     visited = set()
    #
    #     def dfs(vertex):
    #         if vertex == end:
    #             return True
    #         visited.add(vertex)
    #         for neighbor in range(self.matrix_size):
    #             if neighbor in self.deleted_vertices:
    #                 continue
    #             if (
    #                 self.adjacency_matrix[vertex][neighbor] == 1
    #                 and neighbor not in visited
    #                 and dfs(neighbor)
    #             ):
    #                 return True
    #         return False
    #
    #     return dfs(start)

    # Iterative DFS approach (preferred)
    def is_connected_dfs_it(self, start: int, end: int) -> bool:
        """Check if a path exists from start to end via DFS. O(V^2) time, O(V) space."""
        if not self._vertex_exists(start) or not self._vertex_exists(end):
            return False

        visited = set()
        visited.add(start)
        stack = [start]

        while stack:
            vertex = stack.pop()

            if vertex == end:
                return True

            for neighbor in range(self.matrix_size):
                if neighbor in self.deleted_vertices:
                    continue
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
    #     """Check if a path exists via iterative BFS. O(V^2) time, O(V) space."""
    #     if not self._vertex_exists(start) or not self._vertex_exists(end):
    #         return False

    #     visited = set()
    #     visited.add(start)
    #     queue = deque([start])

    #     while queue:
    #         vertex = queue.popleft()

    #         if vertex == end:
    #             return True

    #         for neighbor in range(self.matrix_size):
    #             if neighbor in self.deleted_vertices:
    #                 continue
    #             if (
    #                 self.adjacency_matrix[vertex][neighbor] == 1
    #                 and neighbor not in visited
    #             ):
    #                 visited.add(neighbor)
    #                 queue.append(neighbor)

    #     return False


if __name__ == "__main__":
    # Test Adjacency List implementation
    graph_1 = GraphAdjacencyList(5)
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
    graph_2 = GraphAdjacencyMatrix(5)
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

    # Test vertex index stability after removal
    graph_3 = GraphAdjacencyMatrix(5)
    graph_3.add_edge(4, 3)  # Edge from vertex 4 to vertex 3
    graph_3.remove_vertex(2)  # Remove vertex 2

    # Verify vertex 4 still has edge to vertex 3 (indices preserved)
    assert graph_3.adjacency_matrix[4][3] == 1, (
        "Vertex 4 should still have edge to vertex 3 after removing vertex 2"
    )
    assert graph_3.num_vertices == 4, "Should have 4 vertices after removal"
    assert 2 in graph_3.deleted_vertices, "Vertex 2 should be in deleted set"

    # Verify deleted vertex cannot be used
    try:
        graph_3.add_edge(2, 0)
        assert False, "Should raise ValueError for deleted vertex"
    except ValueError:
        pass

    # Test vertex reuse
    graph_3.add_vertex()  # Should reuse ID 2
    assert 2 not in graph_3.deleted_vertices, "Vertex 2 should be reused"
    assert graph_3.num_vertices == 5, "Should have 5 vertices after adding one back"
    # Verify vertex 2 can now be used
    graph_3.add_edge(2, 0)  # Should work now

    print("All tests passed!")
