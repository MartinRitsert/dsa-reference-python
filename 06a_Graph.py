from collections import deque


# Option 1: Using adjacency list
class Graph_AdjacencyList:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.free_ids = []
        
        # Initialize adjacency list
        self.adjacency_list = {i: [] for i in range(num_vertices)}
        
        # Print the graph
        self.display()

    def display(self):
        for vertex in self.adjacency_list:
            print(vertex, ":", self.adjacency_list[vertex])
    
    def add_edge(self, start, end):
        if start not in self.adjacency_list or end not in self.adjacency_list:
            raise ValueError("Vertices are out of bounds")

        if end not in self.adjacency_list[start]:
            self.adjacency_list[start].append(end)

        # Uncomment for undirected graph (but be aware that methods like topological_sort will not work)
        # if start not in self.adjacency_list[end]:
        #     self.adjacency_list[end].append(start)

    def remove_edge(self, start, end):
        if start not in self.adjacency_list or end not in self.adjacency_list:
            raise ValueError("Vertices are out of bounds")
        
        if end in self.adjacency_list[start]:
            self.adjacency_list[start].remove(end)

        # Uncomment for undirected graph (but be aware that methods like topological_sort will not work)
        # if start in self.adjacency_list[end]:
        #     self.adjacency_list[end].remove(start)

    def add_vertex(self):
        if self.free_ids:
            new_id = self.free_ids.pop()
        else:
            new_id = self.num_vertices
        self.adjacency_list[new_id] = []
        self.num_vertices += 1

    def remove_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            raise ValueError("Vertex does not exist")
        
        del self.adjacency_list[vertex]
        self.free_ids.append(vertex)
        self.num_vertices -= 1

        for key in self.adjacency_list:
            if vertex in self.adjacency_list[key]:
                self.adjacency_list[key].remove(vertex)

    # # Recursive DFS approach
    # def topological_sort_dfs_rec(self):
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
    def topological_sort_bfs_it(self):
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
    # def get_paths_dfs_rec(self, start, end, path=None):
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
    
    # Iteative BFS approach
    def get_paths_bfs_it(self, start, end):
        if start not in self.adjacency_list or end not in self.adjacency_list:
            return []
        
        paths = []
        queue = deque([(start, [start])]) # (current_vertex, current_path)
        
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
    # def get_shortest_path_dfs_rec(self, start, end, path=None):
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
    #             if sp:
    #                 if shortest_path is None or len(sp) < len(shortest_path):
    #                     shortest_path = sp
        
    #     return shortest_path if shortest_path else []
    
    # Iterative BFS approach
    def get_shortest_path_bfs_it(self, start, end):
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
    # def is_connected_dfs_rec(self, start, end, visited=None):
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
    def is_connected_dfs_it(self, start, end):
        if start not in self.adjacency_list or end not in self.adjacency_list:
            return False
        
        visited = set()
        stack = [start] # Note: Could be implemented with deque for better performance
        
        while stack:
            vertex = stack.pop()

            if vertex == end:
                return True
            
            elif vertex not in visited:
                visited.add(vertex)

                for neighbor in self.adjacency_list[vertex]:
                    stack.append(neighbor)
                
        return False

    # # Recursive BFS approach
    # Is skipped because it would be very complex to code
    # As iterative BFS is also more efficient, the recursive BFS is strongly not recommended

    # # Iterative BFS approach
    # def is_connected_bfs_it(self, start, end):
    #     if start not in self.adjacency_list or end not in self.adjacency_list:
    #         return False

    #     visited = set()
    #     queue = deque([start])
        
    #     while queue:
    #         vertex = queue.popleft()

    #         if vertex == end:
    #             return True

    #         elif vertex not in visited:
    #             visited.add(vertex)

    #             for neighbor in self.adjacency_list[vertex]:
    #                 queue.append(neighbor)
                
    #     return False


