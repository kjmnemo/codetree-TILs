from itertools import permutations

n = int(input())
lst = [i for i in range(1,n+1)]
alst = list(permutations(lst,n))
for ans in alst:
    print(*ans)