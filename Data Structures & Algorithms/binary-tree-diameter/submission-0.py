# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDiam = 0
        self.dfs(root)
        return self.maxDiam

    def dfs(self, root: Optional[TreeNode]) -> int:
        if (root == None):
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        self.maxDiam = max(self.maxDiam, left + right)
       
        return max(left,right) + 1