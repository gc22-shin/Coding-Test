n = int(input())

# Please write your code here.

result = []
while n > 1: # 더이상 2로 나눌수 없을때까지
    rem = n % 2 # 해당 자리수
    result.append(rem)
    n = n // 2

result.append(n) #최종 가장 윗자리수를 넣어줌

for i in result[::-1]: #가장 앞에 들어간게 첫쨰 자리수임
    print(i, end="")



