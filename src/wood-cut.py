"""
Q: https://www.lintcode.com/problem/183/
"""
class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """
    def woodCut(self, L, k):
        # write your code here
        # use the classic binary search
        # set a pivot
        # the lower boundary is 1 
        # the max boundary is max(L), because if len > max(L), we have 0 piece
        # here left and right are indices

        #error checking
        if not L:
            return 0
            
        left, right = 0, max(L)

        while left + 1 < right:
            # initialize it as the mid point
            mid = (left + right) // 2
            if self.is_valid(L, mid, k):
                left = mid
            else:
                right = mid
        
        # here either left or right has the mid value 
        # check again to see the correct val if left or right

        if self.is_valid(L, right, k):
            return right
        return left
        


    def is_valid(self, L, mid, k):
        # calculate the number of wood pieces with length mid
        num_wood = 0
        for wood in L:
            num_wood += wood // mid

        if num_wood >= k:
            return True
        else:
            return False