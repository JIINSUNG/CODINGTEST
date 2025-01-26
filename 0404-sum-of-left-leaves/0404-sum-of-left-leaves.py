# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        # left 단말 노드만 더하기

        self.answer = 0
        def traversal(node, isLeft):
            if not node:
                return
            
            # 단말 노드이며 왼쪽 노드 인 경우
            if not node.left and not node.right and isLeft:
                self.answer += node.val
                return
            
            traversal(node.left, True)
            traversal(node.right, False)
        traversal(root, False)
        return self.answer
            
            