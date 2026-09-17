a, b = map(int, input().split())
n = input()

# Please write your code here.
mid = 0 # 중간 10진수 변환 결과물 저장 (바로 못하겠음)

for i in n:
    mid = mid * a + int(i)

result = []

while mid >= b:
    result.append(mid % b)
    mid = mid // b

result.append(mid) #가장 아래 자리수 append

for i in result[::-1]:
    print(i, end = "")