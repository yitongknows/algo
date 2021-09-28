"""
Q:https://www.lintcode.com/problem/587/
"""

class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """
    def twoSum6(self, nums, target):
        # use two pointers with opposite direction
        # error checking
        
        if not nums:
            return 0
        
        #sort the list
        nums.sort()

        pairs = set()

        left, right = 0, len(nums) - 1

        while left < right:

            if nums[left] + nums[right] > target:
                right -= 1
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                # found one match
                # 注意这里，找到一个pair之后，按数字从小到大的顺序建立一个tuple
                # set会自动去重
                # 然后因为我们找的是unique pair 所以向左移指针和
                # 向右移指针都无所谓
                pairs.add((nums[left], nums[right]))
                left +=1
        
        return len(pairs)