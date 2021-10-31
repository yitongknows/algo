"""
T(n) = O(nlogn)
s(n) = n
"""

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # thought
        # zip the inputs together because we want to sort it later
        jobs = zip(startTime, endTime, profit)
        # sort jobs by endTime
        jobs = sorted(jobs, key=lambda x: x[1])
        
        # this is because our dp is consisted of the max profit at time x
        
        #initialize a dp array to store the end time, and the max_p at time n
        # at time 0, the max p = 0
        dp = [[0, 0]]
        # if need to store path
        dp_path = [[]]
        
        print(list(jobs))
        # for each job, two options
        # you don't do the job, then the max p will be the same as the max profit at the start end of this job, or < then the start time of this job
        # or you do the job, same logic + the current profit
        
        for start_time, end_time, profit in jobs:
            #binary search
            prior_profit, idx = self.binarySearch(dp, start_time)
            
            print(prior_profit)
            if prior_profit + profit > dp[-1][1]:
                dp.append([end_time, prior_profit + profit])
                #update path
                dp_path.append(dp_path[idx] + [(start_time,end_time,profit)])
        
        # return the last value
        print(dp)
        return dp[-1][1]
    
    def binarySearch(self, dp, start_time):
        # we want to find what is the max profit made before this start time
        start, end = 0, len(dp) - 1
        max_p = 0
        while start + 1 < end:
            mid = (start + end) // 2
            
            if dp[mid][0] > start_time:
                end = mid
            else:
                start = mid
        
        # compare to see what is the max
        if dp[end][0] <= start_time:
            return dp[end][1], end
        else:
            return dp[start][1], start
