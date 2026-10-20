#https://school.programmers.co.kr/learn/courses/30/lessons/1845
def solution(nums):
    N = len(nums)
    answer = 0
    nums_set = set(nums)
    
    if len(nums_set) < (N/2):
        answer = len(nums_set)
    else:
        answer = N / 2
    
    return answer
