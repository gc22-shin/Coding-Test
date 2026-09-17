a, b, c = map(int, input().split())

# Please write your code here.
start = 11 * 24 * 60 + 11 * 60 + 11

end = a * 24 * 60 + b * 60 + c

if end < start:
    print(-1)
else:
    print(end - start)
