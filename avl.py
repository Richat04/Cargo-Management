from node import Node

def comp_1(node_1, node_2):  #will pass capacity and id of bin as a tuple/list (capacity,id) as an id of node
    if node_1.key[0] < node_2.key[0]:   # for -1 return value, if node 2 is root of subtree, node 1 will go to left subtree, otherwise right subtree
        return -1
    else:
        return 1
    
    

def comp_2(node1, node2):    #for bin_id and object id + object inside a bin avl tree
    if node1.key < node2.key:
        return -1
    else:
        return 1
    

class AVLTree:
    def __init__(self, compare_function=comp_1):
        self.root = None
        self.size = 0
        self.comparator = compare_function

    def balance(self,node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)
    
    def height(self, node):
        if not node:
            return 0
        return node.height

    
    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y
    
    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y
    
    def insert_node(self, root, node):  #can be used for all trees, just change the comparator function
        if not root:
            return node
            
        if self.comparator(node , root) < 0:
            root.left = self.insert_node(root.left , node)
        else:
            root.right = self.insert_node(root.right , node)

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        self.size = self.root.height

        a = self.balance(root)
        #This is the left- left case so only one rotation needed
        if a > 1 and self.comparator(node , root.left) == -1:
            if node == self.root:
                self.root = node.left
            return self.right_rotate(root)
        
        # This is right-right case so only one rotation needed
        if a<-1 and self.comparator(node , root.right) == 1:
            if node == self.root:
                self.root = node.right
            return self.left_rotate(root)
        
        #This is the left - right case so two rotations needed
        if a>1 and self.comparator(node, root.left) ==1:
            if node == self.root:
                self.root = node.left.right
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        
        #This is right left case so two rotations needed
        if a<-1 and self.comparator(node,root.right) ==1:
            if node == self.root:
                self.root = node.right.left
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        
        return root


    def insert_value(self,value):
        self.root = self.insert_node(self.root, value)

    def maxValue(self, root):
        current = root
        
        #loop down to find the rightmost leaf
        while(current.right):
            current = current.right
        return current
    
    def minValue(self, root):
        current = root
    
        # loop down to find the leftmost leaf
        while(current.left is not None):
            current = current.left
    
        return current
    

    def delete(self, root, node):
        if not root:
            return root

        if node.key < root.key:
            root.left = self.delete(root.left, node)
        elif node.key > root.key:
            root.right = self.delete(root.right, node)
        else:
            if not root.left:
                temp = root.right
                root = None
                return temp
            elif not root.right:
                temp = root.left
                root = None
                return temp

            temp = self.minValue(root.right)
            root.key = temp.key
            root.value = temp.value
            root.right = self.delete(root.right, temp)

        if not root:
            return root

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance = self.balance(root)

        if balance > 1 and self.balance(root.left) >0:
            # if node == self.root:
            #     self.root = node.left
            return self.right_rotate(root)

        # Right rotation
        if balance < -1 and self.balance(root.right) < 0:
            # if node == self.root:
            #     self.root = node.right
            return self.left_rotate(root)

        # Left-Right rotation
        if balance > 1 and self.balance(root.left) < 0:
            # if node == self.root:
            #     self.root = node.left.right
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right-Left rotation
        if balance < -1 and self.balance(root.right) > 0:
            # if node == self.root:
            #     self.root = node.right.left
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root


    def delete_value(self, value):
        self.root = self.delete(self.root, value)


    def search(self,root, key):   #this search is for the main tree
        # If root is None
        if root is None:
            return root

        # If found, return True
        elif root.key == key:
            return root
        
        elif root.key > key:
            return self.search(root.left, key)

        # Otherwise, recur to the
        # right subtree
        else:
            return self.search(root.right, key)
        
    def another_search(self,root, key):       #This search is for the two trees
        # If root is None
        if root is None:
            return root

        # If found, return True
        elif root.key[0] == key:
            return root
        
        elif root.key[0] > key:
            return self.another_search(root.left, key)

        # Otherwise, recur to the
        # right subtree
        else:
            return self.another_search(root.right, key)

    def inorder(self,node,l):
        if node is None:
            return
        self.inorder(node.left,l)
        l.append(node.key)
        self.inorder(node.right,l)
        return l

    

    def Compact_fit(self,size):
        result = None
        root = self.root
        while root:
            if root.key >= size:
                result = root  # Update result
                root = root.left  # Move left to find a smaller value
            else:
                root = root.right  # Move right for a larger value
        
        #tree1 = result.value  #access to the nested tree
        return result

if __name__ == "__main__":
    l=[]
    
    tree=AVLTree(compare_function=comp_2)
    tree.insert_value(Node(10,15))
    tree.insert_value(Node(10,20))
    tree.insert_value(Node(15,0))
    tree.insert_value(Node(90,80))
    tree.insert_value(Node(50,60))
    
    a = tree.delete_value(Node(90,80))
    p=tree.inorder(tree.root,l)
    print(p)
    b= tree.maxValue(tree.root)
    print(b.key)
    c = tree.Compact_fit(14)
    print(c.key)

    
    


    
    