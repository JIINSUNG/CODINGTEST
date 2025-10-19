function solution(number) {
    let answer = 0
    for (const num of number){
        answer += parseInt(num)
    }
    return answer % 9
}