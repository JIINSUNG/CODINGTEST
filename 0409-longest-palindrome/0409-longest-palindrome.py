class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        length = 0
        odd_found = False

        for value in counter.values():
            if value % 2 == 0:
                length += value
            else:
                length += value - 1
                if not odd_found:
                    odd_found = True
                    length += 1

        return length

            


