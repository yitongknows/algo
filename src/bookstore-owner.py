"""
Q: https://www.lintcode.com/problem/1849/
"""
class Solution:
    """
    @param customers: the number of customers
    @param grumpy: the owner's temper every day
    @param X: X days
    @return: calc the max satisfied customers
    """
    def maxSatisfied(self, customers, grumpy, X):
        # sliding window
        BAD_MOOD = 1
        GOOD_MOOD = 0

        #first we need to initialize the num of satisfy rate
        # when the window is at 0-X
        sum_satisfied = 0
        final_satisfied = 0
        for i in range(len(customers)):
            # good mood: grumpy[i] = 0
            # becuase of the initialization
            # boss will have a good mood in the first X day
            if i in range(X):
                sum_satisfied += customers[i]
            # else add the num of customers accoording to boss's mood
            else:
                sum_satisfied += (1-grumpy[i]) * customers[i]
        
        final_satisfied = sum_satisfied
        # slide the window
        # first initialize the two pointers
        # here if initized right = [X-1]
        # then in the while loop, have to do right + 1 < len(n)
        # if simply do X, then it is always gonna be the right bound
        # of the new window
        left, right = 0, X
        while right < len(customers):

            # re-calculate the sum based on the new window
            if grumpy[right] == BAD_MOOD:
                sum_satisfied += customers[right]
            if grumpy[left] == BAD_MOOD:
                sum_satisfied -= customers[left]
            
            left += 1
            right += 1
            # compare the new window result with the old one
            final_satisfied = max(sum_satisfied, final_satisfied)
        
        return final_satisfied