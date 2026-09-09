n = int(input())

# Please write your code here.
def print_star(N):
    if N == 0:
        return
    print_star(N - 1)
    print("*" * N)

print_star(n)