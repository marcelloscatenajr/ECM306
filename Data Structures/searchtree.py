from binarytree import BinaryTree, Node

class SearchTree(BinaryTree):
    '''
    Simple Search Tree implementation\n
    Inherits BinaryTree 
    '''
    
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
            if nodeKey in self:
                raise SearchTree.RepeatedKeyError("There is already a node with this key in this tree!")

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
                else:
                    if nodeTrab.right is None:
                        nodeTrab.right = Node(nodeKey)
                        break
                    else:
                        nodeTrab = nodeTrab.right



    class RepeatedKeyError (Exception):
        pass                  