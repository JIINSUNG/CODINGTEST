from collections import defaultdict
import heapq

class NumberContainers:

    def __init__(self):
        self.idx_value = {}  
        self.value_idx = defaultdict(list) 
        self.check_avail = defaultdict(lambda: defaultdict(bool)) 

    def change(self, index: int, number: int) -> None:
        if index in self.idx_value:
            old_number = self.idx_value[index]
            self.check_avail[old_number][index] = False
        
        self.idx_value[index] = number
        self.check_avail[number][index] = True
        heapq.heappush(self.value_idx[number], index)

    def find(self, number: int) -> int:
        if not self.value_idx[number]:
            return -1
        
        while self.value_idx[number]:
            idx = heapq.heappop(self.value_idx[number])
            if self.check_avail[number][idx]:  
                heapq.heappush(self.value_idx[number], idx)  
                return idx
        
        return -1
