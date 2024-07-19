'''
N개의 수 들중 정확히 2개를 제외하여
남은 N-2개의 숫자들의 합이 s와 최대한 가까워지도록
>>> 숫자의 합 - S
'''

n, s = map(int, input().split())
alst = list(map(int, input().split()))

from itertools import combinations
blst = list(combinations(alst,n-2))
ans = 200
for j in blst:
    tmp = abs(s - sum(j))
    ans = min(tmp,ans)
print(ans)