class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
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
                return result
            else:
                return []



        
        return topology(graph, indegree)
        