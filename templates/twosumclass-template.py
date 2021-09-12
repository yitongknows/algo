class TwoSum:
    def __init__(self):
        self.nums = []

    def add(self, number):
        self.nums.append(number)
        index = len(self.nums) - 1

        # insertion sort
        # compare value with the previous one
        # swap if neccessary
        # T(n) = O(n), Space(n) = O(n)
        # boundary check, prevent index out of array
        while index > 0 and self.nums[index-1] > self.nums[index]:
            self.nums[index-1], self.nums[index] = \
            self.nums[index], self.nums[index -1]
            index -= 1
    
    # t(n) = O(n) space(n) = O(n)
    def find(self, target_value):
        #define two pointer
        left, right = 0, len(self.nums) - 1
        while left < right:
            TwoSum = self.nums[left] + self.nums[right]

            # if the sum < target, move the left pointer to the right
            # so that the sum is a little bit larget
            if TwoSum < target_value:
                left += 1
            
            # if the sum > target, move the right pointer to the left
            # so that the sum is a little bit smaller
            elif TwoSum > target_value:
                right -= 1
            else: # twosum == target, we found the answer
                return True
        
        # no answers found
        return False