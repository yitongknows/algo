#Question
#Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
#Your algorithm's runtime complexity must be in the order of O(log n).
#If the target is not found in the array, return [-1, -1].

#Input: nums = [5,7,7,8,8,10], target = 8
#Output: [3,4]

class Solution:
    """
    @param nums: the array of integers
    @param target: 
    @return: the starting and ending position
    """
    def searchRange(self, nums, target):
        # Write your code here.
        appeared_once = False
        lbound, rbound = -1, -1
        lbound = self.binarySearch(nums, 0, len(nums)-1, target, appeared_once)
        
        if lbound == -1:
            return [lbound, rbound]
        
        appeared_once = True
        rbound = self.binarySearch(nums, 0, len(nums)-1, target, appeared_once)

        return [lbound, rbound]

    
    def binarySearch(self, nums, start, end, target, appeared_once):
        if end < start:
            return -1
            
        mid = int((start + end) / 2)

        if nums[mid] == target:
            if not appeared_once and (mid==0 or nums[mid-1] != target):
                return mid
            elif not appeared_once:
                return self.binarySearch(nums, start, mid-1, target, appeared_once)
            elif appeared_once and (mid > len(nums)-1 or nums[mid+1] != target):
                return mid
            elif appeared_once:
                return self.binarySearch(nums, mid+1, end, target, appeared_once)
            
        
        #recursion look at 0 - mid
        if target < nums[mid]:
            return self.binarySearch(nums, start, mid-1, target, appeared_once)

        #look at right side
        return self.binarySearch(nums, mid+1, end, target, appeared_once)