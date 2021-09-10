# Question: Find any position of target number in a sorted array.
# Return -1 if target does not exist

class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def findPosition(self, nums, target):
        # write your code here
        return self.binarySearch(nums, 0, len(nums)-1, target)
    
    def binarySearch(self, nums, start, end, target):
        if end < start:
            return -1
            
        mid = int((start + end) / 2)

        #base case
        if nums[mid] == target:
            return mid
        
        #recursion look at 0 - mid
        if target < nums[mid]:
            return self.binarySearch(nums, start, mid-1, target)

        #look at right side
        return self.binarySearch(nums, mid+1, end, target)