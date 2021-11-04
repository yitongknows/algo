from heapq import *

class Solution:
    def employeeFreeTime(self, schedule):
        heap = []
        for emp in schedule:
            for iv in emp:
                heap.append((iv.start, iv.end))
        heapify(heap)
        
        s, e = heappop(heap)
        free = e
        res = []
        while heap:
            s, e = heappop(heap)
            if s > free:
                res.append(Interval(free, s))
                free = e
            else:
                free = max(free, e)
        return res
        
