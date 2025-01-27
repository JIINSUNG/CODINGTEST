class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dictionary = {}

        for i in range(len(s)):
            # s[i]가 사전에 없는 경우
            if s[i] not in dictionary:
                dictionary[s[i]] = t[i]
            else:
                if dictionary[s[i]] != t[i]:
                    return False
        
        diction = []
        for value in dictionary.values():
            diction.append(value)
        
        return len(dictionary) == len(set(diction))
        
 

    