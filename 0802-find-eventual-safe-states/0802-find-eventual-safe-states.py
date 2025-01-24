class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # n개의 노드로 구성된 방향 그래프가 주어질때 (0 - n-1 까지의 노드번호가 적힌)
        # graph[i]는 노드 i의 인접 노드를 나타낸다
        # 나가는 간선이 없을때 해당 노드는 터미널 노드라고 칭한다
        # 노드는 안전한 노드라고 칭한다, 
        # 해당 노드에서 시작하는 모든 가능한 경로가 터미널 노드(또는 다른 안전 노드)로 연결되는 경우

        def check_safe(node, visited):
            
            queue = deque([node])
            visited[node] = True

            while queue:
                v = queue.popleft()
                visited[v] = True

                for s in graph[v]:

                    # 이미 방문했다면 사이클 발생한 것
                    if visited[s]:
                        return False
                    
                    queue.append(s)
                    visited[s] = True
                
            
            return True
                    

                    
                




        answer = []
        for i in range(len(graph)):
            visited = [False] * len(graph)
            if check_safe(i, visited):
                answer.append(i)
        return answer
