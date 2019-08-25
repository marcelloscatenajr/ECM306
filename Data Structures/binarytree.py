class BinaryTree:
    '''
    simple binary tree implementation in python

    Args:\n
    \troot (Node): sets the root of this tree as the one passed
    \tAllows easy division of binary tree
    '''

    def __init__(self, root = None):
        self.root = root

    def __iter__(self):
        '''
        Inbuilt python funtions "max()" and "min()" already work with this object
        since it iterates through the built inorder generator and compares its values
        '''
        return iter(self.inorder_gen())

    def __len__(self):
        '''
        Returns:\n
        \tlenght (int): Ammount of total nodes in this tree
        '''
        return len([i for i in self])

    def __repr__(self):
        return str([i.data for i in self.inorder_gen()])
    
    def __str__(self):
        return "Preorder:\n%s\nInorder:\n%s\nPostorder:\n%s" % (str([i.data for i in self.pre_order_gen()]), str([i.data for i in self.inorder_gen()]), str([i.data for i in self.post_order_gen()]))



    def __contains__(self, value):
        '''
        checks using the In Order algorithm if there is the given value in the tree

        Use:\n
        \t"value" in instance-of-BinaryTree-class
        
        Returns:\n
        \tcontains (bool): returns if there is element in this object 
        '''
        return value in (i.data for i in self.inorder_gen())
        

    def inorder_gen(self, node = None):
        '''
        inorder algorithm yielding generator for use in 
        generator expression \n

        Args:\n
        \tnode (binarytree.Node): traverse the tree starting from this
        node (defaults to root)

        Yields:\n
        \tnode.data (obj): organized acording  to inorder algorithm
        '''
        if node is None:
            node = self.root

        if node is not None:
            yield from self.inorder_gen(node.left) if node.left else ()
            yield node
            yield from self.inorder_gen(node.right) if node.right else ()

    def pre_order_gen(self, node = None):
        '''
        preorder algorithm yielding generator for use in 
        generator expression \n

        Args:\n
        \tnode (binarytree.Node): traverse the tree starting from this
        node (defaults to root)

        Yields:\n
        \tnode.data (obj): organized acording  to preorder algorithm
        '''
        if node is None:
            node = self.root
        
        if node is not None:
            yield node
            yield from self.pre_order_gen(node.left) if node.left else ()
            yield from self.pre_order_gen(node.right) if node.right else ()
    
    def post_order_gen(self, node = None):
        '''
        postorder algorithm yielding generator for use in 
        generator expression \n

        Args:\n
        \tnode (binarytree.Node): traverse the tree starting from this
        node (defaults to root)

        Yields:\n
        \tnode.data (obj): organized acording  to postorder algorithm
        '''
        if node is None:
            node = self.root
        
        if node is not None:
            yield from self.post_order_gen(node.left) if node.left else ()
            yield from self.post_order_gen(node.right) if node.right else ()
            yield node

    #ROOT SETTER
    
    @property
    def root(self):
        return self.__root
    
    @root.setter
    def root(self, root):
        if isinstance(root, Node):
            self.__root = root
        elif root is None:
            self.__root = root
        else:
            self.__root = Node(root)

    def mean(self):
        '''
        Returns:\n
        \tmean (float): Mean for all data values in tree (requires data type to be comparable)
        '''
        return sum(i.data for i in self)/len(self)           

    def noneCount(self):
        '''
        Counts the ammount of Nones in this tree

        Returns:\n
        \tnoneCount (int): ammount of Nones
        '''
        return sum([i.data is None for i in self])

    def leafCount(self):
        return sum([i.right is None and i.left is None for i in self])

    def height(self, node = 'root'):
        '''
        Gives the height of a node on the tree, if not given one
        it will default to the height of the root

        Args:\n
        \tNode (binarytree.Node): node to find the height of (defaults to root)

        Return:\n
        \theight (int): height of said node
        '''
        if node == 'root':
            new = self.root
        else:
            new = node

        if new is None :
            return 0

        else:
            leftH = self.height(new.left)
            rightH = self.height(new.right)

            return 1 + max(leftH, rightH)
            

    def sum(self):
        '''
        Returns:\n
        \tSum of all of the keys in the nodes
        \tValue must be able to be added
        \tExample(node.data : int + node.data : tuple)
        '''
        return sum(i.data for i in self)
    
    def multiplos_de_dois(self):
        '''
        Yields:\n
        \tyields the even values in the tree
        \tvalues must be numbers
        \tExample(node.data : int + node.data : tuple)
        '''
        for i in self:
            if i.data % 2 == 0:
                yield i.data  

    def clear(self):
        '''
        clears the tree by setting root to null\n
        doesn't actually clear all the nodes from the memory
        '''
        self.root = None

class Node:
    '''
    simple generic tree node

    Args: \n
    \tdata (object): stored data of this node 
    \tparent (TreeNode): parent node of said node, defaults to None 
    \tleft (TreeNode): left child node of said node, defaults to None
    \tright (TreeNode): right child node of said node, defaults to None

    Raises: \n
    \tTypeError: if the "parent", "left" or "right" arguments are not of type 
    \tbinarytree.Node or None
    '''

    def __init__(self, data = None, parent = None, left = None, right = None):

        if not all(isinstance(i, (Node, type(None))) for i in [parent, left, right]): 
            raise TypeError("parent:\t%s\nleft:\t%s\nright:\t%s" % (type(parent), type(left), type(right)))

        self.data = data
        self.parent = parent
        self.left = left
        self.right = right

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
 