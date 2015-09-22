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




# root = Node(8)
# print root
# print root.data
