#https://school.programmers.co.kr/learn/courses/30/lessons/42839

def solution(numbers):
    from itertools import permutations
    answer = 0
    
    def check_prime(num):
        if num in [0, 1]:
            return False
        
        for n in range(2, int(num ** 0.5) + 1):
            if num % n == 0: return False
        #print(num)
        return True
    
    
    total_comb = []
    for i in range(1, len(numbers) + 1):
        combs = list(permutations(numbers, i))
        
        for c in combs:
            total_comb.append(int(''.join(c)))
            
    #print(total_comb)
    total_comb = list(set(total_comb))
    #print(total_comb)
    
    for num in total_comb:
        if check_prime(num):
            answer += 1
            
    ####백트래킹####
    
    combs = []
    visited = [False for _ in numbers]
    
    def find_comb(visited, curr_comb):
        if curr_comb:
            combs.append(''.join(curr_comb))
        
        for i in range(len(numbers)):
            if not visited[i]:
                curr_comb.append(numbers[i])
                visited[i] = True
                find_comb(visited, curr_comb)
                
                curr_comb.pop()
                visited[i] = False
    
    find_comb(visited, [])
    
    return answer
