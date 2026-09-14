import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # use a queue for inserting in element that are on cooldown
        # use a heapq to extract the most occurance remaining character (efficiency)
        counts = Counter(tasks)
        heap = []
        queue = []
        timer = 0 
        for c in counts.values():
            heap.append(-c)
        heapq.heapify(heap)

        while heap or queue:
            # if queue is present and timer matches the first item
            if queue and timer == queue[0][1]:
                currentPair = queue.pop(0)
                heapq.heappush(heap, currentPair[0])
            # else if heap is also active
            if heap:
                current = heapq.heappop(heap)
                if current < -1:
                    current += 1
                    queue.append((current, timer + n + 1))

            timer += 1

        return timer