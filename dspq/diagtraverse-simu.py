"""
Q: https://leetcode.com/problems/diagonal-traverse/submissions/
T(N) = M*N
S(N) = M*N
"""

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        # create an index sum dict to group the elements
        indexSum = {}
        # initialize the return val
        rv = []
        
        # loop through the matrix to populate the index Sum dictionary
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                
                # check if the current index sum is in the dict
                curr_sum = i + j
                if curr_sum in indexSum:
                    indexSum[curr_sum].append(mat[i][j])
                else:
                    indexSum[curr_sum] = [mat[i][j]]
        
        # no need to sort it because the order is based on the insertion
        for key, val in indexSum.items():
            rv.extend(val[::-1]) if key % 2 == 0 else rv.extend(val)
        
        return rv
