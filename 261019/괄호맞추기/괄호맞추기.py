#https://school.programmers.co.kr/learn/courses/30/lessons/12909#

def solution(s):
    from collections import deque
    s = deque(s)
    answer = True
    right = []
    #print(s)
    while len(s) != 0:
        curr = s.pop()
        #print(curr, right)

        if curr == ")":
            right.append(curr)
        else:
            if len(right) == 0:
                return False
            else:
                right.pop()
    if len(right) > 0:
        return False
    

    return True
