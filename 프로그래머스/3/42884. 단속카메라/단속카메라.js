function solution(routes) {
    var answer = 0;
    
    let dist = -30001
    
    routes = routes.sort((a, b) => (a[0] - b[0], a[1] - b[1]))
    

    for (const route of routes){
        if(route[0] <= dist){
            continue
        }else{
            answer += 1
            dist = route[1]
        }
    }
    
    
    
    return answer;
}