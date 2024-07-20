k, N = map(int, input().split())

klst = [i for i in range(1,k+1)]

def dfs(n, alst):
    if n == N:
        print(*alst)
        return

    for j in klst:
        if len(alst)>=2:
            if alst[-1]==j and alst[-2]==j:
                continue
        dfs(n+1, alst+[j])
dfs(0,[])