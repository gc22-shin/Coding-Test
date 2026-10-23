#https://school.programmers.co.kr/learn/courses/30/lessons/42842#

def solution(brown, yellow):
    answer = []
    #가로가 더 길다 -> sort
    #전체 카펫의 가로세로 길이가 노란색의 가로세로 길이보다 길어야함
    #이중 포문으로 풀어야할거같은데 시간복잡도 괜찮나
    
    total_size = brown + yellow
    
    
    total_comb = []
    for i in range(3, int(total_size ** 0.5) + 1): #최소 3은 되어야되니까 제곱수 이전까지만
        if total_size % i != 0 : 
            continue
        j = int(total_size / i) #나눠떨어지는거만 확인
        
        #그냥 무조건 가장 정사각형에 가까운게 답일거같은데 아닌가 
        #yellow가 소수면 아닐수도 있겠다 그럼 yellow 조합도 구해야되네
        #근데 yellow가 직사각형이 아닐수도 있네
        
        #그럼 그냥 가운데에 들어가기 위한 조건만?
        if (i - 2) * (j-2) == yellow: #해당조합에서 내부 공간 크기가 yellow보다 크면 ->크면이 아니라 같아야함, 테두리 한줄만 갈색인거임, 내부는 다 노란색
            total_comb = [j, i] #근데 이게 조합이 하나밖에 없는지 어떻게 알지? 그냥 문제를 믿는다?
            

            
    '''
    yellow_comb = []
    for i in range(1, int(yellow ** 0.5) + 1):
        if yellow % i != 0 :
            continue
        j = int(yellow / i)
        yellow_comb.append([i,j])
    #print(total_comb, yellow_comb)
    '''
    return total_comb
