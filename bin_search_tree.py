# Unable to create a Binary search tree myself, I found an article
# about it on the Internet. The entire code taken over from the web page:
# http://www.laurentluce.com/posts/binary-search-tree-library-in-python/
# I am not author of any of it, except for a few comments written as a 
#reminder/help to myself. 
# My idea was to try to figure the code out and learn from it as I read and type it over.

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

    def children_count(self):
        """
        Returns the number of children
        
        @returns number 0, 1 or 2
        """
        cnt = 0
        if self.left:
            cnt += 1
        if self.right:
            cnt += 1
        return cnt

    def delete(self, data):
        """
        Delete node containing data
        
        @param data: node's content to delete
        """
        # get node containing data
        node, parent = self.lookup(data)
        if node is not None:
            children_count = node.children_count()

        # if node has no children, just remove it
        if children_count == 0:
            if parent: #if parent exists, ie node is not root
                if parent.left is node:
                    parent.left = None
                else:
                    parent.right = None
                del node
            else:
                self.data = None # if it's root, just delete it
        
        # if node has 1 child, replace it with its child
        elif children_count == 1:
            if node.left:
                n = node.left
            else:
                n = node.right
            if parent:
                if parent.left is node:
                    parent.left = n
                else:
                    parent.right = n
                del node
            # special case hen the node is the root of the tree
            else:
                self.left = n.left
                self.right = n.right
                self.data = n.data

        # if node has 2 children
        else:
            # find its successor
            parent = node
            successor = node.right
            while  successor.left:
                parent = successor
                successor = successor.left
            # replace node data by its successor data
            node.data = successor.data
            # fix successor's parent's child
            if parent.left == successor:
                parent.left = successor.right
            else:
                parent.right = successor.right

    def print_tree(self):
        """
        Print tree content in order.
        """
        if self.left:
            self.left.print_tree()
        print self.data
        if self.right:
            self.right.print_tree()

    def compare_trees(self, node):
        """
        Compare 2 trees

        @param node: tree's root node to compare to
        @returns True if the tree passed is identical to this tree
        """
        if node is None:
            return False
        if self.data != node.data:
            return False
        res = True
        if self.left is None:
            if node.left: # ...is true (exists)
                return False
        else:
            res = self.left.compare_trees(node.left)
            if res is False:
                return False
        if self.right is None:
            if node.right:
                return False
        else:
            res = self.right.compare_trees(node.right)
            return res

    # Generator returning the tree elements one by one
    # Generators and Yeald keyword - unfamiliar ground to me
    # Trying to figure it out:




root = Node(8)
# print root
# print root.data

root.insert(3)
root.insert(10)
# root.insert(1)
# root.insert(6)
# root.insert(4)
# root.insert(7)
# root.insert(14)
# root.insert(13)

# print root.left.right.data

# node, parent = root.lookup(13)
# print node.data, parent.data

# root.delete(14)
# node, parent = root.lookup(13)
# print node.data, parent.data

root.print_tree()

root2 = Node(8)
root2.insert(3)
root2.insert(11)

print root.compare_trees(root2)