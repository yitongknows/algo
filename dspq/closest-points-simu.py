"""
Q: https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/
T(N) = O(n)
S(N) = O(1)
"""

class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        min_dis = float("inf")
        min_idx = -1
        # iterate through each point
        for i in range(len(points)):
            
            x2, y2 = points[i]
            
            # skip invalid points
            if x2 != x and y2 != y:
                continue
            
            curr_dis = self.calculateDistance(x, y, x2, y2)
            if curr_dis < min_dis:
                min_dis = curr_dis
                min_idx = i
        
        return min_idx
                
    
    def calculateDistance(self, x1, y1, x2, y2):
        return abs(x1 - x2) + abs(y1 - y2)
