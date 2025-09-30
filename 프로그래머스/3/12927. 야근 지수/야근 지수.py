import heapq

def solution(n, works):
    totalPatigues = 0
    maxHeap = []
    
    for work in works:
        maxHeap.append(-work)
        totalPatigues += work**2
    heapq.heapify(maxHeap)
    
    for _ in range(n):
        # 가장 비용이 비싼 work를 꺼낸다
        work = heapq.heappop(maxHeap)
        
        # 최대힙으로 만들기 위해 -를 했으므로 다시 양수로 바꿈
        work = -work
        
        # 만약 현재 꺼낸 가장 비용이 비싼 work가 0이라면 모든 업무 처리한 것이니 0으로 리턴
        if work <= 0:
            return 0
        
        # 현재 작업했던 비용을 전체 피로도에서 감소
        totalPatigues -= (work) ** 2
        
        # 현재 작업을 1만큼 진행시킴
        work -= 1
        
        # 현재 비용만큼을 전체 피로도에 추가
        totalPatigues += (work) ** 2
        heapq.heappush(maxHeap, -work)

    
    
    return totalPatigues