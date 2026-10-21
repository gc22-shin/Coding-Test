#https://school.programmers.co.kr/learn/courses/30/lessons/42584#
def solution(prices):
    answer = [0 for _ in prices]
    
    stack = []
    for i in range(len(prices)): #prices 인덱스에 대해서
        while stack and prices[stack[-1]] > prices[i]: #현재까지 스택의 값보다 현재 값이 작아지면 (증가 파괴)
            j = stack.pop() #다시 증가 방향 맞출수 있을 때까지 뽑기
            answer[j] = i - j # 뽑힌 인덱스의 위치는 현재값까지 증가했던 것 -> 현재 인덱스 - 뽑힌 인덱스 = 증가 지속된 기간 

        stack.append(i) #증가 맞춰서 붙이고 마무리
        
    for i in stack:
        # 스택에 남아있는 인덱스들= 끝까지 증가
        answer[i] = len(prices) - 1 - i  #마지막 인덱스 - 자신 인덱스 = 증가한 기간


    '''
    시간 초과!!
    while prices:
        t = 0
        curr = prices.popleft()
        temp = deque(i for i in prices)
        
        #print(curr)
        
        while temp:
            next = temp.popleft()
            #print(t, next, temp)
            t += 1   #일단 증감 비교하지말고 시간 증가
            if curr > next: #증가해놓고 만약에 더 컸다면 루프 끊기
                break
        answer.append(t)
        #print()
        '''
    return answer
