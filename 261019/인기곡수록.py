def solution(genres, plays):
    answer = []
    dic = {}
    temp = []
    play_dic = {}
    
    for i, (g, p) in enumerate(zip(genres, plays)):
        play_dic[g] = play_dic.get(g, 0) + p
        
    for i, (g, p) in enumerate(zip(genres, plays)):
        temp.append((i, g, p, play_dic[g]))
    
    temp.sort(key = lambda x : (-x[3], -x[2], x[0]))
    
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
            
    ''' 이렇게 세는것 가능
    count = {}
    for song in temp:
        if count.get(song[1], 0) < 2:
            count[song[1]] = count.get(song[1], 0) + 1
            answer.append(song[0])
    '''
    return answer
