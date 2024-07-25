n = int(input())
lst = sorted(list(map(int, input().split())))
print(*lst)
print(*lst[::-1])