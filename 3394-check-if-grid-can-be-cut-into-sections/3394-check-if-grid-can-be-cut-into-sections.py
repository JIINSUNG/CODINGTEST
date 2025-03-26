class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        n = len(rectangles)
        
        def is_can(direction):
            rectangles.sort(key = lambda x : x[direction])

            last_end = rectangles[0][direction+2]
            cnt = 0

            for rectangle in rectangles[1:len(rectangles)]:
                # 시작점을 가져온다
                if rectangle[direction] >= last_end:
                    cnt += 1

                last_end = max(last_end, rectangle[direction+2])
            
            if cnt >= 2:
                return True

            return False
        
        return is_can(0) or is_can(1) 
            

