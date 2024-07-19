'''
n개의 숫자가 주어지고, 그 숫자를 적절하게 골라
더했을 때 carry가 전혀 발생하지 않는 > 최대로 고를 수 있는 숫자의 개수
carry = 수와 수를 더했을 때 10이 자리를 넘기는 것
각 자릿수를 모두 각각 더했을 때, 10이상이 되는 경우가 전혀 없어야
'''
n = int(input())
alst = []
for _ in range(n):
    a = int(input())
    alst.append(a)
alst.sort()
ans = 0
def dfs(cnt, result, tmp):
    global ans
    nwresult = result[:]
    if cnt == n:
        #print(result)
        ans = max(tmp, ans)
        return
    a = 0
    for i in str(alst[cnt])[::-1]:
        nwresult[a] += int(i)
        a += 1

    flag = False
    for j in nwresult:
        if j > 9:
            flag = True
            break
    if flag :
        dfs(cnt+1, result, tmp)
    else:
        dfs(cnt+1, nwresult, tmp+1)

dfs(0, [0]*10, 0)
print(ans)