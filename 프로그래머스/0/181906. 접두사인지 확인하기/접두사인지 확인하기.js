function solution(my_string, is_prefix) {
    const strMap = {}
    var answer = 0;
    let before = ''
    for(const char of my_string){
        before += char
        strMap[before] = 1
    }
    
    return strMap[is_prefix] ? 1 : 0;
}