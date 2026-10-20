#https://school.programmers.co.kr/learn/courses/30/lessons/42577v

def solution(phone_book):
    answer = True   
    phone_book.sort()
    
    for i in range(len(phone_book) - 1):
        if phone_book[i] ==  phone_book[i + 1][:len(phone_book[i])]:
            answer = False
            return answer
    
    return answer

#오답 
def solution(phone_book):
    answer = True   
    phone_book.sort()
    
    for i in range(len(phone_book) - 1):
        if phone_book[i] in phone_book[i + 1]:
            answer = False
            return answer
    
    return answer
