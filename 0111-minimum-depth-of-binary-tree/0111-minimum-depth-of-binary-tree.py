# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.answer = float('inf')

        def traversal(node, depth):
            if not node:
                return
            if not node.left and not node.right:
                self.answer = min(self.answer, depth)
            
            traversal(node.left, depth+1)
            traversal(node.right, depth+1)
        
        traversal(root, 1)

        return self.answer