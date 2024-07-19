n = int(input())
if n > 369:
    for i in range(369,n+1):
        if i%2==1:
            print(i,end =' ')
else:
    for i in range(n,370):
        if i%2==1:
            print(i,end=' ')