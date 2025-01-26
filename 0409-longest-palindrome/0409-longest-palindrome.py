class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        answer = 0
        findOdd = False
        for value in count.values():
            if value % 2 == 0:
                answer += value
            else:
                findOdd = True
                answer += value-1
        if findOdd:
            return answer + 1 
        else:
            return answer

            


