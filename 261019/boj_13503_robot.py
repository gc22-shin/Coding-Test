N, M = map(int, input().split())
r, c, d = map(int, input().split())

room = []
for _ in range(N):
    room.append(list(map(int, input().split())))

class Robot():
    def __init__(self, r, c, d):
        self.i = r
        self.j = c
        self.dir = d
        self.for_i, self.for_j = [-1, 0, 1, 0], [0, 1, 0, -1]
        self.back_i, self.back_j = [1, 0, -1, 0], [0, -1, 0, 1]
        self.cleaned = 0

    def clean_curr(self):
        room[self.i][self.j] = -1  #청소된게 -1
        self.cleaned += 1

    def movable(self, new_i, new_j):
        if 0 <= new_i and new_i < N:
            if 0 <= new_j and new_j < M:
                return room[new_i][new_j] != 1

    def check_cleanable(self):
        for _ in range(3, -1, -1):
            d = (self.dir + _) % 4 #반시계
            new_i = self.i + self.for_i[d]
            new_j = self.j + self.for_j[d]
            if self.movable(new_i, new_j):
                if room[new_i][new_j] == 0:
                    return True, new_i, new_j, d
        return False, self.i, self.j, self.dir


    def move(self):
        while True:
            if room[self.i][self.j] == 0:
                self.clean_curr()
            cleanable, self.i, self.j, self.dir = self.check_cleanable()
            if cleanable:
                continue
            else:
                new_i = self.i + self.back_i[self.dir]
                new_j = self.j + self.back_j[self.dir]
                if not self.movable(new_i, new_j):
                    break
                self.i = new_i
                self.j = new_j

robot = Robot(r, c, d)
robot.move()
print(robot.cleaned)