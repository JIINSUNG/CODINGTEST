class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        graph = defaultdict(set)
        indegree = {}
        answer = []
        queue = deque()

        for i in range(len(recipes)):
            for ingredient in ingredients[i]:
                graph[ingredient].add(recipes[i])
            indegree[recipes[i]] = len(ingredients[i])
        
        for supply in supplies:
            queue.append(supply)

        while queue:
            ingredient = queue.popleft()

            for recipe in graph[ingredient]:
                indegree[recipe] -= 1

                if indegree[recipe] == 0:
                    answer.append(recipe)
                    queue.append(recipe)
        return answer 
                


