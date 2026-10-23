#https://school.programmers.co.kr/learn/courses/30/lessons/87946#

def solution(k, dungeons):
    answer = 0
    
    #조합 구해서 , 각 조합이 viable한지 체크 
    
    from itertools import permutations
    
    combs = []
    
    for i in range(1, len(dungeons) + 1):
        #combs = list(permutations(dungeons, i)) #i개 던전으로 이뤄진 조합
    
        #for comb in combs: #각 조합에 대해서
        for comb in permutations(dungeons, i): #permutation은 iterable이다

            curr = k
            possible = True #각 던전을 들어갔다 나올수 있는지
            #print(curr)
            for required, used in comb:
                #print(curr, required, )
                if required > curr:
                    #print("imposs")
                    possible = False
                    break
                curr -= used
            if possible:
                #print(comb)
                answer = len(comb)
    return answer
