class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        adj = defaultdict(list)
        degree=[0]*numCourses
        for a, b in prerequisites:
            adj[b].append(a)
            degree[a]+=1
        q = deque([i for i in range(numCourses) if degree[i] == 0])
        order=[]
        while q:
            p = q.popleft()
            order.append(p)
            for v in adj[p]:
                degree[v]-=1
                if degree[v]==0:
                    q.append(v)

        return order if len(order) == numCourses else []

        

        