from binarytree import BinaryTree, Node

class SearchTree(BinaryTree):
    '''
    Simple Search Tree implementation\n
    Inherits BinaryTree 
    For this tree, whatever object populates the tree node's data must be able to comparable to other objects or itself\n
    ie: "node1.data > node1.data" must be valid
    '''

    def __contains__(self, value):
        return self.searchKey(value) is not None

    def searchKey(self, key):
        '''
        Searches the search tree for the given key\n
        \tO(log (tree.height))

        Args:\n
        \tkey (obj): the given key will be the object that will be searched in the tree

        Returns:\n
        \tnode: returns the actual Tree Node, if found, otherwise, None
        '''
        node = self.root

        while node is not None and node.data != key:
            if key < node.data:
                node = node.left
            else:
                node = node.right
        return node

    
    def add(self, *nodeKeys):
        '''
        Adds node to tree acording to search tree algorithm.
        nodeKey object must be comparable (<, <=, ==, >, >=)

        Args:\n
        \t*nodeKeys (*obj): Keys to be added to nodes that are also added to the tree

        Raises:\n
        \tTypeError: if somewhere in the tree a Key cannot be compared to another. Example(node.left.key : str < node.key : int)
        \tSearchTree.RepeatedKeyError: if there is already a node with this key in this tree
        '''
        for nodeKey in nodeKeys:
            # if nodeKey in self:
            #     raise SearchTree.RepeatedKeyError("There is already a node with this key in this tree!")

            new_node = Node(nodeKey)

            if self.root is None:
                self.root = new_node
                continue
            
            nodeTrab = self.root

            while True:
                if nodeKey < nodeTrab.data:
                    if nodeTrab.left is None:
                        nodeTrab.left = Node(nodeKey)
                        break
                    else:
                        nodeTrab = nodeTrab.left
                elif nodeKey > nodeTrab.data:
                    if nodeTrab.right is None:
                        nodeTrab.right = Node(nodeKey)
                        break
                    else:
                        nodeTrab = nodeTrab.right
                elif nodeKey == nodeTrab.data:
                    raise SearchTree.RepeatedKeyError("There is already a node with this key in this tree!")
    
    def pop(self, nodeKey):
        '''
        Removes a Node from the tree, given a the node Key, and then mends the tree afterwards

        Args:\n
        \tnodeKey (object): the Key of the node to search and remove the node from the tree 

        Returns:\n
        \tsuccess (bool): returns if the removal was sucessful
        '''
        node = self.searchKey(nodeKey)
        
        if node is None:
            return False

        #if there is no left child
        if node.left is None:

            #and there is no right child, it's a leaf
            if node.right is None:

                #Find the parent node reference of this node and kill it
                if node.parent.left is node:
                    node.parent.left = None
                else:
                    node.parent.right = None
                
                return True

            else:
                #Determines if the node is the right or left child and then swaps the references between its right child and parent
                if node.parent.left is node:
                    node.right.parent, node.parent.left = node.parent, node.right
                else:
                    node.right.parent, node.parent.right = node.parent, node.right

                return True

        elif node.right is None:
            #Determines if the node is the right or left child and then swaps the references between its left child and parent
                if node.parent.left is node:
                    node.left.parent, node.parent.left = node.parent, node.left
                else:
                    node.left.parent, node.parent.right = node.parent, node.left

                return True

        else:
            #Node has left and right subtrees

            node_traversal = node.right
            #traverse tree to find the lowest key in the right subtree
            while node_traversal.left is not None:
                node_traversal = node_traversal.left

            #Determines if the node_traversal is a right or left child and then gives its data to the original Node, then kills node_traversal parent's references 
            if node_traversal.parent.left is node_traversal:
                node.data, node_traversal.parent.left = node_traversal.data, None
            else:
                node.data, node_traversal.parent.right = node_traversal.data, None 

            return True

    def remove(self, nodeKey):
        '''
        Removes the entire subtree of a given node

        Args:\n
        \tnodeKey (object): the Key of the node to search and remove the node from the tree 

        Returns:\n
        \tsuccess (bool): returns if the removal was sucessful
        '''
        node = self.searchKey(nodeKey)

        if node is None:
            return False

        if node is self.root:
            self.root = None
            return True
        
        if node.parent.left is node:
            node.parent.left = None
        else:
            node.parent.right = None

        return True


    class RepeatedKeyError (Exception):
        pass                  