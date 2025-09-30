function solution(s1, s2) {
    var answer = 0;
    
    const wordSet = new Set()
    
    for (const word of s1){
        wordSet.add(word)
    }
    
    for (const word of s2){
        wordSet.add(word)
    }
    
    return (s1.length + s2.length) - wordSet.size
}