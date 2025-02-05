# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.value = []

        def traversal(node):
            if not node:
                return
            self.value.append(node.val)
            traversal(node.next)
        
        traversal(head)

        for i in range(len(self.value)//2):
            if self.value[i] != self.value[-i-1]:
                return False
        return True