n = int(input())
nlst = list(map(int, input().split()))

ans = int(1e9)

for i in range(n):
    alst = nlst[:]
    alst[i] = alst[i]*2
    blst = alst[:]
    for j in range(n):
        dlst = blst[:]
        c = dlst[j]
        dlst.remove(c)
        tmp = 0
        for k in range(n-2):
            tmp += abs(dlst[k]-dlst[k+1])
        ans = min(tmp, ans)

print(ans)