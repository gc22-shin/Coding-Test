def solution(clothes):
    answer = 1
    c_dic = {}
    for cloth, category in clothes:
        #print(cloth, category)
        c_dic[category] = c_dic.get(category, 0) + 1
    
    for key, value in c_dic.items():
        answer *= value+1
        
    answer -= 1
    return answer
