# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.answer = False
        def traversal(node, sum):
            if not node:
                return
   
            if not node.left and not node.right and sum + node.val == targetSum:
                self.answer = True
                return 
            
            
            traversal(node.left, sum + node.val)
            traversal(node.right, sum + node.val)
        
        if not root:
            return False

        traversal(root, 0)
        return self.answer

        