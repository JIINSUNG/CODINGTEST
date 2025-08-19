function solution(n) {
    var answer = 0;
    let cnt = (n.toString(2).match(/[1]/g) ?? []).length
    while(true){
        n++;
        if((n.toString(2).match(/[1]/g) ?? []).length === cnt){
            return n
        }
    }
    // return answer;
}