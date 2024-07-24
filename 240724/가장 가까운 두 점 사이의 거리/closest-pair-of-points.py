n = int(input())
xylst = []
for _ in range(n):
    x,y = map(int, input().split())
    xylst.append((x,y))

ans = int(1e9)
for i in range(n):
    x1,y1 = xylst[i]
    for j in range(i+1,n):
        x2,y2 = xylst[j]
        tmp =  abs((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2) )
        ans = min(ans, tmp)

print(ans)