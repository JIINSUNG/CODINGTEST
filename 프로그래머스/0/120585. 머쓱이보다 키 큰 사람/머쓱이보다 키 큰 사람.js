function solution(array, height) {
    let answer = 0
    array = array.sort((a, b) => b-a)
    
    
    for(let i=0; i< array.length; i++){
        if (array[i] > height){
            answer += 1
        }
    }
    return answer
    
}