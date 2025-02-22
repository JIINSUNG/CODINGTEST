class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # k번째로 큰 수 구하기, nums배열 정렬 없이 구할 것
        pq = []

        for num in nums:
            heapq.heappush(pq, -num)
        
        for _ in range(k-1):
            num = heapq.heappop(pq)

        return -heapq.heappop(pq)