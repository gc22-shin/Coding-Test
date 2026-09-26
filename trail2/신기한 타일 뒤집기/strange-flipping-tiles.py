n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Please write your code here.
left_max = 0
right_max = 0

for xi, di in zip(x, dir):
    if di == 'L':
        left_max += xi
    else:
        right_max += xi

line = [-1 for _ in range(left_max + right_max)] #0 = W , 1 = B


def update_tile(pos, num, di):
    if di == 'L':
        new_pos = pos - num + 1
        for i in range(new_pos, pos + 1):
            line[i] = 0
    else:
        new_pos = pos + num - 1
        for i in range(pos, new_pos + 1):
            line[i] = 1

    return new_pos

curr = left_max
for num, di in zip(x, dir):
    curr = update_tile(curr, num, di)
    #print(line)

#print(line)
ans_0 = 0
ans_1 = 0
for i in line:
    if i == 0:
        ans_0 += 1
    elif i == 1:
        ans_1 += 1

print(ans_0, ans_1)

