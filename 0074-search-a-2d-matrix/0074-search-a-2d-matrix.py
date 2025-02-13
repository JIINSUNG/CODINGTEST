class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 각 행은 오름차순 메트릭스가 주어짐 
        
        # 각 행의 첫 정수는 이전 행의 마지막 정수보다 크다

        # solution.
        # target이 속할 행을 찾는다
        # 이분탐색으로 target을 찾는다
        
        def bisect_search(arr, target):
            left = 0
            right = len(arr) - 1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] == target:
                    return True

                elif arr[mid] < target:
                    left = mid + 1 

                else:
                    right = mid - 1
            return False

        for arr in matrix:
            if target <= arr[-1]:
                return bisect_search(arr, target)
        return False
        

