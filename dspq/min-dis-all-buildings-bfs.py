class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        # some constant variables
        self.DIRECTIONS = [[0,1], [0, -1], [1, 0], [-1, 0]]
        self.LAND = 0
        self.BUILDING = 1
        self.OBSTACLE = 2
        self.rowLen = len(grid)
        self.colLen = len(grid[0])

        # use a matrix to count the sum of distance
        #and the number of building visited
        #[0, 0] = [sum_of_distances from all buildings, num of building visited]
        distances = [[[0, 0] for _ in range(self.colLen)] for _ in range(self.rowLen)]

        self.NUM_BUILDINGS = 0
        for i in range(self.rowLen):
            for j in range(self.colLen):
                if grid[i][j] == self.BUILDING:
                    self.NUM_BUILDINGS += 1
        
        # apply bfs on all buildings
        for i in range(self.rowLen):
            for j in range(self.colLen):
                
                # skip if not building
                if grid[i][j] != self.BUILDING:
                    continue
                
                # bfs on building to find the distance to all lands
                # 
                if not self.bfs(grid, i, j, distances):
                    return -1
                
        min_dis = float("inf")
        # find the min distance point
        for i in range(self.rowLen):
            for j in range(self.colLen):
                if grid[i][j] != self.LAND:
                    continue
                
                # skip points that cannot visit all buildings
                if distances[i][j][1] != self.NUM_BUILDINGS:
                    continue
                
                # update min_dis
                min_dis = min(min_dis, distances[i][j][0])
        
        return min_dis if min_dis != float("inf") else -1
    
    def bfs(self, grid, i, j, distances):
        #[i, j, 0] = [i, j, distance]
        queue = collections.deque([[i, j, 0]])
        visited = set()
        build_visited = 0
        
        while queue:
            x, y, dis = queue.popleft()

            for dx, dy in self.DIRECTIONS:
                new_x = x + dx
                new_y = y + dy
                
                # check if new coordinate is valid and land
                if not self.isValid(grid, new_x, new_y, visited):
                    continue
                
                if grid[new_x][new_y] == self.BUILDING:
                    build_visited += 1
                    visited.add((new_x, new_y))
                    continue
                
                if grid[new_x][new_y] == self.LAND:
                
                    #update the distance matrix
                    distances[new_x][new_y][0] += dis + 1
                    distances[new_x][new_y][1] += 1
                    queue.append([new_x, new_y, dis+1])
                    visited.add((new_x, new_y))

        # return true if all buildings are connected
        return self.NUM_BUILDINGS == build_visited
    
    
    def isValid(self, grid, x, y, visited):
        if x < 0 or x >= self.rowLen:
            return False
        if y < 0 or y >= self.colLen:
            return False
        if (x, y) in visited:
            return False
        return True
