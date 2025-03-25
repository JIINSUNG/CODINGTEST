class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        answer = 0 
        start = 1

        meetings.sort(key = lambda x : (x[0]))
        
        for s, e in meetings:
            if start < s:
                answer += s - start
            start = max(start, e + 1)

        start-= 1        
        return answer + (days-start)
         