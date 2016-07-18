class Node:
    cost = 0
    parent = 0
    left = True
    state = []

    def __init__(self, cost, parent, state, ):
        self.cost = cost
        self.parent = parent
        self.state = state

    def f(self, ):
        return self.cost + self.state[0] + self.state[1]

    def possible(self, ):
        for i in self.state:
            if i < 0:
                return False
        return self.state[0] >= self.state[1] & self.state[2] >= self.state[3]

    @property
    def __str__(self):
        return self.state

    def __lt__(self, other):
        return self.f() < other.f()

    def finale(self, ):
        return self.state == [0, 0, 3, 3]
