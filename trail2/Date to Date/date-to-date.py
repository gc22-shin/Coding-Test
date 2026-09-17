m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
num_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def sum_days(m, d):
    days = 0
    for i in range(m):
        days += num_days[i]
    days += d

    return days


result = sum_days(m2, d2) - sum_days(m1, d1)  + 1

print(result)