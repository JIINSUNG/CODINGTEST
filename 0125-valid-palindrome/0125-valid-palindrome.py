class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = ''.join(char.lower() for char in s if char.isalnum())

        for i in range(len(word)//2):
            if word[i] != word[-i-1]:
                return False
        return True