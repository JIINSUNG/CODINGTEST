function solution(sides) {
    var answer = 0;
    
    // 가장 긴 변의 길이는 다른 두변의 길이의 합보다 작다
    sides = sides.sort((a,b) => a-b)
    
    
    
    
    return sides[2] < sides[0] + sides[1] ? 1 : 2
}