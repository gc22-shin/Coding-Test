m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

day_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def get_sum_days(m):
    days = 0
    for i in range(m):
        days += day_in_month[i]

    return days

diff = (get_sum_days(m1) + d1) % 7

result = (get_sum_days(m2) + d2) % 7 - diff

print(days[result])