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

print(max(abs(a-b),abs(b-c))-1)