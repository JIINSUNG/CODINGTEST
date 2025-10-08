function solution(genres, plays) {
    var answer = [];
    
    const playMap = {}
    
    const idxMap = {}
    
    for (let i=0; i< genres.length; i++){
        playMap[genres[i]] = (playMap[genres[i]] || 0) + plays[i]
        
        if(!idxMap[genres[i]]){
            idxMap[genres[i]] = []
        }
        
        idxMap[genres[i]].push([plays[i], i])
    }
    const sortedPlayList = Object.entries(playMap).sort((a, b) => b[1] - a[1])
    
    for (const group of sortedPlayList){
        const targetArr = idxMap[group[0]]
        targetArr.sort((a, b) => {
            // 빈도수가 같다면 인덱스번호가 낮은순으로
            if(a[0] == b[0]){
                return a[1] - b[1]
            } // 그 이외에는 재생 횟수가 많은 순
            else{
                return b[0] - a[0]
            }
        })
        
        for(let i=0; i<2; i++){
            if(targetArr.length === 0){
                break
            }
            const target = targetArr.shift()
            answer.push(target[1])
        }
    }
    
    
        
    
    return answer;
}