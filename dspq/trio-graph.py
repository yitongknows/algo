"""
T(n) = O(v^3)
s(n) = O(len(edges))
"""

class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        #build the graph first
        graph = defaultdict(set)
        
        # CONSTANT 
        TRIO_CONNECTION = 6
        
        # use dict to keep track of the connections for each node
        # set is to remove duplicates
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
            
        min_degree = float("inf")
        
        # sorted here is for optimization
        # 1-indexed
        # find a trio relationship
        ##for i in range(1, n+1):

        #sort the graph for optimization
        for i in sorted(graph.keys(), key = lambda x: len(graph[x])):
            
            # for optimization
            # because we sorted by the number of connections
            # if we found 1, 
            if len(graph[i]) >= min_degree / 3:
                break
            
            for j in graph[i]:
                for k in graph[j]:
                    
                    # j <=> i, k <=> j, check if k <=> i
                    if k not in graph[i]:
                        continue
                    
                    # k in i, find our trio relationship
                    degree = len(graph[i]) + len(graph[j])
                    \ + len(graph[k])
                    min_degree = min(min_degree, degree)
            
        min_degree -= TRIO_CONNECTION
        
        return min_degree if min_degree != float("inf") else -1
