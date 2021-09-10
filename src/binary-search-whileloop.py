class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    Find any position of a target number in a sorted array. Return -1 if target does not exist.
    """
    def findPosition(self, nums, target):
        # write your code here
        #error checking
        if not nums:
            return -1
        
        # set mid point
        start, end = 0, len(nums) -1
        
        while start+1 < end:
            mid = (start + end) //2
            
            if nums[mid] == target:
                return mid
            
            if target < nums[mid]:
                end = mid
            else:
                start = mid
        
        # check the last element
        if start != -1 and nums[start] == target: return start
        
        return (len(nums) -1) if nums[-1] == target else -1