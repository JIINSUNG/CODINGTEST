from collections import defaultdict

class NumberContainers:

    def __init__(self):
        self.idx_value = { 1 : 10} # { idx : value }
        
        self.value_idx = defaultdict(list) # {10 : heap : [idx1, idx2, ...]}

        self.check_avail = defaultdict(lambda: defaultdict(bool)) # { 10 : {1 : False, 2 : True}}

    def change(self, index: int, number: int) -> None:
        if index in self.idx_value:
            self.check_avail[self.idx_value[index]][index] = False # 이전 인덱스 유효성을 False로 변경
        
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

        
# ["NumberContainers", "find", "change", "change", "change", "change", "find", "change", "find"]
# [[], [10], [2, 10], [1, 10], [3, 10], [5, 10], [10], [1, 20], [10]]

# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)