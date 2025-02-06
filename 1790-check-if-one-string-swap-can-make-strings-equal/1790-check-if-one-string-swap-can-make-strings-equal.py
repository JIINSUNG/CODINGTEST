class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        # 길이가 같은 두 문자열 s1과 s2가 주어진다.
        # 문자열 교환 : 문자열에서 두 개의 인덱스(반드시 다를 필요는 없음)를 선택 후 문자를 바꾸는 작업
        # 문자열 중 정확히 하나에 대해 최대 하나의 문자열 교환을 수행하여 두 문자열을 동일하게 만드는 것이 가능하면 true를 반환. 
        # 그렇지 않으면 false를 반환합니다.
        if s1 == s2:
            return True

        # 다른 문자의 인덱스를 저장
        index = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                index.append(i)

        # 다른 문자가 2개가 아니면 False 반환
        if len(index) != 2:
            return False

        i, j = index
        return s1[i] == s2[j] and s1[j] == s2[i]
        
            
