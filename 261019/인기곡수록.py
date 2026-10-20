#https://school.programmers.co.kr/learn/courses/30/lessons/42579/solution_groups?language=python3
def solution(genres, plays):
    answer = []
    dic = {}
    temp = []
    play_dic = {}
    
    for i, (g, p) in enumerate(zip(genres, plays)):
        #print(i, g, p)
        play_dic[g] = play_dic.get(g, 0) + p
        
    for i, (g, p) in enumerate(zip(genres, plays)):
        '''
        if g not in dic:
            dic[g] = [play_dic[g], (i, p)]
        else:
            dic[g].append((i, p))
        '''
        temp.append((i, g, p, play_dic[g]))
    temp.sort(key = lambda x : (-x[3], -x[2], x[0]))
    #print(temp)
    g_count = 0
    prev_g = ''
    for song in temp:
        if prev_g == song[1]:
            if g_count < 2:
                answer.append(song[0])
                g_count += 1
            else:
                g_count += 1
        else:
            prev_g = song[1]
            g_count = 1
            answer.append(song[0])
            
        
                   
    
    
    return answer
