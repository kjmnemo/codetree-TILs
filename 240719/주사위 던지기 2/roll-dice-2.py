n, m = map(int, input().split())

def dfs(cnt, result):
    if cnt == n and sum(result)==m:
        print(*result)
        return
    for i in range(1,7):
        if sum(result) + i + cnt - n > m:
            continue
        else:
            dfs(cnt+1, result+[i])

dfs(0,[])