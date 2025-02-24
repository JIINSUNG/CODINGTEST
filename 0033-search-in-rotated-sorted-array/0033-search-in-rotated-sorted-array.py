class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 오름차순으로 정렬된 정수 배열 숫자가 있습니다 (따라서 고유한 값이 있습니다).

        # 함수로 전달되기 전에, nums는 알려지지 않은 피벗 인덱스 k (1 <= k < nums.length)에서 회전될 수 있으며, 
        # 그 결과 배열은 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1] (0-indexed)가 됩니다. 예를 들어, [0,1,2,4,5,6,7]은 피벗 인덱스 3에서 회전되어 [4,5,6,7,0,1,2]가 될 수 있습니다.

        # 가능한 회전 후 배열 수와 정수 타겟이 주어졌을 때, 타겟의 인덱스가 숫자로 되어 있으면 반환하고, 숫자로 되어 있지 않으면 -1로 반환합니다.
        # 실행 시간 복잡도가 O(log n)인 알고리즘을 작성해야 합니다.
        
        if target in nums:
            return nums.index(target)
        else:
            return -1