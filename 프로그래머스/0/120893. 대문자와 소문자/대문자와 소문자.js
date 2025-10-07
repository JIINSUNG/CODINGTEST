function solution(my_string) {
    var answer = '';
    
    for (const char of my_string){
        if(char >= 'a' && char <= 'z'){
            answer += char.toUpperCase()
        }else{
            answer += char.toLowerCase()
        }
    }
    
    return answer;
}