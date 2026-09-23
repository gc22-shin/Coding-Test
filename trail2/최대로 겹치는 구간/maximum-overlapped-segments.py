n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
#total = [0 for _ in range(100 + 1)] #겹치는 구간 계산용 

start = float('inf')
end = -float('inf')


for a, b in segments: # 각 선분 뽑기
    if a < start:
        start = a   
    if b > end:
        end = b

#print(start, end)
segments_changed = [(a - start, b - start) for a, b in segments]

#print(segments_changed)

total = [0 for _ in range(end - start+ 1)] #겹치는 구간 계산용 

for a, b in segments_changed: # 각 선분 뽑기
    for i in range(a, b):  # 각 선분 시작점기준 계산 -> b까지만 계산
        total[i] += 1
        
print(max(total))