function solution(a, b) {
    var answer = 0;
    if (a%2 === 0 && b % 2 === 0){
        return Math.abs(a-b)
    }else if (a%2 === 0 || b % 2 === 0){
        return 2 * (a + b )
    }else {
        return a**2 + b **2
    }
}