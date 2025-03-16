class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def can_repair(time):
            return sum(int((time // r) ** 0.5) for r in ranks) >= cars
        
        left, right = 0, min(ranks) * cars * cars
        while left < right:
            mid = (left + right) // 2
            if can_repair(mid):
                right = mid
            else:
                left = mid + 1
        
        return left