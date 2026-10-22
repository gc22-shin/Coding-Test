#https://school.programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    answer = []
    for i, j, k in commands:
        arr = array[i-1:j]
        arr.sort()
        #print(arr)
        #if i == 4:break
        num = arr[k - 1]
        #print(arr)
        
        
        
        answer.append(num)
    return answer
