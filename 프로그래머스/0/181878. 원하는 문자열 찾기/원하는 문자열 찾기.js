function solution(myString, pat) {
    var answer = 0;
    return myString.toLowerCase().includes(pat.toLowerCase()) ? 1 : 0;
}