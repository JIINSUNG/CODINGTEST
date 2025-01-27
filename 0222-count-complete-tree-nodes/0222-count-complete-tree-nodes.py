# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        self.answer = 0 

        def traversal(node):
            if not node:
                return
            
            self.answer +=1
            traversal(node.left)
            traversal(node.right)
        traversal(root)

        return self.answer