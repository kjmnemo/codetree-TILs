'''
n개의 줄이 있다. 각각의 줄로 들수 있는 최대 무게 wi
2개 이상의 줄을 같이 사용하게 되면
사용하는 줄의 수가 k, 무게 W를 달았을 때 > 각각의 줄에는 W/k 만큼의 중량
줄을 적절하게 사용하여 들 수 있는 최대 무게
'''

n = int(input())
klst = []
for _  in range(n):
    k = int(input())
    klst.append(k)

klst.sort()
num = 1
ans = 0

for i in klst[::-1]:
    tmp = i*num
    if tmp > ans:
        ans = tmp
    else:
        print(ans)
        break
    num += 1