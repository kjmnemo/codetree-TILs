'''
n개의 회의의 정보
한회의 끝나는 직후에 동시에 다른 회의 시작

최대한 많은 수의 회의가 원활하게 진행되기 위해
> 취소해야 하는 최소 회의 수 출력
'''

import heapq
n = int(input())
room = []

for _ in range(n):
    a,b = map(int, input().split()) #시작 시간, 끝나는 시간
    heapq.heappush(room,(b,a)) # 끝나는 시간 오름차순으로 정렬

cnt = 0
time = 0
while room:
    end_time, start_time = heapq.heappop(room)
    if start_time >= time:
        cnt += 1
        time = end_time

print(n-cnt)