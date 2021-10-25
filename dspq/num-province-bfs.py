"""
Q:https://leetcode.com/problems/number-of-provinces/submissions/
T(n) = O(n^2)
s(n) = O(n)
"""
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        #bfs
        
        #use a set to record the visited cities
        num_provinces = 0
        visited = set()
        
        # bfs to find the connected cities
        for city in range(len(isConnected)):
            # skip city if visited
            if city in visited:
                continue
            
            self.bfs(isConnected, city, visited)
            num_provinces += 1
        return num_provinces
    
    def bfs(self, isConnected, city, visited):
        
        queue = deque([city])
        
        while queue:
            city = queue.popleft()
            visited.add(city)
            for i in range(len(isConnected)):
                if i == city:
                    continue
                if isConnected[city][i] == 0:
                    continue
                if i in visited:
                    continue
                    
                # found a neighbor
                queue.append(i)
