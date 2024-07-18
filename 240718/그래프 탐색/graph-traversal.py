'''
n개의 정점과 m개의 간선으로 이루어진 양방향 그래프
1번 정점에서 시작하여, 주어진 간선을 따라 도달
> 도달할 수 있는 서로 다른 정점의 수 (1번은 제외)
'''
n, m = map(int, input().split())
arr = [[0]*n for _ in range(n)]
for _ in range(m):
    x,y = map(int, input().split())
    arr[x-1][y-1] = 1
    arr[y-1][x-1] = 1

visit = set()

def dfs(start):
    global visit

    for i in range(n):
        if arr[start][i] == 1:
            arr[start][i] -= 1
            visit.add(i)
            dfs(i)
    else:
        return

dfs(0)
print(len(visit)-1)
#print(visit)