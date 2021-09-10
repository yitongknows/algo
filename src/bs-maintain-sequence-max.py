
class Solution:
    """
    @param nums: a mountain sequence which increase firstly and then decrease
    @return: then mountain top
    Given a mountain sequence of n integers which increase firstly and then decrease, find the mountain top(Maximum).
    """
    def mountainSequence(self, nums):
        # write your code here
        if not nums:
            return -1
        
        # set mid point
        start, end = 0, len(nums) -1
        
        while start+1 < end:
            mid = (start + end) //2
            
            # check start and end later
            if mid == 0 or mid == len(nums)-1:
                break;
                
            if nums[mid-1] < nums[mid] and nums[mid + 1] < nums[mid]:
                return nums[mid]
            
            elif nums[mid-1] < nums[mid]:
                start = mid
            else:
                end = mid
        
        #compare start with end
        return nums[0] if nums[0] > nums[-1] else nums[-1]

        