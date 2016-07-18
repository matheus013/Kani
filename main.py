from Node import Node

priority = []


def expand(actual, side):
    aux = travel(actual, 1, 1, side)
    if aux.possible():
        priority.append(aux)
    aux = travel(actual, 1, 0, side)
    if aux.possible():
        priority.append(aux)
    aux = travel(actual, 0, 1, side)
    if aux.possible():
        priority.append(aux)
    aux = travel(actual, 2, 0, side)
    if aux.possible():
        priority.append(aux)
    aux = travel(actual, 0, 2, side)
    if aux.possible():
        priority.append(aux)
    priority.sort()
    pass


def travel(current, a, b, side):
    # print side
    if side:
        current.state[0] = current.state[0] - a
        current.state[2] = current.state[2] + a
        current.state[1] = current.state[1] - b
        current.state[3] = current.state[3] + b
    else:
        current.state[0] = current.state[0] + a
        current.state[2] = current.state[2] - a
        current.state[1] = current.state[1] + b
        current.state[3] = current.state[3] - b
    return Node(current.state, current, current.cost + 1, not side)


def star(root):
    priority.append(root)
    while priority.__len__() > 0:
        next_node = priority.pop(0)
        if next_node.finale():
            print next_node.state
            return next_node
        expand(next_node, next_node.left)
    pass


if __name__ == '__main__':
    start = Node(0, 0, [3, 3, 0, 0], True)
    star(start)
    pass
