#https://school.programmers.co.kr/learn/courses/30/lessons/42576

def solution(participant, completion):
    answer = ''
    count = {}
    for a in participant:
        count[a] = count.get(a, 0) + 1
    #print(count)
    for a in completion:
        count[a] = count.get(a, 0) - 1
        if count[a] == 0:
            del count[a]
    #print(count)
        
    if len(count) != 0:
        answer = list(count.keys()).pop()
    
    
    return answer

