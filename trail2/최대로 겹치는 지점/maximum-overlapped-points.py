n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.

total = [0 for _ in range(100+1)]

for a, b in segments:
    for i in range(a, b + 1): #조건에서 도출된
        total[i] += 1

#print(total)

max = 0
for i in total:
    if max < i:
        max = i
    

print(max)

