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
    if di == "L":
        left_max += xi
    else:
        right_max += xi

#color = [0 for _ in range(left_max + right_max)] 
line = [{"color": "O", "W" : 0, "B": 0} for _ in range(left_max + right_max + 1)] #0무색 1흰 2검 3회

#print(len(line))

def print_curr_color():
    for grid in line:
        print(grid["color"], end = "")
    print()



def update_color(di : str, pos, new_pos):
    #print(pos, new_pos)
    if di == "R": #오른쪽 이동, 검은색
        for i in range(pos, new_pos + 1): #오른쪽이동
            line[i]["B"] += 1
            
            if line[i]["B"] >= 2 and line[i]["W"] >= 2:
                line[i]["color"] = "G"

            else:
                line[i]["color"] = "B"

    elif di == "L":
        for i in range(new_pos, pos + 1): #왼쪽 이동
            line[i]["W"] += 1
            
            if line[i]["B"] >= 2 and line[i]["W"] >= 2:
                line[i]["color"] = "G"

            else:
                line[i]["color"] = "W"

curr = left_max

for xi, di in zip(x, dir):
    #print(line)
    if di == "L":
        new_pos = curr - xi + 1
        #print(curr, new_pos)
        update_color(di, curr, new_pos)
        curr = new_pos

    else:
        new_pos = curr + xi - 1
        #print(curr, new_pos)
        update_color(di, curr, new_pos)
        curr = new_pos
    #print_curr_color()

white = 0
black = 0
gray = 0

#print()
#print_curr_color()
for grid in line:
    if grid["color"] == "W":
        white += 1
    elif grid["color"] == "B":
        black += 1
    elif grid["color"] == "G":
        gray += 1

print(white, black, gray)
