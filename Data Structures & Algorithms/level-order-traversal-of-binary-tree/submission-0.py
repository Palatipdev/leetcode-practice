# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []

        resultList = []
        q = deque()
        q.append(root)

        
        while q:
            temporaryList = []
            for _ in range(len(q)):
                currentNode = q.popleft()
                temporaryList.append(currentNode.val)
                if currentNode.left != None:
                    q.append(currentNode.left)
                if currentNode.right != None:
                    q.append(currentNode.right)
            resultList.append(temporaryList)
        return resultList

            