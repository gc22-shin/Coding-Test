#https://school.programmers.co.kr/learn/courses/30/lessons/86491

def solution(sizes):
    answer = 0
    #print(sorted(sizes[0]))
    sort_size = [sorted(p) for p in sizes]
    #print(sort_size)
    max_size = [p[1] for p in sort_size]
    min_size = [p[0] for p in sort_size]
    
    answer = max(max_size) * max(min_size)
    
    return answer
