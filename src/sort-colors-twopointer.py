"""
Q:https://leetcode.com/problems/sort-colors/submissions/

O(n) = 1
T(n) = n
"""
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return []
        
        # use two pointer to act as the boundaries between
        # 0 and 1 and 1 and 2
        # use a third pointer to go through the list
        # swap if neccessary
        # everything < pointer left is 0
        # everything > pointer right is 2
        left, right = 0, len(nums) -1
        curr = left
        
        # if curr > left, the rest of the list should be 2
        while curr <= right:
            #if curr = 0, move both left and curr to the right
            if nums[curr] == 0:
                nums[curr], nums[left] = nums[left], nums[curr]
                left += 1
                curr += 1
            # if curr = 2, move to the end
            elif nums[curr] == 2:
                nums[curr], nums[right] = nums[right], nums[curr]
                right -= 1
            else:
                curr += 1
                