#https://school.programmers.co.kr/learn/courses/30/lessons/42746

def solution(numbers):
    answer = ''
    numbers = [str(n) for n in numbers]
    
    numbers.sort(key = lambda x : x*4)
    if numbers[-1] == "0":
        return "0"
    
    for num in numbers[::-1]:
        answer += num
    
    return answer
