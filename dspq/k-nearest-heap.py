# T(n) = nlog(k)
# space = k for the heap

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #
        heap = []
        heapq.heapify(heap)
        for x, y in points:
            # turn miniheap to max heap
            # by default heap return the min, but we want to keep the min
            # so -1
            distance = -1 * (x**2 + y ** 2)
            #log(n)
            if len(heap) < k:
                heapq.heappush(heap, [distance, x, y])
            else:
                heapq.heappushpop(heap, [distance, x, y])
        
        # return x y
        return [[x, y] for _, x, y in heap]
            
