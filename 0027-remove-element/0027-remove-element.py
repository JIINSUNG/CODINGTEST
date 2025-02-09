class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        pq = []
        k = 0
        for i in range(len(nums)-1, -1, -1):
            
            if nums[i] == val:
                k += 1
                if pq:
                    idx = -heapq.heappop(pq)
                    nums[i], nums[idx] = nums[idx], nums[i]
                    heapq.heappush(pq, -i)
    
            else:
                heapq.heappush(pq, -i)
        return len(nums)-k
        
        


