class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def topView(root):
    ans_dict = {}
    ans_dict[0] = root
    queue = []
    queue.append((root , 0))
    while queue :
        node_set = queue.pop(0)
        node = node_set[0]
        if node.left:
            v_level = node_set[1]-1
            queue.append((node.left , v_level))
            if v_level not in ans_dict:
                ans_dict[v_level] = node.left
        if node.right:
            v_level = node_set[1]+1
            queue.append((node.right , v_level))
            if v_level not in ans_dict:
                ans_dict[v_level] = node.right
    ans_dict = dict(sorted(ans_dict.items()))
    for i in ans_dict:
        print(ans_dict[i] , end = ' ')
            
    #Write your code here

