n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

ans = 0
for i in range(n-2):
    for j in range(n-2):
        tmp = 0
        for p in range(3):
            for q in range(3):
                tmp += arr[i+p][j+q]
        ans = max(tmp, ans)

if n == 3:
    ans = 0
    for p in range(3):
        for q in range(3):
            ans += arr[p][q]

print(ans)