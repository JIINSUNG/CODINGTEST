from collections import defaultdict
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        answer = ''
        dictionary = defaultdict(list)
        dict_idx = 0
        idx = 0
        cnt = 0
        flag = 1
        # numRows : 3, len(s) : 14
        while cnt < len(s):
            # dictionary[0] : ['P'], dictionary[1]: ['A'] dictionary[2]: ['Y']
            # idx : 1
            # cnt = 1
            dictionary[dict_idx].append(s[idx])            
            
            dict_idx += flag
            
            if dict_idx == numRows or dict_idx == -1:
                flag *= -1
                dict_idx += flag * 2

            if numRows == 1:
                dict_idx = 0

            cnt += 1
            idx += 1
        
        for i in range(numRows):
            answer += ''.join(dictionary[i])
        return answer


        # 0 1 2 3 2 1 0 1 2 3 2 1 0 .... 

        
        