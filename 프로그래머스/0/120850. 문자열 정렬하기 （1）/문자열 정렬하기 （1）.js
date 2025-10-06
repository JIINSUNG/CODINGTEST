function solution(my_string) {
    var answer = [];
    
    
    return my_string.match(/\d/g).map(Number).sort((a,b) => a-b)
}