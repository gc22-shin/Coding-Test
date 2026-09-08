n = int(input())

# Please write your code here.
def print_hello(N):
    if N == 0:
        return
    print_hello(N - 1)
    print("HelloWorld")

print_hello(n)