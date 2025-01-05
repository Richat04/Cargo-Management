from node import Node

from avl import AVLTree, comp_2
class Bin:
    def __init__(self, bin_id, capacity):
        self.id = bin_id
        self.capacity = capacity
        self.objects_stored = AVLTree(comp_2)    #makes an avl tree of objects stored in it

    def add_object(self, object):
        # Implement logic to add an object to this bin
        a= Node(object)
        #implement insert logic
        self.capacity -= object.size
        pass

    def remove_object(self, object_id):
        # Implement logic to remove an object by ID
        
        
        pass
