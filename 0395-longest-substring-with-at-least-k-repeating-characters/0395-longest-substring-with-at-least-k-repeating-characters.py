from collections import defaultdict

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) == 0 or len(s) < k:
            return 0

        counter = Counter(s)

        for i, chr in enumerate(s):
            if counter[chr] < k:
                return max(self.longestSubstring(s[:i], k), self.longestSubstring(s[i+1:], k))

        return len(s)


        