class Solution:
    """
    @param A: An integers array.
    @return: return any of peek positions.
    """
    def findPeak(self, A):
        # arr has at least 3 element, no need to check error
        start, end = 0, len(A) -1

        while start+1 < end:
            mid = (start+end) //2

            if A[mid-1] < A[mid] and A[mid+1] < A[mid]:
                return mid
            elif A[mid] > A[mid-1]:
                start = mid
            else:
                end = mid