class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        graph = {}
        indegree = {}
        answer = []
        queue = deque()
        
        for i in range(len(recipes)):
            graph[recipes[i]] = ingredients[i]
            indegree[recipes[i]] = len(ingredients[i])

        for supply in supplies:
            queue.append(supply)

        while queue:
            ingredient = queue.popleft()

            for key in graph.keys():
                if ingredient in graph[key]:
                    indegree[key]-= 1
                    if indegree[key] == 0:
                        answer.append(key)
                        queue.append(key)
        return answer 
                


        # print(graph)
