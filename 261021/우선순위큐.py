#https://school.programmers.co.kr/learn/courses/30/lessons/42583
def solution(priorities, location):
    answer = 0
    from collections import deque
    
    p = deque(priorities)
    while location != -1:
        curr = p.popleft()
        location -= 1
        temp = sorted(p)
        
        if p:
            if temp[-1] > curr:
                p.append(curr)
                if location == -1:
                    location = len(p) - 1
                    continue
            else:
                answer += 1
        else:
            answer += 1
    return answer
