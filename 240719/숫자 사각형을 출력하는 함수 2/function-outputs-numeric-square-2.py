n = int(input())
alst = [2**i for i in range(n)]
print(*alst)

for i in range(2,n+1):
    for j in alst:
        print(i*j, end = ' ')
    print()