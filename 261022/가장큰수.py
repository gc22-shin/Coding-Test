#https://school.programmers.co.kr/learn/courses/30/lessons/42746

def solution(numbers):
    answer = ''
    numbers = [str(n) for n in numbers]
    
    from functools import cmp_to_key
    #아, a+b랑 b+a를 비교해서 정렬해야겠구나를 떠올림
    
    def compare(a,b):
        if a + b > b + a:
            return 1
        elif a+ b < b + a:
            return -1
        return 0
    
    numbers.sort(key = cmp_to_key(compare))
    #print(numbers)
    
    
    '''
    numbers.sort(key = lambda x : x*4)
    '''
    if numbers[-1] == "0":
        return "0"
    
    for num in numbers[::-1]:
        answer += num
    
    
    return answer
