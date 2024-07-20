n = int(input())
r1, c1, r2, c2 = map(int, input().split())

arr = [[0]*n for _ in range(n)]
v = [[0]*n for _ in range(n)]

from collections import deque

def bfs(si,sj):
    q = deque()
    q.append((si,sj))
    v[si][sj] = 1

    while q:
        ci, cj = q.popleft()
        for di, dj in ((1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<n and 0<=nj<n and v[ni][nj]==0:
                q.append((ni,nj))
                v[ni][nj] = 1
                arr[ni][nj] = arr[ci][cj]+1
                if ni ==r2-1 and nj == c2-1:
                    return arr[ni][nj]
    return -1

print(bfs(r1-1,c1-1))