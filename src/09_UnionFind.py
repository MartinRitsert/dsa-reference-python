# # 1. Quick Find
# class UnionFind:
#     def __init__(self, size: int) -> None:
#         self.root = [i for i in range(size)]

#     def find(self, x: int) -> int:
#         """Find the root of x. O(1) time, O(1) space."""
#         return self.root[x]

#     def union(self, x: int, y: int) -> None:
#         """Merge the sets containing x and y. O(n) time, O(1) space."""
#         root_x = self.find(x)
#         root_y = self.find(y)
#         if root_x != root_y:
#             for i in range(len(self.root)):
#                 if self.root[i] == root_y:
#                     self.root[i] = root_x

#     def connected(self, x: int, y: int) -> bool:
#         """Check if x and y are in the same set. O(1) time, O(1) space."""
#         return self.find(x) == self.find(y)
 
# # 2. Quick Union
# # Preferable to Quick Find
# class UnionFind:
#     def __init__(self, size: int) -> None:
#         self.root = [i for i in range(size)]

#     def find(self, x: int) -> int:
#         """Find the root of x by following parent pointers. O(n) time, O(1) space."""
#         while x != self.root[x]:
#             x = self.root[x]
#         return x

#     def union(self, x: int, y: int) -> None:
#         """Merge the sets containing x and y. O(n) time, O(1) space."""
#         root_x = self.find(x)
#         root_y = self.find(y)
#         if root_x != root_y:
#             self.root[root_y] = root_x

#     def connected(self, x: int, y: int) -> bool:
#         """Check if x and y are in the same set. O(n) time, O(1) space."""
#         return self.find(x) == self.find(y)
    
# # 3. Union by Rank
# # Is an optimization of the Quick Union algorithm
# class UnionFind:
#     def __init__(self, size: int) -> None:
#         self.root = [i for i in range(size)]
#         self.rank = [1] * size

#     def find(self, x: int) -> int:
#         """Find the root of x by following parent pointers. O(log n) time, O(1) space."""
#         while x != self.root[x]:
#             x = self.root[x]
#         return x

#     def union(self, x: int, y: int) -> None:
#         """Merge sets by attaching smaller tree under larger. O(log n) time, O(1) space."""
#         root_x = self.find(x)
#         root_y = self.find(y)
#         if root_x != root_y:
#             if self.rank[root_x] > self.rank[root_y]:
#                 self.root[root_y] = root_x
#             elif self.rank[root_x] < self.rank[root_y]:
#                 self.root[root_x] = root_y
#             else:
#                 self.root[root_y] = root_x
#                 self.rank[root_x] += 1

#     def connected(self, x: int, y: int) -> bool:
#         """Check if x and y are in the same set. O(log n) time, O(1) space."""
#         return self.find(x) == self.find(y)

# # 4. Path Compression
# # Is an optimization of the Quick Union algorithm
# class UnionFind:
#     def __init__(self, size: int) -> None:
#         self.root = [i for i in range(size)]

#     def find(self, x: int) -> int:
#         """Find the root of x with path compression. O(log n) amortized, O(log n) space."""
#         if x == self.root[x]:
#             return x
#         self.root[x] = self.find(self.root[x])
#         return self.root[x]

#     def union(self, x: int, y: int) -> None:
#         """Merge the sets containing x and y. O(log n) amortized, O(log n) space."""
#         root_x = self.find(x)
#         root_y = self.find(y)
#         if root_x != root_y:
#             self.root[root_y] = root_x

#     def connected(self, x: int, y: int) -> bool:
#         """Check if x and y are in the same set. O(log n) amortized, O(log n) space."""
#         return self.find(x) == self.find(y)


# 5. Optimized Union Find
# Combines Union by Rank and Path Compression
class UnionFind:
    def __init__(self, size: int) -> None:
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    # Recursive path compression (standard textbook approach — simple and concise):
    def find(self, x: int) -> int:
        """Find the root of x with path compression. O(alpha(n)) amortized, O(alpha(n)) space."""
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    # # Iterative path compression (two-pass: find root, then compress):
    # def find(self, x: int) -> int:
    #     """Find the root of x with path compression. O(alpha(n)) amortized, O(1) space."""
    #     root = x
    #     while root != self.root[root]:
    #         root = self.root[root]
    #     while x != root:
    #         next_x = self.root[x]
    #         self.root[x] = root
    #         x = next_x
    #     return root

    # Uses union by rank
    def union(self, x: int, y: int) -> None:
        """Merge the sets containing x and y. O(alpha(n)) amortized, O(alpha(n)) space."""
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.root[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.root[root_x] = root_y
            else:
                self.root[root_y] = root_x
                self.rank[root_x] += 1

    def connected(self, x: int, y: int) -> bool:
        """Check if x and y are in the same set. O(alpha(n)) amortized, O(alpha(n)) space."""
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