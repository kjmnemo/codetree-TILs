'''
1이상 K이하의 숫자를 하나 고르는 행위를
N번 반복하여 나올 수 있는 모든 서로 다른 순서쌍
'''

k, n = map(int, input().split())
from itertools import product

lst = [i for i in range(1,k+1)]
alst = list(product(lst, repeat=n))
#print(alst)
for a in alst:
    print(*a)