n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.
ans = 0

def find_max_xor(idx, count, current_xor):
    global ans
    # m개를 모두 선택한 경우
    if count == m:
        if current_xor > ans:
            ans = current_xor
        return
    
    # 남은 원소를 다 더해도 m개를 채울 수 없는 경우 탐색 종료
    if (n - idx) < (m - count):
        return

    # 현재 원소를 선택하는 경우
    find_max_xor(idx + 1, count + 1, current_xor ^ A[idx])
    # 현재 원소를 선택하지 않는 경우
    find_max_xor(idx + 1, count, current_xor)

find_max_xor(0, 0, 0)
print(ans)