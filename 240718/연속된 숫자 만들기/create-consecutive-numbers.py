'''
양 끝쪽에 있는 사람 중  한 사람을 선택해
항상 남은 두 사람 사이로 이동시켜
결국 세 사람이 서 있는 위치가 연속된 숫자가 되도록
> 최소 이동횟수, 최대 이동 횟수
'''

lst = sorted(list(map(int, input().split())))
ans = []

def dfs(alst,m):
    #print(alst)
    alst = sorted(alst)
    a1 = alst[0]
    a2 = alst[1]
    a3 = alst[2]
    global ans

    if abs(a1-a2)==1 and abs(a2-a3)==1:
        ans.append(m)
        return

    if abs(a2-a3) > 1:
        for j in range(a2+1,a3):
            nlst = [a2,a3] + [j]
            dfs(nlst, m+1)

    if abs(a1-a2) > 1:
        for j in range(a1+1,a2):
            nlst = [a1,a2] + [j]
            dfs(nlst, m+1)

dfs(lst,0)
print(min(ans))
print(max(ans))