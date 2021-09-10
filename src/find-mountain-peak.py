class Solution:
    """
    @param A: An integers array.
    @return: return any of peek positions.
    There is an integer array which has the following features:

The numbers in adjacent positions are different.
A[0] < A[1] && A[A.length - 2] > A[A.length - 1].
We define a position P is a peak if:

A[P] > A[P-1] && A[P] > A[P+1]
Find a peak element in this array. Return the index of the peak.

It's guaranteed the array has at least one peak.
The array may contain multiple peeks, find any of them.
The array has at least 3 numbers in it.
样例
Example 1:

Input:

A = [1, 2, 1, 3, 4, 5, 7, 6]
Output:

1
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
