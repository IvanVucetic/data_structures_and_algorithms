# http://www.laurentluce.com/posts/binary-search-tree-library-in-python/

class Node(object):
    """
    Tree node: left and right child + data which can
    be any object
    """
    def __init__(self, data):
        """ Node constructor """
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        """Insert new node with data"""
        if self.data:
            if data < self.data:
                # ako nema cvora, napravimo ga
                if self.left is None:
                    self.left = Node(data)
                # a ako ima, njega sad pitamo isto (rekurzija)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def lookup(self, data, parent=None):
        """
        Lookup node containing data
        @param data: data of the node object to look up
        @param parent: node's parent
        @returns node and node's parent if found or None, None
        """
        if data < self.data:
            if self.left is None:
                return None, None
            else:
                return self.left.lookup(data, self)
        elif data > self.data:
            if self.right is None:
                return None, None
            else:
                return self.right.lookup(data, self)
        else:
            return self, parent


root = Node(8)
print root
print root.data

root.insert(3)
root.insert(10)
root.insert(1)
root.insert(6)
root.insert(4)
root.insert(7)
root.insert(14)
root.insert(13)

print root.left.right.data

node, parent = root.lookup(6)
print node.data, parent.data