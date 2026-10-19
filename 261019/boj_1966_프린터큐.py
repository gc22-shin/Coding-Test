
T = int(input())
from collections import deque

for _ in range(T):
    #print(_)
    N, M = map(int, input().split())
    priorities = list(map(int, input().split()))
    turn = 1 #뽑히는 순서
    #print(priorities)

    priorities = deque(priorities)

    while len(priorities) != 0: #걍 빌 때까지
        #print(priorities, turn, M)
        paper = priorities.popleft()
        M -= 1

        if len(priorities) == 0:
            print(turn)
            break

        elif paper >= max(priorities):
            if M == -1:
                print(turn)
                break
            else:
                turn += 1
        else:
            priorities.append(paper)
            if M == -1:
                M = len(priorities) - 1
   # print("hi")