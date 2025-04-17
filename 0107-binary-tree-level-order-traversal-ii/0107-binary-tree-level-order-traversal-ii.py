# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        def bfs(node):
            if not node:
                return []
            
            queue = deque([node])
            result = []

            while queue:
                temp = []
                size = len(queue)
                for _ in range(size):
                    node = queue.popleft()
                    temp.append(node.val)

                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                result.append(temp)
            return result[::-1]
    
        return bfs(root)

