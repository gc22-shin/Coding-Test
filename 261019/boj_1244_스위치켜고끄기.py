N = int(input())
switches = list(map(int, input().split()))

M = int(input())
students = []
for _ in range(M):
    gender, num = map(int, input().split())

    students.append((gender, num))
#print(students)

def switch_light(idx):
    if switches[idx] == 0:
        switches[idx] = 1
    else:
        switches[idx] = 0

def switch_male(num):
    i = num - 1
    while i < len(switches):
        switch_light(i)
        i += num

def switch_female(num):
    center = num - 1
    max_diff = 0

    i = 1
    while 0 <= (center - i) and (center+ i) < len(switches):
        #print(candi)

        if switches[center - i] == switches[center + i]:
            max_diff = i
            i += 1
        else:
            break


    for i in range(center - max_diff, center+ max_diff + 1):
        switch_light(i)

#print(switches)
for gender, num in students:
    if gender == 1:
        switch_male(num)
    else:
        switch_female(num)
#    print(switches)


print(*switches)
#print(switches)