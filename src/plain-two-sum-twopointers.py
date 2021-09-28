"""
Q:https://leetcode.com/problems/two-sum/submissions/

"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # use two pointers with the opposite direction
        
        #error checking
        if not nums:
            return [-1, -1]
        
        # convert the index and value into a tuple list
        numbers = [
            (number, index)
            for index, number in enumerate(nums)
        ]
        print(numbers)
        #first sort the list
        numbers.sort()
        
        left, right = 0, len(nums) - 1
        
        while left < right:
            if numbers[left][0] + numbers[right][0] > target:
                right -= 1
            elif numbers[left][0] + numbers[right][0] < target:
                left += 1
            else:
                #equals
                return sorted([numbers[left][1], numbers[right][1]])
        
        # if nothing found
        return [-1, -1]