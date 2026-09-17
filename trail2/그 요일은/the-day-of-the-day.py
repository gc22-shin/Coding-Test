m1, d1, m2, d2 = map(int, input().split())
A = input()

# Please write your code here.
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
day_in_month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

idx = 0

for i in range(len(days)):
    if days[i] == A:
        idx = i
        break

#print(idx)

def get_sum_days(m, d):
    days = 0
    for i in range(m):
        days += day_in_month[i]

    days += d

    return(days)

diff = get_sum_days(m1, d1) % 7

diff_days = get_sum_days(m2, d2) - get_sum_days(m1, d1)

count = (diff_days - idx) // 7

if diff_days >= idx:
    count += 1

elif count < 0:
    count = 0

print(count)
