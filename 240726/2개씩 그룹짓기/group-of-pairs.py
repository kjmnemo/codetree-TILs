n = int(input())

lst = list(map(int, input().split()))
lst.sort()

alst = []
for j in range(n):
    alst.append(lst[j]+lst[2*n-1-j])
alst.sort()
print(alst[-1])