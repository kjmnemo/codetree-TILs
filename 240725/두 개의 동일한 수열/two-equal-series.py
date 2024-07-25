n = int(input())
alst = set(list(map(int,input().split())))
blst = set(list(map(int,input().split())))
if alst == blst:
    print('Yes')
else:
    print('No')