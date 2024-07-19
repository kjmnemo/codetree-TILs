'''
N개의 발의 높낮이가 너무 엉망진창이라 일정구간만이라도 고르게
낮은 밭의 높이를 1올때, 낮출때 > 소모되는 비용 1로 동일
N개의 밭의 높이가 주어지면 
연속하게 최소 T번이상 H높이로 나오게끔 하려고 할떄 
> 필요한 최소비용
'''

n, h, t = map(int, input().split())
nlst = list(map(int, input().split()))

ans = int(1e9)
for i in range(n-t+1):
    tmp = 0
    for j in nlst[i:i+t]:
        tmp += abs(j-h)
    ans = min(tmp, ans)
print(ans)