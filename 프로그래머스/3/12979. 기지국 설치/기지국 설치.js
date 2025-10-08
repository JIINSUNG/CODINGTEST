

function solution(n, stations, w) {
    let answer = 0;
    
    // 현재 미커버중인 지역 중 가장 낮은 번호
    let noCover = 1
    
    for(let i=0; i<stations.length; i++){
        // 현재 커버중인 지역
        const cover = stations[i]
        
        // 현재 중계기가 설치된 지역 왼쪽 중 가장 큰 번호
        const largeCover = cover-w-1
        
        if(largeCover >= noCover){
            answer += Math.ceil((largeCover - noCover + 1) / (2*w+1) )
        }
        
        noCover = stations[i] + w + 1
    }
    
    if (noCover <= n){
        answer += Math.ceil((n - noCover + 1) / (2*w+1))
    }
    
    return answer    
}