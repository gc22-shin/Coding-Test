#https://school.programmers.co.kr/learn/courses/30/lessons/42747#

def solution(citations):
    answer = 0
    citations.sort()
    
    for h in range(len(citations)+ 1):
        '''
        #print(citations[i:])
        for j, c in enumerate(citations):
            if c >= h and len(citations[j:]) >= h:
                answer = h
        '''
        start_i = len(citations) -1 - h
        if start_i >= 0:
            if citations[start_i] >= h + 1:
                answer = h + 1
    
    return answer
