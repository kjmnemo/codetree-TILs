'''
양 끝쪽에 있는 사람 중  한 사람을 선택해
항상 남은 두 사람 사이로 이동시켜
결국 세 사람이 서 있는 위치가 연속된 숫자가 되도록
> 최소 이동횟수, 최대 이동 횟수
'''

lst = sorted(list(map(int, input().split())))
ans = []

a = lst[0]
b = lst[1]
c = lst[2]

if abs(a-b)==1 and abs(b-c) == 1:
    print(0)
elif abs(a-b) ==2 or abs(b-c) ==2:
    print(1)
else:
    print(2)

ans = 0
b = set()
def dfs(alst,m):
    alst = sorted(alst)
    #print(alst,m)
    a1 = alst[0]
    a2 = alst[1]
    a3 = alst[2]
    global ans

    if abs(a1-a2)==1 and abs(a2-a3)==1:
        ans = max(ans,m)
        return

    if abs(a2-a3) > 1:
        if (a2,a3) in b:
            return
        else:
            for j in (a2+1,a3-1):
                nlst = [a2,a3] + [j]
                b.add((a2,a3))
                dfs(nlst, m+1)

    if abs(a1-a2) > 1:
        if (a1,a2) in b:
            return
        for j in (a1+1,a2-1):
            nlst = [a1,a2] + [j]
            b.add((a1,a2))
            dfs(nlst, m+1)

dfs(lst,0)
print(ans)