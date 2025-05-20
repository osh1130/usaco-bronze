#fin = open('Geometry/mowing_bronze_jan16/3.in','r')
fin = open('mowing.in','r')
fout = open('mowing.out','w')
N = int(fin.readline())
grid = [[-1]*2001 for _ in range(2001)]
# instructions = [input().split() for _ in range(N)]
directions = {
        'N': (0, 1),
        'E': (1, 0),
        'S': (0, -1),
        'W': (-1, 0)
    }
x, y = 1000, 1000
t=0
min_diff = float('inf')
grid[x][y] = 0
for i in range(N):
    line = fin.readline().split()
    D = line[0]          
    S = int(line[1])
    dx, dy = directions[D]
    for _ in range(S):
            t += 1
            x += dx
            y += dy
            if grid[x][y] != -1:
                diff = t - grid[x][y]
                if diff < min_diff:
                    min_diff = diff
            grid[x][y] = t
        
#print(-1 if min_diff == float('inf') else min_diff)
fout.write(str(-1 if min_diff == float('inf') else min_diff))