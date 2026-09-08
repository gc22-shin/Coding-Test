n = int(input())

# Please write your code here.
def print_inc(N):
    if N == 0:
        return
    print_inc(N - 1)
    print(N, end = " ")

def print_dec(N):
    if N == 0:
        return
    print(N, end = " ")
    print_dec(N - 1)


print_inc(n)
print()
print_dec(n)
