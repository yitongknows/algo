"""
Q: https://leetcode.com/problems/course-schedule-ii/
T(N) = len(courses) + len(edges) where edges is the relationship among courses
T(N) = len(courses) + len(edges)
"""
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # first construct the graph
        # use a dict to store the course order
        # use a second dict to indicate the in-degree for each course
        courseGraph = defaultdict(list)
        inDegree = {}
        courseOrder = []
        
        for dest, src in prerequisites:
            courseGraph[src].append(dest)
            
            #increment the indegree for the destination course
            inDegree[dest] = inDegree.get(dest, 0) + 1
        
        queue = deque([x for x in range(numCourses) if x not in inDegree])
        
        while queue:
            course = queue.popleft()
            courseOrder.append(course)
            
            # iterate through current course's neighbor
            if course not in courseGraph:
                continue
            
            for dependency in courseGraph[course]:
                inDegree[dependency] -= 1
                
                if inDegree[dependency] == 0:
                    queue.append(dependency)
                
        return courseOrder if len(courseOrder) == numCourses else []
        
