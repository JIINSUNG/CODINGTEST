# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]) -> (int, int):
            if node is None:
                return 0, 0
        
            left_with, left_without = dfs(node.left)

            right_with, right_without = dfs(node.right)

            current_with = node.val + left_without + right_without

            current_without = max(left_with, left_without) + max(right_with, right_without)

            return current_with, current_without

        return max(dfs(root))


        



