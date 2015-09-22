class Node(object):
    '''___'''

    def __init__(self, val=None, key=None):
        # key je broj (2, 5, 99) i sluzi kao index
        # val ne neka vrednost (npr string) koju indexiramo
        self.val = val
        self.key = key 
        self.parent = None
        self.lchld = None
        self.rchld = None

    def set_rchld(self, node):
        self.rchld = node
        self.rchld.parent = self

    def set_lchld(self, node):
        self.lchld = node
        self.lchld.parent = self

    def inorder(self):
        left_vals = self.lchld.inorder() if self.lchld is not None else []
        right_vals = self.rchld.inorder() if self.rchld is not None else []
        return left_vals + [self.val] + right_vals

    def insert(self, key, val):
        if not self.key:
            self.key = key
            self.val = val
        elif key < self.key:
            if self.lchld is None:
                self.lchld = Node(self)
            self.lchld.insert(key, val)
        elif key > self.key:
            if self.rchld is None:
                self.rchld = Node(self)
            self.rchld.insert(key, val)
        elif key == self.key:
            self.val = val

    def get_item(self, key):
        if key == self.key:
            return self.val
        elif key < self.key and self.lchld is not None:
            return self.lchld.get_item(key)
        elif key > self.key and self.rchld is not None:
            return self.rchld.get_item(key)
        else:
            return None

    def  ordered_traverse(self):
        if self.lchld is not None:
            for (x, y) in self.lchld.ordered_traverse:
                # o yield i generatorima: http://bit.ly/11tfEZq
                yield (x, y)
        yield (self.key, self.val)
        if self.rchld is not None:
            for (x, y) in self.rchld.ordered_traverse():
                yield (x, y)



# root = Node('az', 4)
# a = root.get_item(4)
# print a

# left = Node()
# root.set_lchld(left)
# print left.key, left.val

# root.insert(3, 'buki')
# b = root.get_item(3)
# print b

# c = root.get_item(5)
# print c

# ----

# left = Node(3)
# left.set_lchld(Node(1))
# left.set_rchld(Node(20))

# right = Node(7)
# right.set_lchld(Node(6))
# right.set_rchld(Node(30))

# root.set_lchld(left)
# root.set_rchld(right)

# print root.inorder()