# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.answer = []
        def traversal(node, path):
            if not node:
                return
            

            if not node.left and not node.right and sum(path) + node.val == targetSum:
                self.answer.append(path + [node.val])
                return
            
            traversal(node.left, path + [node.val])
            traversal(node.right, path + [node.val])
        
        traversal(root, [])
        
        return self.answer