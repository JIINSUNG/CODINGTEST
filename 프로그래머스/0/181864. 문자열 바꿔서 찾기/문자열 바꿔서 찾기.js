function solution(myString, pat) {
    var answer = 0;
    
    myString = myString.replaceAll('A', 'C').replaceAll('B','A').replaceAll('C','B')
    return  myString.includes(pat) ? 1 : 0
    
}