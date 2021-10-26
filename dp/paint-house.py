"""
Q: https://www.lintcode.com/problem/515/description
"""
class Solution:
    """
    @param costs: n x 3 cost matrix
    @return: An integer, the minimum cost to paint all houses
    """
    def minCost(self, costs):
        n = len(costs)

        if not n:
            return 0
        """
        Note: DON'T use [[0]*3] * n, It's a trap
        """
        # initilization
        dp = [[0] * 3 for _ in range(n)]
        
        dp[0] = costs[0]

        for i in range(1, n):
            dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i][0]
            dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i][1]
            dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + costs[i][2]
        #print(dp)
        return min(dp[n-1])
 

####Solution 2: rolling arrays
    def minCost(self, costs):
        n = len(costs)

        if not n:
            return 0
        
        # initilization
        # use rolling array to optimize space complexity
        dp = [[0] * 3 for _ in range(2)]

        dp[0] = costs[0]

        new = 0
        old = 1

        for i in range(1, n):
            #switch new and old
            new, old = old, new

            dp[new][0] = min(dp[old][1], dp[old][2]) + costs[i][0]
            dp[new][1] = min(dp[old][0], dp[old][2]) + costs[i][1]
            dp[new][2] = min(dp[old][0], dp[old][1]) + costs[i][2]

        #print(dp)
        return min(dp[new])