# Option 2: Using adjacency matrix
class Graph_AdjacencyMatrix:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices

        # Initialize adjacency matrix
        self.adjacency_matrix = [[0] * num_vertices for _ in range(num_vertices)]
        
        # Print the graph
        self.display()

    def display(self):
        for row in self.adjacency_matrix:
            print(row)

    def add_edge(self, start, end):
        if start >= self.num_vertices or end >= self.num_vertices or start < 0 or end < 0:
            raise ValueError("Vertices are out of bounds")

        self.adjacency_matrix[start][end] = 1

        # Uncomment for undirected graph (but be aware that methods like topological_sort will not work)
        # self.adjacency_matrix[end][start] = 1

    def remove_edge(self, start, end):
        if start >= self.num_vertices or end >= self.num_vertices or start < 0 or end < 0:
            raise ValueError("Vertices are out of bounds")
        
        self.adjacency_matrix[start][end] = 0

        # Uncomment for undirected graph (but be aware that methods like topological_sort will not work)
        # self.adjacency_matrix[end][start] = 0

    def add_vertex(self):
        self.num_vertices += 1

        for row in self.adjacency_matrix:
            row.append(0)
        self.adjacency_matrix.append([0] * self.num_vertices)

    def remove_vertex(self, vertex):
        if vertex >= self.num_vertices or vertex < 0:
            raise ValueError("Vertex does not exist")
        
        for row in self.adjacency_matrix:
            row.pop(vertex)
        self.adjacency_matrix.pop(vertex)

        self.num_vertices -= 1

    # # Recursive DFS approach
    # def topological_sort_dfs_rec(self):
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
    def topological_sort_bfs_it(self):
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
    # def get_paths_dfs_rec(self, start, end, path=None):
    #     if start >= self.num_vertices or end >= self.num_vertices or start < 0 or end < 0:
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
    
    # Iteative BFS approach
    def get_paths_bfs_it(self, start, end):
        if start >= self.num_vertices or end >= self.num_vertices or start < 0 or end < 0:
            return []
        
        paths = []
        queue = deque([(start, [start])]) # (current_vertex, current_path)
        
        while queue:
            vertex, path = queue.popleft()

            if vertex == end:
                paths.append(path)
            else:
                for neighbor in range(self.num_vertices):
                    if self.adjacency_matrix[vertex][neighbor] == 1 and neighbor not in path:
                        queue.append((neighbor, path + [neighbor]))
        
        return paths
    
    # # Recursive DFS approach
    # def get_shortest_path_dfs_rec(self, start, end, path=None):
    #     if start >= self.num_vertices or end >= self.num_vertices or start < 0 or end < 0:
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
    #             if sp:
    #                 if shortest_path is None or len(sp) < len(shortest_path):
    #                     shortest_path = sp
        
    #     return shortest_path if shortest_path else []
    
    # Iterative BFS approach
    def get_shortest_path_bfs_it(self, start, end):
        if start >= self.num_vertices or end >= self.num_vertices or start < 0 or end < 0:
            return []

        queue = deque([(start, [start])])
        visited = set()
        visited.add(start)

        while queue:
            vertex, path = queue.popleft()

            if vertex == end:
                return path
            
            for neighbor in range(self.num_vertices):
                if self.adjacency_matrix[vertex][neighbor] == 1 and neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))

        return []    

    # # Recursive DFS approach
    # def is_connected_dfs_rec(self, start, end, visited=None):
    #     if start >= self.num_vertices or end >= self.num_vertices or start < 0 or end < 0:
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
    def is_connected_dfs_it(self, start, end):
        if start >= self.num_vertices or end >= self.num_vertices or start < 0 or end < 0:
            return False
        
        visited = set()
        stack = [start] # Note: Could be implemented with deque for better performance
        
        while stack:
            vertex = stack.pop()

            if vertex == end:
                return True
            
            elif vertex not in visited:
                visited.add(vertex)

                for neighbor in range(self.num_vertices):
                    if self.adjacency_matrix[vertex][neighbor] == 1:
                        stack.append(neighbor)
                
        return False

    # # Recursive BFS approach
    # Is skipped because it would be very complex to code
    # As iterative BFS is also more efficient, the recursive BFS is strongly not recommended

    # # Iterative BFS approach
    # def is_connected_bfs_it(self, start, end):
    #     if start >= self.num_vertices or end >= self.num_vertices or start < 0 or end < 0:
    #         return False

    #     visited = set()
    #     queue = deque([start])
        
    #     while queue:
    #         vertex = queue.popleft()

    #         if vertex == end:
    #             return True

    #         elif vertex not in visited:
    #             visited.add(vertex)

    #             for neighbor in range(self.num_vertices):
    #                 if self.adjacency_matrix[vertex][neighbor] == 1:
    #                     queue.append(neighbor)
                
    #     return False



if __name__ == '__main__':
    # Test cases for adjacency list
    graph_1 = Graph_AdjacencyList(5)
    graph_1.add_edge(0, 1)
    graph_1.add_edge(1, 2)
    graph_1.add_edge(2, 3)
    graph_1.add_edge(3, 4)
    graph_1.display()

    # Test get_paths_bfs_it
    print("Paths from 0 to 4:", graph_1.get_paths_bfs_it(0, 4))  # Expected paths: [[0, 1, 2, 3, 4]]
    print("Paths from 0 to 2:", graph_1.get_paths_bfs_it(0, 2))  # Expected paths: [[0, 1, 2]]

    # Test get_shortest_path_bfs_it
    print("Shortest path from 0 to 4:", graph_1.get_shortest_path_bfs_it(0, 4))  # Expected: [0, 1, 2, 3, 4]
    print("Shortest path from 0 to 2:", graph_1.get_shortest_path_bfs_it(0, 2), "\n")  # Expected: [0, 1, 2]


    # Test cases for adjacency matrix
    graph_2 = Graph_AdjacencyMatrix(5)
    graph_2.add_edge(0, 1)
    graph_2.add_edge(1, 2)
    graph_2.add_edge(2, 3)
    graph_2.add_edge(3, 4)
    graph_2.display()

    # Test get_paths_bfs_it
    print("Paths from 0 to 4:", graph_2.get_paths_bfs_it(0, 4))  # Expected paths: [[0, 1, 2, 3, 4]]
    print("Paths from 0 to 2:", graph_2.get_paths_bfs_it(0, 2))  # Expected paths: [[0, 1, 2]]

    # Test get_shortest_path_bfs_it
    print("Shortest path from 0 to 4:", graph_2.get_shortest_path_bfs_it(0, 4))  # Expected: [0, 1, 2, 3, 4]
    print("Shortest path from 0 to 2:", graph_2.get_shortest_path_bfs_it(0, 2))  # Expected: [0, 1, 2]