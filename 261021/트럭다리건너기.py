https://school.programmers.co.kr/learn/courses/30/lessons/42583?language=python3##
def solution(bridge_length, weight, truck_weights):
    answer = 0

    from collections import deque

    bridge = deque() ## [[무게, 위에 있었던 시간], [무게2, 시간2]] 으로 저장할거임.
    tw = deque(truck_weights)

    while tw or bridge:
        #print(answer)
        #print(bridge, tw)

        if bridge:
            bridge = deque([[truck[0], truck[1] + 1] for truck in bridge])
            if bridge[0][1] > bridge_length:
                bridge.popleft()

        if tw:
            curr = tw.popleft()
            if (sum([truck[0] for truck in bridge])  +  curr) <= weight and bridge_length >= len(bridge) + 1: #새로 들어갈 차까지 합이 최대하중보다 작고, 들어간 차 대수가 최대 길이 + 1보다 작을떄 
                bridge.append([curr, 1]) # 차한대 더 올리기
            else:
                tw.appendleft(curr)
        answer += 1


    return answer
