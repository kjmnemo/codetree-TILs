a,b,c = map(int, input().split())
ans = -int(1e9)
i = -1
tmp = 0
while a*i <= c:
    i += 1
    j = -1
    while True:
        j += 1
        tmp = a*i + b*j
        if tmp > c:
            break
        else:
            #print(i,j)
            ans = max(tmp,ans)

print(ans)