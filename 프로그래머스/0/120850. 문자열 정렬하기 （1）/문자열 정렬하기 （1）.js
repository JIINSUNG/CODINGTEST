function solution(my_string) {
    var answer = [];
    
    
    return my_string.match(/[0-9]/g).map(Number).sort((a,b) => a-b)
}