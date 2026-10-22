#https://school.programmers.co.kr/learn/courses/30/lessons/42626

def solution(scoville, K):
    import heapq
    answer = 0
    
    heapq.heapify(scoville)
    #print(scoville)
    
    while scoville[0] < K:
        first = heapq.heappop(scoville)
        if len(scoville) == 0:
            return -1
        second = heapq.heappop(scoville)
        
        mix = first + second * 2
        heapq.heappush(scoville, mix)
        answer += 1
    
    return answer
