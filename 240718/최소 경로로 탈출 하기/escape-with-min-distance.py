n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
# 뱀이 없는 경우 1, 뱀이 있는 경우 0 / 1를 지나가야함
# 좌측상단 > 우측하단 - 이동가능한 경로 중 최단거리 출력 (불가능이면 -1)

from collections import deque

def bfs(si,sj):
    global arr
    q = deque()
    q.append((si,sj))
    v[si][sj] = 1

    while q:
        ci, cj = q.popleft()
        for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<n and 0<=nj<m and v[ni][nj]==0 and arr[ni][nj]!=0:
                q.append((ni,nj))
                arr[ni][nj] = arr[ci][cj]+1
                v[ni][nj] = 1

v = [[0]*m for _ in range(n)]
bfs(0,0)
if arr[n-1][m-1] == 1:
    print(-1)
else:
    print(arr[n-1][m-1]-1)