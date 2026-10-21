#https://school.programmers.co.kr/learn/courses/30/lessons/12906

def solution(arr):
    from collections import deque
    answer = []
    arr = deque(arr)
    #print(arr)
    #print(answer[-1])
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    
    for n in arr:
        if len(answer) == 0:
            answer.append(n)
        elif answer[-1] != n:
            answer.append(n)
    '''
    for n in arr:
        if answer[-1:] == [n]:
            continue
        answer.append(n)
    ##############
    
    for _ in range(len(arr)):
        num = arr.popleft()
        if len(answer) == 0:
            answer.append(num)
        elif num != answer[-1]:
            answer.append(num)
        #print(answer)
    '''
    return answer
