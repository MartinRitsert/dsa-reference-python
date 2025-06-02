# # 1. Quick Find
# class UnionFind:
#     def __init__(self, size: int) -> None:
#         self.root = [i for i in range(size)]

#     def find(self, x: int) -> int:
#         return self.root[x]
		
#     def union(self, x: int, y: int) -> None:
#         rootX = self.find(x)
#         rootY = self.find(y)
#         if rootX != rootY:
#             for i in range(len(self.root)):
#                 if self.root[i] == rootY:
#                     self.root[i] = rootX

#     def connected(self, x: int, y: int) -> bool:
#         return self.find(x) == self.find(y)
 
# # 2. Quick Union
# # Preferable to Quick Find
# class UnionFind:
#     def __init__(self, size: int) -> None:
#         self.root = [i for i in range(size)]

#     def find(self, x: int) -> int:
#         while x != self.root[x]:
#             x = self.root[x]
#         return x
		
#     def union(self, x: int, y: int) -> None:
#         rootX = self.find(x)
#         rootY = self.find(y)
#         if rootX != rootY:
#             self.root[rootY] = rootX

#     def connected(self, x: int, y: int) -> bool:
#         return self.find(x) == self.find(y)
    
# # 3. Union by Rank
# # Is an optimization of the Quick Union algorithm
# class UnionFind:
#     def __init__(self, size: int) -> None:
#         self.root = [i for i in range(size)]
#         self.rank = [1] * size

#     def find(self, x: int) -> int:
#         while x != self.root[x]:
#             x = self.root[x]
#         return x
		
#     def union(self, x: int, y: int) -> None:
#         rootX = self.find(x)
#         rootY = self.find(y)
#         if rootX != rootY:
#             if self.rank[rootX] > self.rank[rootY]:
#                 self.root[rootY] = rootX
#             elif self.rank[rootX] < self.rank[rootY]:
#                 self.root[rootX] = rootY
#             else:
#                 self.root[rootY] = rootX
#                 self.rank[rootX] += 1

#     def connected(self, x: int, y: int) -> bool:
#         return self.find(x) == self.find(y)
    
# # 4. Path Compression
# # Is an optimization of the Quick Union algorithm
# class UnionFind:
#     def __init__(self, size: int) -> None:
#         self.root = [i for i in range(size)]

#     def find(self, x: int) -> int:
#         if x == self.root[x]:
#             return x
#         self.root[x] = self.find(self.root[x])
#         return self.root[x]
		
#     def union(self, x: int, y: int) -> None:
#         rootX = self.find(x)
#         rootY = self.find(y)
#         if rootX != rootY:
#             self.root[rootY] = rootX

#     def connected(self, x: int, y: int) -> bool:
#         return self.find(x) == self.find(y)


# 5. Optimized Union Find
# Combines Union by Rank and Path Compression
class UnionFind:
    def __init__(self, size: int) -> None:
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    # Uses path compression
    def find(self, x: int) -> int:
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    # Uses union by rank
    def union(self, x: int, y: int) -> None:
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

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


if __name__ == '__main__':
    uf = UnionFind(10)
    # 1-2-5-6-7 3-8-9 4
    uf.union(1, 2)
    uf.union(2, 5)
    uf.union(5, 6)
    uf.union(6, 7)
    uf.union(3, 8)
    uf.union(8, 9)
    print(uf.connected(1, 5))  # true
    print(uf.connected(5, 7))  # true
    print(uf.connected(4, 9))  # false
    # 1-2-5-6-7 3-8-9-4
    uf.union(9, 4)
    print(uf.connected(4, 9))  # true