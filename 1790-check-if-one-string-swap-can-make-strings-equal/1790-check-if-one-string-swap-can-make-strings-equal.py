class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        # 길이가 같은 두 문자열 s1과 s2가 주어진다.
        # 문자열 교환 : 문자열에서 두 개의 인덱스(반드시 다를 필요는 없음)를 선택 후 문자를 바꾸는 작업
        # 문자열 중 정확히 하나에 대해 최대 하나의 문자열 교환을 수행하여 두 문자열을 동일하게 만드는 것이 가능하면 true를 반환. 
        # 그렇지 않으면 false를 반환합니다.
        if s1 == s2:
            return True
        
        index = [] 
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                index.append(i)
        
        if len(index) > 2 or len(index) <= 1:
            return False
        
        s2 = list(s2)
        print(s2)
        s2[index[0]], s2[index[1]] = s2[index[1]], s2[index[0]]
        s2 = ''.join(s2)
        return s1 == s2
        
            
