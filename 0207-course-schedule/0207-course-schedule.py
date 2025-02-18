class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 들어야 할 강의의 총 개수 numCourses 

        # [a, b] <- 코스 a를 듣기 위해선 b를 반드시 수강할 것
        # 강의를 모두 들을 수 있다면 True, 불가능 하다면 False
        
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for v1, v2 in prerequisites:
            graph[v2].append(v1)
            indegree[v1] += 1
        
        def topology(graph, indegree):
            result = []
            pq = deque()
            
            for i in range(numCourses):
                if indegree[i] == 0:
                    pq.append(i)
            
            while pq:
                v = pq.popleft()
                result.append(v)
                for neighbor in graph[v]:
                    indegree[neighbor] -= 1
                    
                    if indegree[neighbor] == 0:
                        pq.append(neighbor)
                
            if len(result) == numCourses:
                return True
            return False



        
        return topology(graph, indegree)



        # def topology():


