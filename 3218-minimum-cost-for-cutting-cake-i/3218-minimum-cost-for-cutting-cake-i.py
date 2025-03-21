class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        # 1 x 1 조각으로 잘라야 하는 m x n 케이크가 있습니다.
        # 정수 m, n, 그리고 두 개의 배열이 주어집니다:
        # 크기 m - 1의 수평 절단, 여기서 수평 절단[i]은 수평선 i를 따라 절단하는 비용을 나타냅니다.
        # 크기 n - 1의 수직 절단, 여기서 수직 절단[j]은 수직선 j를 따라 절단하는 비용을 나타냅니다.
        # 한 번의 작업으로 아직 1 x 1 정사각형이 아닌 케이크 조각을 선택하고 다음 중 하나의 컷을 수행할 수 있습니다:
        # 가로줄 i를 따라 자르면 가로줄 [i]의 비용이 듭니다.
        # 수직선 j를 따라 수직 절단 비용을 지불하고 절단하세요 [j].
        # 절단 후 케이크 조각은 두 개의 뚜렷한 조각으로 나뉩니다.
        # 절단 비용은 라인의 초기 비용에만 의존하며 변경되지 않습니다.
        # 케이크 전체를 1 x 1 조각으로 자르려면 최소 총 비용을 반환하세요.

        # 비용이 낮은 걸로 자른다?
        horizontalCut.sort()
        verticalCut.sort()
        
        # Priority Queue 초기화
        pq = []
        
        # 초기 케이크 조각 크기
        h, v = m, n
        
        for cut in horizontalCut:
            heapq.heappush(pq, (cut, 'h'))

        for cut in verticalCut:
            heapq.heappush(pq, (cut, 'v'))
        
        # 총 비용 초기화
        total_cost = 0
        
        # 모든 절단을 처리할 때까지 반복
        while pq:
            cost, direction = heapq.heappop(pq)
            
            if direction == 'h':
                # 수평 절단
                total_cost += cost * v
                h -= 1
            else:
                # 수직 절단
                total_cost += cost * h
                v -= 1
        
        return total_cost