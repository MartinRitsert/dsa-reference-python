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

    # Build component: 1-2-5-6-7
    uf.union(1, 2)
    uf.union(2, 5)
    uf.union(5, 6)
    uf.union(6, 7)

    # Build component: 3-8-9
    uf.union(3, 8)
    uf.union(8, 9)

    # Element 4 remains solo (no union operations)

    # Test connected within first component
    assert uf.connected(1, 5), "1 and 5 should be connected"
    assert uf.connected(5, 7), "5 and 7 should be connected"
    assert uf.connected(1, 7), "1 and 7 should be connected"

    # Test connected within second component
    assert uf.connected(3, 9), "3 and 9 should be connected"

    # Test solo element 4 is not connected to anyone
    assert not uf.connected(4, 9), "4 (solo) should not be connected to 9"
    assert not uf.connected(4, 1), "4 (solo) should not be connected to 1"
    assert not uf.connected(1, 3), "Components 1-2-5-6-7 and 3-8-9 should not be connected"

    # Test union: connect solo element 4 to component 3-8-9
    uf.union(9, 4)
    assert uf.connected(4, 9), "4 and 9 should now be connected"
    assert uf.connected(3, 4), "3 and 4 should now be connected"

    # Test find returns same root for connected elements
    assert uf.find(1) == uf.find(7), "Connected elements should have same root"
    assert uf.find(3) == uf.find(4), "Connected elements should have same root"

    print("All tests passed!")