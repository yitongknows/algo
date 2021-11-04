class Solution:
    def minPatches(self, nums, n):
        limit, count, i = 0, 0, 0
        
        while limit < n:
            if i < len(nums) and nums[i] <= limit + 1:
                limit += nums[i]
                i += 1
            else:
                count += 1
                limit = limit + (limit + 1)       
                
        return count
