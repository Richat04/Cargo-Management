from bin import Bin
from avl import AVLTree, comp_1, comp_2
from object import Object, Color
from exceptions import NoBinFoundException
from node import Node

class GCMS:
    def __init__(self):
        # Maintain all the Bins and Objects in GCMS
        self.Bin_Cap_Tree = AVLTree(compare_function = comp_2)
        self.Bin_ID_Tree = AVLTree(compare_function = comp_1)
        self.Object_ID_Tree = AVLTree(compare_function = comp_1)
        
         

    def add_bin(self, bin_id, capacity):
        c= AVLTree(compare_function=comp_2)
        node_bin_id = Node([bin_id,capacity],c)
        
        
        a = self.Bin_Cap_Tree.search(self.Bin_Cap_Tree.root, capacity)
        if a!= None:
            a.value.insert_value(Node(bin_id,None))
        else:
            b = AVLTree(compare_function=comp_2)
            b.insert_value(Node(bin_id, None))
            self.Bin_Cap_Tree.insert_value(Node(capacity, b))
        
        self.Bin_ID_Tree.insert_value(node_bin_id)       
              
        

    def add_object(self, object_id, size, color):

        if (color == Color.BLUE):
            req = self.Bin_Cap_Tree.Compact_fit(size)         #ideal node(capacity) jisme jaayega
            if (req == None or req.key <size):
                raise NoBinFoundException
            
            else:
                cap = req.key   #jis capacity wali bin mein gaya hai  
                bin_node = req.value.minValue(req.value.root)      #jis bin mein gaya hai
                bin_id = bin_node.key
                
                req.value.delete_value(Node(bin_id,None))
                cap-=size                            
                a = self.Bin_Cap_Tree.search(self.Bin_Cap_Tree.root, cap)
                if a!= None:
                    a.value.insert_value(Node(bin_id,None))
                else:
                    b = AVLTree(compare_function=comp_2)
                    b.insert_value(Node(bin_id, None))
                    self.Bin_Cap_Tree.insert_value(Node(cap, b)) 
                

                if req.value.root == None:
                    self.Bin_Cap_Tree.delete_value(req)               
                    
                d = self.Bin_ID_Tree.another_search(self.Bin_ID_Tree.root, bin_id)
                z=d.key
                z[1] = cap
                d.key=z
                d.value.insert_value(Node(object_id,None))
                self.Object_ID_Tree.insert_value(Node((object_id,size),bin_id))
                

        elif (color == Color.YELLOW):
            req = self.Bin_Cap_Tree.Compact_fit(size)
            if (req == None or req.key <size):
                raise NoBinFoundException
            else:
                cap = req.key   #jis capacity wali bin mein gaya hai  
                bin_node = req.value.maxValue(req.value.root)      #jis bin mein gaya hai
                bin_id = bin_node.key
                req.value.delete_value(Node(bin_id,None))
                cap-=size
                
                a = self.Bin_Cap_Tree.search(self.Bin_Cap_Tree.root, cap)
                if a!= None:
                    a.value.insert_value(Node(bin_id,None))
                else:
                    b = AVLTree(compare_function=comp_2)
                    b.insert_value(Node(bin_id, None))
                    self.Bin_Cap_Tree.insert_value(Node(cap, b))   
                if req.value.root == None:
                    self.Bin_Cap_Tree.delete_value(req)
                
                d = self.Bin_ID_Tree.another_search(self.Bin_ID_Tree.root, bin_id)
                z=d.key
                z[1] = cap
                d.key=z
                d.value.insert_value(Node(object_id,None))
                self.Object_ID_Tree.insert_value(Node((object_id,size),bin_id))
                

        elif (color == Color.RED):           
            
            req = self.Bin_Cap_Tree.maxValue(self.Bin_Cap_Tree.root)
            
            if (req == None or req.key <size):
                
                raise NoBinFoundException
            else:
                cap = req.key   #jis capacity wali bin mein gaya hai  
                bin_node = req.value.minValue(req.value.root)      #jis bin mein gaya hai
                bin_id = bin_node.key
                req.value.delete_value(Node(bin_id,None))
                cap-=size
                
                a = self.Bin_Cap_Tree.search(self.Bin_Cap_Tree.root, cap)
                if a!= None:
                    a.value.insert_value(Node(bin_id,None))
                else:
                    b = AVLTree(compare_function=comp_2)
                    b.insert_value(Node(bin_id, None))
                    self.Bin_Cap_Tree.insert_value(Node(cap, b))  
                if req.value.root == None:
                    self.Bin_Cap_Tree.delete_value(req)
    
                d = self.Bin_ID_Tree.another_search(self.Bin_ID_Tree.root, bin_id)
                z=d.key
                z[1] = cap
                d.key=z
                d.value.insert_value(Node(object_id,None))
                self.Object_ID_Tree.insert_value(Node((object_id,size),bin_id))
                

        elif (color == Color.GREEN):
            req = self.Bin_Cap_Tree.maxValue(self.Bin_Cap_Tree.root)
            
            if (req == None or req.key <size):
                raise NoBinFoundException
            else:
                cap = req.key   #jis capacity wali bin mein gaya hai  
                bin_node = req.value.maxValue(req.value.root)      #jis bin mein gaya hai
                bin_id = bin_node.key
                
                req.value.delete_value(Node(bin_id,None))
                cap-=size
                
                a = self.Bin_Cap_Tree.search(self.Bin_Cap_Tree.root, cap)
                if a!= None:
                    a.value.insert_value(Node(bin_id,None))
                else:
                    b = AVLTree(compare_function=comp_2)
                    b.insert_value(Node(bin_id, None))
                    self.Bin_Cap_Tree.insert_value(Node(cap, b))  
                if req.value.root == None:
                    self.Bin_Cap_Tree.delete_value(req)
                
                
                d = self.Bin_ID_Tree.another_search(self.Bin_ID_Tree.root, bin_id)
                z=d.key
                z[1] = cap
                d.key=z
                d.value.insert_value(Node(object_id,None))
                self.Object_ID_Tree.insert_value(Node((object_id,size),bin_id))
                


    def delete_object(self, object_id):
        # Implement logic to remove an object from its bin
        #first search the object in object tree, return its size and the delete it
        #then delete it from bin id tree
        #then again update it in capacity tree
        d = self.Object_ID_Tree.another_search(self.Object_ID_Tree.root, object_id)
        size = d.key[1]
        bin_id = d.value
        self.Object_ID_Tree.delete_value(d)

        req_bin = self.Bin_ID_Tree.another_search(self.Bin_ID_Tree.root, bin_id)
        a = req_bin.key
        cap = a[1]
        a[1]+=size
        new_cap = cap+size
        req_bin.key = a
        req_bin.value.delete_value(Node(object_id, None))

        b = self.Bin_Cap_Tree.search(self.Bin_Cap_Tree.root, cap)
        b.value.delete_value(Node(bin_id, None)) 

        z = self.Bin_Cap_Tree.search(self.Bin_Cap_Tree.root, new_cap)
        if z!= None:
            z.value.insert_value(Node(bin_id,None))
        else:
            y = AVLTree(compare_function=comp_2)
            y.insert_value(Node(bin_id, None))
            self.Bin_Cap_Tree.insert_value(Node(new_cap, y))
        if b.value.root == None:
            self.Bin_Cap_Tree.delete_value(b)
            

    def bin_info(self, bin_id):    
        # returns a tuple with current capacity of the bin and the list of objects in the bin (int, list[int])
        l=[]
        a = self.Bin_ID_Tree.another_search(self.Bin_ID_Tree.root, bin_id)
        p = a.value.inorder(a.value.root, l)
        if p == None:
            p=[]
            return (a.key[1],p)
        else:
            return (a.key[1],p)
        
        

    def object_info(self, object_id):     
        # returns the bin_id in which the object is stored
        a = self.Object_ID_Tree.another_search(self.Object_ID_Tree.root, object_id)
        if a == None:
            return None
        else:
            return a.value
    
 

