function solution(arr) {
    var answer = [0, 0];
    const n = arr.length
    const m = arr[0].length
    
    // 쿼드트리 압축 방식
    // 어떤 영역 S를 압축한다할때
    // S내부에 있는 모든 수가 같은 값이라면 S를 하나로 압축시킨다
    // 모든 수가 같지 않다면 4개의 균일한 정사각형 영역으로 쪼갠 뒤 각 정사각형 영역에 대해 같은 방식의 압축을 시도한다
    
    
    // 먼저 S의 모든 요소가 같은 숫자로 이뤄져있는지 체크한다
    
    const divideConquer = (x, y, size) => {
        const target = arr[x][y]
        let isSame = true
        for(let i= x; i< x + size; i++){
            for (let j= y; j< y + size; j++){
                if(arr[i][j] !== target){
                    isSame = false
                    break
                }
            }
        }
        
        // 모든 요소가 같은 경우
        if(isSame){
            answer[target] += 1
            return   
        }
        
        // 하나라도 다른 경우가 있으면 divide conquer 진행
        
        divideConquer(x, y, size/2)
        divideConquer(x+size/2, y, size/2)
        divideConquer(x, y+size/2, size/2)
        divideConquer(x+size/2, y+size/2, size/2)
        
    }
    
    divideConquer(0, 0, n)
    
    
    
    
    
    
    return answer;
}