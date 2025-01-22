class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        cnt = ''
        for digit in digits:
            cnt += str(digit)
        cnt = int(cnt)+1
        cnt = str(cnt)
        answer = []
        for c in cnt:
            answer.append(int(c))
        return answer
