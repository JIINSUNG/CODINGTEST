function solution(food) {
    let foodString = ""
    for (let i= 1; i<= food.length; i++){
        const count = Math.floor(food[i] /2)
        
        foodString += String(i).repeat(count)
        
    }
    
    
    return foodString + "0" + foodString.split('').reverse().join('')
}