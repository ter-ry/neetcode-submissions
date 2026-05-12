import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        result = []
        for x1, x2 in points:
            heap.append((x1**2 + x2**2, [x1, x2]))
        heapq.heapify(heap)

        while k > 0:
            distance, [y1, y2] = heapq.heappop(heap)
            result.append([y1, y2])
            k -= 1
        
        return result
        
        