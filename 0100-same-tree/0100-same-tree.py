# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
    
        if not p or not q or p.val != q.val:
            return False

        tree =[[],[]]

        def traversal(node, idx):
            if not node:
                tree[idx].append(None)
                return
            traversal(node.left, idx)
            tree[idx].append(node.val)    
            traversal(node.right, idx)

        traversal(p, 0)
        traversal(q, 1)

        return tree[0] == tree[1]

        


        