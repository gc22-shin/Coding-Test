N = input()

# Please write your code here.
n = 0
for i in N:
    n = n * 2 + int(i)

n *= 17
result = []

while n >= 2:
    result.append(n % 2)
    n  = n // 2

result.append(n)

for i in result[::-1]:
    print(i, end = "")