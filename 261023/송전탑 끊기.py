#https://school.programmers.co.kr/learn/courses/30/lessons/86971

def solution(n, wires):
    #print(adj)
    answers = []
    for v1, v2 in wires: #자를 전선
        adj = [[] for _ in range(n + 1)]
        for v1_, v2_ in wires: #연결할 전선
            if v1 == v1_ and v2 == v2_:
                continue
            adj[v1_].append(v2_)
            adj[v2_].append(v1_)
        
        visited = [False for _ in range(n + 1)]
        visited[0] = True
        
        #connected = (DFS(adj, 1, visited))       
        connected = BFS(adj, 1, visited)
        
        diff = abs(2* connected - n)
        answers.append(diff)
        
    return min(answers)

def DFS(adj, tower, visited):
    count = 1
    visited[tower] = True
    for t in adj[tower]:
        if not visited[t]:
            count += DFS(adj, t, visited) #DFS는 보통 카운트 값을 더해나가는식으로 함
            
            
def BFS(adj, start, visited):    
    from collections import deque
    q = deque()
    count = 1
    q.append(start)
    visited[start] = True
    while q:
        curr = q.popleft()
        for t in adj[curr]:
            if not visited[t]: 
                q.append(t)
                visited[t] = True
                count += 1
            
    return count
