function solution(begin, target, words) {
    var answer = 1000000;
    const visited = new Set()
    visited.add(begin)
    
    // 1. 현재 단어를 이용해 한글자만 변경하면 변경할 수 있는 단어들을 words에서 찾는다
    // 2. 이때 target으로 바꿀 수 있다면 바로 리턴
    // 3. 이미 변환하지 않은 단어중 가능한 단어를 모두 큐에 집어넣음
    

    
    const isCanChange = (str1, str2) => {
        // 같은 단어라면 변경할 필요가 없음
        if(str1 === str2){
            return false
        }
        
        let cnt = 0
        
        for(let i=0; i<str1.length; i++){
            if(str1.at(i) !== str2.at(i)){
                cnt += 1
            }
            
            if(cnt >= 2){
                return false
            }
        }
        
        return cnt === 1
    }
    
    const bfs = (depth, current) => {
        const queue = [[current, depth]]
        while (queue.length > 0){
            const [cword, depth] = queue.shift()
            if(cword === target){
                answer = Math.min(answer, depth)
                break
            }
                
            
            for (const w of words){
                if(!visited.has(w) && isCanChange(cword, w)){
                    queue.push([w, depth+1])
                    visited.add(w)
                }
            }
        }
    }
    
    
    
    bfs(0, begin)


    return answer === 1000000 ? 0 : answer
}