n = int(input())
abclst = []
for _ in range(n):
    a,b,c = map(int,input().split())
    abclst.append((a-1,b-1,c-1))

ans = -int(1e9)

for i in range(3):
    tmp = 0
    cuplst = [0]*3
    cuplst[i] = 1
    for a,b,c in abclst:
        cuplst[a],cuplst[b] = cuplst[b], cuplst[a]
        if cuplst[c] == 1:
            #print(cuplst,(a,b,c))
            tmp +=1
    
    ans = max(ans, tmp)

print(ans)