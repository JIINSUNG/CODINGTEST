def solution(s1, s2):
    wordSet = set()
    for word in s1:
        wordSet.add(word)
    for word in s2:
        wordSet.add(word)
    return len(s1) + len(s2) - len(wordSet)