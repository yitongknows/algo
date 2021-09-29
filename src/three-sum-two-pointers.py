"""
Q:https://leetcode.com/problems/3sum/submissions/

T(n) = O(n^2)
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #leverage what we did for two sum
        # iterate through the first element a
        # find b+c = -a
        
        #don't want index, we can sort the array
        nums.sort()
        
        #two sum result
        # use set to obtain unique results
        solutions = []
        
        # a+ b+ c = 0, since we sorted the array
        # a< b< c
        for i in range(len(nums)):
            
            #skip if duplicates
            if i > 0 and nums[i-1] == nums[i]:
                continue
            
            target = -nums[i]

            self.find_two_sum(nums[i+1:], target, solutions)
        
        return solutions
    
    def find_two_sum(self, nums: List[int], target, solutions):
        # find all possible results, drop duplicate
        
        if not nums:
            return
        
        left, right = 0, len(nums) -1
        
        while left < right:
            if nums[left] + nums[right] > target:
                right -= 1
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                #find match
                # since array is sorted, left < right
                #remove duplicate
                new_match = [-target, nums[left], nums[right]]
                if new_match not in solutions:
                    solutions.append(new_match) 
                left += 1
