'''
정수n을 1,2,3으로 나타내는 방법의 수
'''
n = int(input())
ans = 0

def dfs(result):
    global ans
    if result >= n:
        if result ==n:
            ans += 1
        return

    for i in range(1,4):
        dfs(result+i)

dfs(0)
print(ans)