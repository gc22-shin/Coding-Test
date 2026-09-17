N, B = map(int, input().split())

# Please write your code here.
result = []
while N >= B:
    result.append(N % B)
    N = N // B

result.append(N) #최종 나머지 append

for i in result[::-1]:
    print(i, end="")