function solution(n)
{
    const str = String(n)
    let answer = 0
    for (const s of str){
        answer += Number(s)
    }
    return answer
}