class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
       # solution 1:
        # Use Union Find
        
        self.parent = list(range(len(edges) +1))
        marked = -1
        for i in range(0,len(edges)):
            if self.find(edges[i][0]) == self.find(edges[i][1]):
                marked = i
                continue
            else:
                self.union(edges[i][0], edges[i][1])
        if marked != -1:
            return edges[marked]
        else:
            return []

    def find(self, node: int) -> int:
        while (self.parent[node] != node):
            node = self.parent[node]
        return node

    def union(self,a: int, b: int):
        a_root = self.find(a)
        b_root = self.find(b)
        self.parent[a_root] = b_root

            