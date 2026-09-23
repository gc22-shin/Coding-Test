n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

# Please write your code here.
# 일단 가장 왼쪽/오른쪽 값을 잡아야할듯.
# 왼쪽 방향만 뽑아서 다 더한값
#오른쪽 방향만 뽑아서 더한값 
# 둘의 합 = 길이

left_max = 0
right_max = 0

for xi, di in zip(x,dir):
    #print(x, dir)
    if di == 'L':
        left_max += xi
    else:
        right_max += xi

#수직선 (최초 position은 left_max)
line = [0 for _ in range(left_max + right_max)]

pos = left_max

def update_line(left, right):
    '''지나간 곳 업데이트'''
    for i in range(left, right):
        line[i] += 1

for xi, di in zip(x, dir):
    if di == 'L':
        new_pos = pos - xi
        update_line(new_pos, pos)
        pos = new_pos
    elif di == 'R':
        new_pos = pos + xi
        update_line(pos, new_pos)
        pos = new_pos

    #print(line)

result = 0

for i in line:
    if i >= 2:
        result += 1

print(result)
