"""
Original Question:https://leetcode.com/problems/two-sum/submissions/
T(n) = O(n)
S(n) = O(n)
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # use a hash set
        # example [1, 2, 3, 4] target=4 
        # for i = 0 => 1 we need to find if 4-1 = 3 is in the list
        # if it is, return
        
        hashset = set()
        for i in range(len(nums)):
            # first find it's pair, then insert
            # 一个pair （a，b）当中， 因为b还不存在， 所以
            # a会暂时找不到pair 但是轮到b的时候b会找到a
            number = nums[i]
            pair = target-number
            if pair in hashset:
                return nums.index(pair), i
            
            # insert the num
            hashset.add(number)
        
        # if nothing found
        return [-1, -1]