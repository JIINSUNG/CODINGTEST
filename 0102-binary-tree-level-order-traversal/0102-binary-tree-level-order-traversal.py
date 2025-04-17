# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def bfs(node):
            if not node:
                return []
            
            result = [] 
            queue = deque([root])
            while queue:
                same_level = len(queue)
                temp = []
                for _ in range(same_level):
                    node = queue.popleft()
                    temp.append(node.val)

                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)

                result.append(temp)
            return result
            
        
        return bfs(root)