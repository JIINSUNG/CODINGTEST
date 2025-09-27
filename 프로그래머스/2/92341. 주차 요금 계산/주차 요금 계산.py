from collections import defaultdict
import math 

def solution(fees, records):
    answer = []

    defaultTime = fees[0]
    defaultPrice = fees[1]
    unitTime = fees[2]
    unitPrice = fees[3]
    
    totalParkTime = defaultdict(int)
    currentParkTime = defaultdict(int)
    
    for record in records:
        time, carNumber, types = record.split(" ")
        minute_of_time = int(time.split(":")[0])*60 + int(time.split(":")[1])
        
        if types == "IN":
            currentParkTime[carNumber] = minute_of_time
            
        elif types == "OUT":
            parkTime = minute_of_time - currentParkTime[carNumber]
            totalParkTime[carNumber] +=  parkTime
            del currentParkTime[carNumber]
        
    maxTime = 23* 60 + 59
    for carNumber, time in currentParkTime.items():
        totalParkTime[carNumber] += maxTime - time
    
    
    def calculatePrice(time) :
        price = 0
        price += defaultPrice
        
        if time - defaultTime > 0:
            price += math.ceil((time-defaultTime) / unitTime) * unitPrice
        return price

    for key in sorted(totalParkTime.keys()):
        answer.append(calculatePrice(totalParkTime[key]))
    
    return answer