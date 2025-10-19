function solution(arr) {
    var answer = [];
    
    for (const num of arr){
        if (num >= 50 && num % 2 === 0){
            answer.push(parseInt(num/2))
        } else if (num < 50 && num % 2 === 1){
            answer.push(num * 2)
        }
        else{
            answer.push(num)
        }
    }
    return answer;
}