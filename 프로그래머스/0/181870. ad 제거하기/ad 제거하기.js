function solution(strArr) {
    var answer = [];
    
    for (const word of strArr){
        if (word.includes("ad")){
            continue
        }
        answer.push(word)
    }
    return answer;
}