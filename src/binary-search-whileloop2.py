class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    Find the last position of a target number in a sorted array. Return -1 if target does not exist.
    """
    def lastPosition(self, nums, target):
        # write your code here
        if not nums:
            return -1
        
        # set mid point
        start, end = 0, len(nums) -1
        
        while start+1 < end:
            mid = (start + end) //2
            
            if nums[mid] == target and mid < len(nums) and nums[mid+1] != target:
                return mid
            
            elif target < nums[mid]:
                end = mid
            else:
                start = mid
        
        # check the last element
        if nums[-1] == target: return (len(nums) -1)
        
        if start != -1 and nums[start] == target: return start
        
        return -1