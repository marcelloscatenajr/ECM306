class BinaryTree:
    '''
    generic tree implementation in python
    '''

    def __init__(self):
        self.size = 0
        self.root = Node('root')

    def __contains__(self, value):
        '''
        checks using the In Order algorithm if there is the given value in the tree

        Use:\n
            \t"value" in instance-of-BinaryTree-class
        
        Returns:\n
            \tTrue or False
        '''
        return value in self.inorder_gen()

    def inorder_gen(self, node = None):
        '''
        inorder algorithm yielding generator for use in 
        generator expression \n

        Yields:\n
            \tgenerator object with every data in tree traversed acording to inorder algorithm
        '''
        if node is None:
            node = self.root

        if node is not None:
            yield from self.inorder_gen(node.left) if node.left else ()
            yield node.data
            yield from self.inorder_gen(node.right) if node.right else ()

    def pre_order_gen(self, node = None):
        '''
        inorder algorithm yielding generator for use in 
        generator expression \n

        Yields:\n
        '''
        node = self.root if node is None else ()

        if node is not None:
            raise NotImplementedError
            #IMPLEMENT

            


class Node:
    '''
    simple generic tree node

    Args: \n
        \tdata (object): stored data of this node 
        \tparent (TreeNode): parent node of said node, defaults to None 
        \tleft (TreeNode): left child node of said node, defaults to None
        \tright (TreeNode): right child node of said node, defaults to None

    Raises: \n
        \tTypeError: if the "parent", "left" or "right" arguments are not of type binarytree.Node or None
    '''

    def __init__(self, data = None, parent = None, left = None, right = None):

        if not all(isinstance(i, (Node, type(None))) for i in [parent, left, right]): 
            raise TypeError("parent:\t%s\nleft:\t%s\nright:\t%s" % (type(parent), type(left), type(right)))

        self.data = data
        self.parent = parent
        self.left = left
        self.right = right

    #def __repr__(self):
     #   return "Data:\t%s" % (self.data)


    #PROPERTIES

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, left):
        if not isinstance(left, (Node, type(None))):
            raise TypeError
        
        self.__left = left

        if self.left is not None:
            left.parent = self

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, right):
        if not isinstance(right, (Node, type(None))):
            raise TypeError
        
        self.__right = right

        if self.right is not None:
            right.parent = self

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, parent):
        if not isinstance(parent, (Node, type(None))):
            raise TypeError
        self.__parent = parent

    #END OF PROPERTIES    

