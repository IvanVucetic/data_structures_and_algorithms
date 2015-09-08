class Node(object):
    """Node of a Binary Search Tree"""
    def __init__(self, val):
        self.val = val
        self.l_child = None
        self.r_child = None
        self.parent = None

    def set_left(self, node):
        self.l_child = node
        self.l_child.parent = self

    def set_right(self, node):
        self.r_child = node
        self.r_child.parent = self
        