function solution(fees, records) {
    var answer = [];
    
    const defaultTime = fees[0]
    const defaultPrice = fees[1]
    const unitTime = fees[2]
    const unitPrice = fees[3]
    
    
    // 차량별 누적 주차시간 정보 
    const totalParkMap = {}
    
    // 주차된 차량정보 
    const currentParkMap = {}
    
    
    
    for(const record of records){
        const [time, carNumber, type] = record.split(' ')
        
        let parkTime = +time.split(":")[0] * 60 + +time.split(":")[1]
        if(type === "IN"){
            // 입차라면 parkMap에 시간 저장
            currentParkMap[carNumber] = parkTime
        }
        
        if(type === "OUT"){
            // 출차라면 주차한 총 시간 계산
            const totalParkTime = parkTime - currentParkMap[carNumber]
            totalParkMap[carNumber] = (totalParkMap[carNumber] || 0) + totalParkTime
            delete currentParkMap[carNumber]
        }
        
    }
    
    const maximumTime = 23*60 + 59
    for (const [carNumber, time] of Object.entries(currentParkMap)){
        totalParkMap[carNumber] = (totalParkMap[carNumber] || 0) + maximumTime - time
    }
    
    const calculatePrice = (time) => {
        let price = 0
        
        // 기본 요금 부과
        price += defaultPrice
        
        if(time - defaultTime > 0){
            price += Math.ceil((time-defaultTime) / unitTime) * unitPrice
        }
        return price
    }
    
    
    for(const carNum of Object.keys(totalParkMap).sort((a, b) => a-b)){
        const price = calculatePrice(totalParkMap[carNum])
        answer.push(price)
    }
    
    return answer;
}