#단지번호
import sys

def dfs(x, y, N, grid):
    if x < 0 or x >= N or y < 0 or y >= N:
        return 0
    
    if grid[x][y] == 1:
        grid[x][y] = 0
        count = 1
        #bible
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]

        for i in range(4):
            count += dfs(x+dx[i],y+dy[i], n, grid)
        return count
    
    return 0

n = int(input())
#bible
grid_map = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]

result = []

for i in range(n):
    for j in range(n):
        size = dfs(i,j,n,grid_map)
        if size > 0:
            result.append(size)
            
result.sort()
print(len(result))
for r in result:
    print(r)
