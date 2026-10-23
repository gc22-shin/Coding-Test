#https://school.programmers.co.kr/learn/courses/30/lessons/43165?language=python3

def solution(numbers, target):
    def DFS(target, curr_i, total):
        if curr_i == len(numbers):
            if total == target:
                return 1
            return 0
        
        plus = DFS(target, curr_i + 1, total + numbers[curr_i])
        minus = DFS(target, curr_i + 1, total - numbers[curr_i])
        
        return plus + minus
    
    answer = DFS(target, 0, 0)
    
    return answer
    
    
    
    '''
    #모든 수는 + 또는 -선택
    #-> 하나의 수에 대해 +/-선택하면 반대쪽 부호도 visited로처리하면 되지 않을까?
    
    numbers_ = [i for i in numbers]
    for n in numbers:
        numbers_.append(-1 * n)
    #print(numbers_)
    adj = [[] for _ in range(len(numbers_))]
    
    for i, n in enumerate(numbers_):
        for j, m in enumerate(numbers_):
            if i == j or j == i + len(numbers):
                continue
            adj[i].append(m)  #adj의 인덱스를 numbers_에 넣으면 무슨숫자에 대응하는지 나옴
    print(adj)
    
    visited = [False for _ in range(len(numbers_))] #1 2 3 4 5, -1 -2 -3 -4 -5

    for i in range(len(numbers_)):
        if not visited[i]:
            visited[i] = True
            answer += DFS(visited, target, i)
    return answer
    '''


        
        
    
                
    
