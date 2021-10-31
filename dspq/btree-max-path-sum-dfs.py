# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None, is_alive=True):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.is_alive = is_alive
"""
Time complexity: O(N), where N is number of nodes, since we visit each node not more than 2 times.

Space complexity: O(H), where H is a tree height, to keep the recursion stack. 
In the average case of balanced tree, the tree height H =logN, in the worst case of skewed tree,H=N.
"""
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # two cases
        # 1. path sum goes through the root
        # the path sum does not goes through root
        # dfs
        
        self.max = float("-inf")
        
        # root max = left_max + right_max
        self.dfs(root)
        
        return max(self.max, root.val)
    
    def dfs(self, root):
        
        #base case, leave root has sum of 0
        if root is None:
            return float("-inf")
        
        left_sum = max(self.dfs(root.left), 0)
        right_sum = max(self.dfs(root.right), 0)
        
        current_sum = root.val + max(left_sum, right_sum)
        
        self.max = max(self.max, current_sum, root.val + left_sum + right_sum)
        
        return current_sum
