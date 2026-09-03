import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w)) 
        visited = set()
        minimum = 0
        heap = []
        heapq.heappush(heap, (0, k))

        while len(visited) != n and heap:
            distance, node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            if len(visited) == n:
                return distance
            
            for v, w in adj[node]:
                if v not in visited:
                    heapq.heappush(heap, (distance + w, v))  

        return -1
