#https://school.programmers.co.kr/learn/courses/30/lessons/42586

def solution(progresses, speeds):
    answer = []
    from collections import deque
    
    #progresses = deque(progresses)
    speeds = deque(speeds)
    
    #progresses = deque([progresses[i] + speeds[i] for i in range(len(speeds))])
    #print(progresses)
    n = 0
    while len(progresses) > 0:
        n += 1
        print(n)
        
        progresses = deque([progresses[i] + speeds[i] for i in range(len(speeds))])
        
        
        #zip 활용!
        #progresses = deque(p + s for p, s in zip(progresses, speeds))
        #print(progresses, speeds)

        deployed = 0
        print(progresses)
        #if n == 9: break
        

        while len(progresses) != 0 and progresses[0] >= 100:

            curr = progresses.popleft()
            speeds.popleft()
            deployed += 1
            
        if deployed > 0:
            answer.append(deployed)
            
        print(progresses, speeds)
        
    
    return answer
