def gridDfs(grid):
    visited={}
    maxi=0
    n=len(grid)
    m=len(grid[0])
    for i in range(0,len(grid)):
        for j in range(0,len(grid[0])):
            if visited.get((i,j))==None:
                stack=[]
                stack.append((i,j))
                visited[(i,j)]=1
                while stack:
                    r,c=stack.pop()
                    for r,c in [(r-1,c),(r+1,c),(r,c+1),(r,c-1)]:
                        if (0<=r<n) and (0<=c<m) and grid[r][c]==1 and visited.get((r,c))==None:
                            stack.append((r,c)) 
                            visited[(r,c)]=1
                
    return 0
