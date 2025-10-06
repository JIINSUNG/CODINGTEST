function solution(rsp) {
    var answer = '';
    
    
    for (const char of rsp){
        if (char === "2"){
            answer += "0"
        }
        else if (char === "0"){
            answer += "5"
        } else if (char === "5"){
            answer += "2"
        }
    }
    
    return answer;
}