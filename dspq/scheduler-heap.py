"""
Question: https://leetcode.com/problems/meeting-scheduler/
vip
"""

class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        # build the heap first -> combine slots1 + slots2
        # only insert it if available time >= duration
        """
        T(n) = O(n) where n = len(slots1) + len(slots2)
        """
        timeslots = [x for x in (slots1 + slots2) if x[1] - x[0] >= duration]
        print(timeslots)
        
        #heapify the array
        #This function is used to convert the iterable into a heap data structure.
        # in-place
        # heapify takes O(n)
        heapq.heapify(timeslots)
        
        # iterate through the timeslot heap until only one left
        # while loop O(n), poping logn=> nlogn
        while len(timeslots) > 1:
          #poping takes O(logn)
            start1, end1 = heapq.heappop(timeslots)
            
            # get the next one for comparison
            #The heap[0] element also returns the smallest element each time
            start2, end2 = timeslots[0]
            
            # check if found result
            if end1 >= start2 + duration:
                return [start2, start2 + duration]                            
        
        # result not found, return empty array
        return []
