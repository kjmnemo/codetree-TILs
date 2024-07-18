a = list(map(int, input().split()))
ind = a.index(-999)
a = a[:ind]
print(max(a), end =' ')
print(min(a))