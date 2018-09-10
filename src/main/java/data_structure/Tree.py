class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


t = Node(1, Node(2, Node(4, Node(7))), Node(3, Node(5), Node(6)))
