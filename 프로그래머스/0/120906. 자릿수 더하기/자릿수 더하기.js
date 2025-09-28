function solution(n) {
    let answer = 0
    for (const char of String(n)){
        answer += +char
    }
    return answer
}