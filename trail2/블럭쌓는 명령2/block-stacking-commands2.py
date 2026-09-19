n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.
# 1-base

blocks = [0 for _ in range(n)]
for (a, b) in commands:
    for i in range(a-1, b):
        blocks[i] += 1

print(max(blocks))