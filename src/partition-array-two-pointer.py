"""
Q: https://www.lintcode.com/problem/31/description
"""

class Solution:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        # write your code here
        # error checking
        if not nums:
            return 0
        
        left, right = 0, len(nums) - 1
        # remember here is <= , not <
        while left < right:
            while left <= right and nums[left] < k:
                left += 1
            while left <= right and nums[right] >=k:
                right -= 1
            
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                # at this point, left > k, right < k
                # so we swap the two
                # remember to increment left and decrement? right
                left += 1
                right -= 1
        print(nums)
        return left

        