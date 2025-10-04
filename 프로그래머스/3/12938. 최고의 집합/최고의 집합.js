function solution(n, s) {
    if (s < n) return [-1]
    const answer = []
    const q = parseInt(s/n)
    const r = parseInt(s%n)
    
    for (let i=0; i < n-r; i++){
        answer.push(q)
    }
    
    for (let i=0; i< r; i++){
        answer.push(q+1)
    }
    
    return answer
    
}