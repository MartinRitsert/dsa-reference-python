# import heapq


# Optimized Union Find
# Combines Union by Rank and Path Compression
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    # Uses path compression
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    # Uses union by rank
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)
    
    
# Kruskal's Algorithm (Minimum Spanning Tree) using the provided UnionFind class
# Optimal for sparse graphs
def kruskal(n, edges):
    if n == 0:
        return []

    # Initialize the UnionFind structure
    uf = UnionFind(n)
    mst = []
    
    # Sort edges by weight
    edges.sort(key=lambda x: x[2])
    
    # Iterate over sorted edges
    for u, v, weight in edges:
        if not uf.connected(u, v):  # Check if u and v are in different components
            uf.union(u, v)  # Union the two components
            mst.append((u, v, weight))  # Add the edge to the MST
    
    return mst


# # Prim's Algorithm (Minimum Spanning Tree) using adjacency list and heapq
# # Optimal for sparse graphs with similar efficiency to Kruskal's
# # However, Kruskal is easier to implement and thus preferred
# def prim_adj_list(n, edges, start_vertex=0):
#     if n == 0:
#         return []

#     # Initialize adjacency list
#     adjacency_list = {i: [] for i in range(n)}
#     for u, v, weight in edges:
#         # Ensure vertices are within bounds if not already guaranteed by input
#         if 0 <= u < n and 0 <= v < n:
#             adjacency_list[u].append((v, weight))
#             adjacency_list[v].append((u, weight)) # Graph is undirected
#         # else:
#             # Optionally handle or log out-of-bounds vertices from edges list

#     # min_heap stores tuples of (cost_to_reach_vertex, vertex_to_reach, parent_in_mst)
#     min_heap = [(0, start_vertex, -1)]  # parent is -1 for start_vertex

#     # visited[i] will be true if vertex i is included in MST
#     visited = [False] * n
    
#     mst = []
#     vertices_in_mst_count = 0

#     while min_heap and vertices_in_mst_count < n:
#         cost, u, parent_of_u = heapq.heappop(min_heap)

#         if visited[u]:
#             continue

#         visited[u] = True
#         vertices_in_mst_count += 1

#         if parent_of_u != -1:
#             v1, v2 = sorted((parent_of_u, u))
#             mst.append((v1, v2, cost))

#         # Explore neighbors of u
#         if u in adjacency_list:
#             for neighbor_v, weight_uv in adjacency_list[u]:
#                 if not visited[neighbor_v]:
#                     heapq.heappush(min_heap, (weight_uv, neighbor_v, u))
                
#     return mst


# Prim's Algorithm (Minimum Spanning Tree) using adjacency matrix
# Optimal for dense graphs
def prim_adj_mat(n, edges, start_vertex=0):
    if n == 0:
        return []

    # Initialize adjacency matrix
    adj_matrix = [[float('inf')] * n for _ in range(n)]

    for u, v, weight in edges:
        if 0 <= u < n and 0 <= v < n:
            adj_matrix[u][v] = weight
            adj_matrix[v][u] = weight  # Undirected graph

    # min_cost[i] will hold the minimum weight edge to connect vertex i to the MST
    min_cost = [float('inf')] * n

    # parent[i] will store the parent of vertex i in the MST
    parent = [-1] * n

    # visited[i] will be true if vertex i is included in MST
    visited = [False] * n
    
    mst = []

    # Start with the initial start_vertex
    min_cost[start_vertex] = 0

    for _ in range(n):
        # Find the unvisited vertex with the minimum cost
        min_val = float('inf')
        u = -1  # Current vertex to add to MST

        for v_idx in range(n):
            if not visited[v_idx] and min_cost[v_idx] < min_val:
                min_val = min_cost[v_idx]
                u = v_idx
        
        # No more reachable vertices
        if u == -1:
            break

        visited[u] = True

        if parent[u] != -1:
            v1, v2 = sorted((parent[u], u))
            mst.append((v1, v2, adj_matrix[u][parent[u]]))

        # Update costs for adjacent vertices
        for v_neighbor in range(n):
            if not visited[v_neighbor] and adj_matrix[u][v_neighbor] != float('inf'):
                if adj_matrix[u][v_neighbor] < min_cost[v_neighbor]:
                    min_cost[v_neighbor] = adj_matrix[u][v_neighbor]
                    parent[v_neighbor] = u
    
    return mst


if __name__ == '__main__':
    edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]  # Example edges (u, v, weight)
    n = 4  # Number of vertices
    mst = kruskal(n, edges)

    # Print the resulting MST
    print("Minimum Spanning Tree:", mst)