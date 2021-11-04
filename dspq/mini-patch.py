class Solution:
    def minPatches(self, nums, n):
        reach, ans, idx = 0, 0, 0
        
        while reach < n:
            if idx < len(nums) and nums[idx] <= reach + 1:
                reach += nums[idx]
                idx += 1
            else:
                ans += 1
                reach = 2*reach + 1       
                
        return ans
