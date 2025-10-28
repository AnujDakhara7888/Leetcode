class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count=0
        dir = ((-1,0),(1,0),(0,-1),(0,1))
        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    count+=1
                    queue = deque()
                    queue.append((i,j))
                    grid[i][j]='0'
                    while queue:
                        x,y = queue.popleft()
                        for dx,dy in dir:
                            nx,ny=x+dx,y+dy
                            if nx<0 or ny<0 or nx>=len(grid) or ny>=len(grid[0]) or grid[nx][ny]=='0':
                                continue
                            grid[nx][ny]='0'
                            queue.append((nx,ny))


        return count

                        




        