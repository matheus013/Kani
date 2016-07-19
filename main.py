from Node import Node
import copy

priority = []


def expand(actual, side):
    aux = travel(copy.deepcopy(actual), 1, 1, side)
    if aux.possible():
        priority.append(aux)

    aux = travel(copy.deepcopy(actual), 1, 0, side)
    if aux.possible():
        priority.append(aux)

    aux = travel(copy.deepcopy(actual), 0, 1, side)
    if aux.possible():
        priority.append(aux)

    aux = travel(copy.deepcopy(actual), 2, 0, side)
    if aux.possible():
        priority.append(aux)

    aux = travel(copy.deepcopy(actual), 0, 2, side)
    if aux.possible():
        priority.append(aux)
    priority.sort()
    pass


def travel(current, a, b, side):
    parent = copy.deepcopy(current)
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
    return Node(current.cost + 1, parent, current.state, not side)


def star(root):
    priority.append(root)
    while priority.__len__() > 0:
        next_node = priority.pop(0)
        # print str(next_node.state) + " real cost " + str(next_node.cost) + " f(n) = " + str(next_node.f())
        if next_node.finale():
            # print next_node.state
            return next_node
        expand(next_node, next_node.left)
    pass


if __name__ == '__main__':
    zero = Node
    start = Node(0, zero, [3, 3, 0, 0], True)
    result = star(start)

    while (result != zero):
        print str(result.state) + " " + str(result.left)
        result = result.parent
    pass
    # 3 3 0 0 T
    # 3 1 0 2 F
    # 3 2 0 1 T
    # 3 0 0 3 F
    # 1 1 2 2 T
    # 2 2 1 1 F
    # 0 2 3 1 T
    # 0 3 3 0 F
    # 0 1 3 2 T
    # 0 2 3 1 F
    # 0 0 3 3
