class Solution:
    """
    @param A: a list of integer
    @param K: a integer
    @param L: a integer
    @return: return the maximum number of apples that they can collect.
    """
    def PickApples(self, A, K, L):
        # write your code here
        n = len(A)
        INVALID = -1
        max_apple = INVALID
        # check corner case
        if K+L > n:
            return INVALID

        for i in range(n):
            # don't know if L should be at left, K should be at right
            # and vice versa
            # so check both cases
            # 这里用的是隔板法
            leftMaxL = self.findMax(A, L, 0, i)
            rightMaxK = self.findMax(A, K, i, n)

            leftMaxK = self.findMax(A, K, 0, i)
            rightMaxL = self.findMax(A, L, i, n)
            
            # check corner cases
            if leftMaxL != INVALID and rightMaxK != INVALID:
                max_apple = max(max_apple, leftMaxL+rightMaxK)

            if leftMaxK != INVALID and rightMaxL != INVALID:   
                max_apple = max(max_apple, leftMaxK + rightMaxL)

            #if max_apple == float("-inf"):
                #return -1

        return max_apple

    def findMax(self, A, num_apples, lbound, rbound):
        ZERO_APPLE_COLLECTED = -1

        # check corner case
        if rbound - lbound < num_apples:
            return ZERO_APPLE_COLLECTED
        
        apples, max_apples = 0, 0

        # sliding window initialization
        for i in range(lbound, lbound+num_apples):
            apples += A[i]
        max_apples = apples

        # slide the window
        left, right = lbound, lbound + num_apples
        while right < rbound:
            apples += A[right]
            apples -= A[left]
            max_apples = max(max_apples, apples)

            left += 1
            right += 1
        return max_apples