class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        self.parents = [i for i in range(n)]


                    
        def find(x):
            if self.parents[x] != x:
                self.parents[x] = find(self.parents[x])
            return self.parents[x]

        def union(a, b):
            a = find(a)
            b = find(b)

            if a < b:
                self.parents[b] = a
            else:
                self.parents[a] = b
        for a,b in edges:
            union(a, b)
        return find(source) == find(destination)