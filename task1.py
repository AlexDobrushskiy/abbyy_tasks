"""
Reverse single linked list for O(n) time and constant memory
"""


class Node:
    def __init__(self, v, ni):  # value, next_item
        self.v = v
        self.ni = ni


def reverse_sll(node):
    c = node
    p = None  # previous
    while c is not None:
        n = c.ni
        c.ni = p
        p = c
        c = n
    return p


def print_sll(n):
    c = n
    while c is not None:
        print(c.v)
        c = c.ni

if __name__ == '__main__':
    # 1 -> 3 -> 10 -> -3
    node = Node(1, None)
    node.ni = Node(3, None)
    node.ni.ni = Node(10, None)
    node.ni.ni.ni = Node(-3, None)
    print_sll(node)
    new_sll = reverse_sll(node)
    print_sll(new_sll)
