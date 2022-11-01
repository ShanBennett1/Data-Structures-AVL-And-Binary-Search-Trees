"""
AVL_Tree.py

"""

def inputInt():
    while True:
        try:
            value = int(input())
        except ValueError:
            print('Invalid input. Re-enter:')
            continue
        break
    return value

outputdebug = False

def debug(msg):
    if outputdebug:
        print (msg)


class Node():
    def __init__(self, key):
        self.key = key
        self.left = None 
        self.right = None 


class AVLTree():
    def __init__(self, *args):
        self.node = None 
        self.height = -1  
        self.balance = 0;
        
        if len(args) == 1: 
            for i in args[0]: 
                self.insert(i)
                
                
    def height(self):
        if self.node:
            return self.node.height 
        else: 
            return 0
        
    
    def is_leaf(self):
        return (self.height == 0)
    

    def get_leafs(self):
        '''
        A method to find and print all leaf nodes
        '''
        if (self.node != None):
            if self.is_leaf():
                print(self.node.key)
            if self.node.left != None: 
                self.node.left.get_leafs()
            if self.node.right != None: 
                self.node.right.get_leafs()
                
            
    def get_nonleafs(self):
        '''
        A method to find and print all non-leaf nodes
        '''
        if (self.node != None):
            if not self.is_leaf():
                print(self.node.key)
            if self.node.left != None: 
                self.node.left.get_nonleafs()
            if self.node.right != None: 
                self.node.right.get_nonleafs()
                
    
    def insert(self, key):
        tree = self.node
        
        newnode = Node(key)
        
        if tree == None:
            self.node = newnode 
            self.node.left = AVLTree() 
            self.node.right = AVLTree()
            print("Inserted key [" + str(key) + "]")
        
        elif key < tree.key: 
            self.node.left.insert(key)
            
        elif key > tree.key: 
            self.node.right.insert(key)
        
        else: 
            print("Key [" + str(key) + "] already in tree.")
            
        self.rebalance()
        

    def find_node(self, key):
        if (self.node != None):
            if key == self.node.key:
                print(key, 'is in the tree.')
            elif key < self.node.key:
                self.node.left.find_node(key)
            elif key > self.node.key:
                self.node.right.find_node(key)
        else:
            print(str(key)+" is not in the tree.")
            

    def delete(self, node, delkey):
        if not node:
            #if key does not exist in tree
            print("Key ["+str(delkey)+"]","is not in the tree.")
            return node
        elif delkey < node.key:
            node.left.node = self.delete(node.left.node, delkey)
        elif delkey > node.key:
            node.right.node = self.delete(node.right.node, delkey)
        else:
            if node.left.node is None:
                temp = node.right.node
                return temp
            elif node.right.node is None:
                temp = node.left.node
                return temp
            temp = self.logical_successor(node) #finding min-value in right subtree
            node.key = temp.key
            node.right.node = self.delete(node.right.node, temp.key)

        #updating heights and rebalancing the tree
        self.update_heights()
        self.rebalance()
        
        return node
    
        
    def rebalance(self):
        ''' 
        Rebalance a particular (sub)tree
        ''' 
        # key inserted. Let's check if we're balanced
        self.update_heights(False)
        self.update_balances(False)
        while self.balance < -1 or self.balance > 1: 
            if self.balance > 1:
                if self.node.left.balance < 0:  
                    self.node.left.lrotate() # we're in case II
                    self.update_heights()
                    self.update_balances()
                self.rrotate()
                self.update_heights()
                self.update_balances()
                
            if self.balance < -1:
                if self.node.right.balance > 0:  
                    self.node.right.rrotate() # we're in case III
                    self.update_heights()
                    self.update_balances()
                self.lrotate()
                self.update_heights()
                self.update_balances()


            
    def rrotate(self):
        # Rotate left pivoting on self
        debug ('Rotating ' + str(self.node.key) + ' right') 
        A = self.node 
        B = self.node.left.node 
        T = B.right.node 
        
        self.node = B 
        B.right.node = A 
        A.left.node = T 

    
    def lrotate(self):
        # Rotate left pivoting on self
        debug ('Rotating ' + str(self.node.key) + ' left') 
        A = self.node 
        B = self.node.right.node 
        T = B.left.node 
        
        self.node = B 
        B.left.node = A 
        A.right.node = T 
        
            
    def update_heights(self, recurse=True):
        if not self.node == None: 
            if recurse: 
                if self.node.left != None: 
                    self.node.left.update_heights()
                if self.node.right != None:
                    self.node.right.update_heights()
            
            self.height = max(self.node.left.height,
                              self.node.right.height) + 1 
        else: 
            self.height = -1
            
            
    def update_balances(self, recurse=True):
        if not self.node == None: 
            if recurse: 
                if self.node.left != None: 
                    self.node.left.update_balances()
                if self.node.right != None:
                    self.node.right.update_balances()

            self.balance = self.node.left.height - self.node.right.height 
        else: 
            self.balance = 0 


    def logical_predecessor(self, node):
        ''' 
        Find the biggest valued node in LEFT child
        ''' 
        node = node.left.node 
        if node != None: 
            while node.right != None:
                if node.right.node == None: 
                    return node 
                else: 
                    node = node.right.node  
        return node
    
    
    def logical_successor(self, node):
        ''' 
        Find the smallest valued node in RIGHT child
        ''' 
        node = node.right.node  
        if node != None: # just a sanity check  
            
            while node.left != None:
                debug("LS: traversing: " + str(node.key))
                if node.left.node == None: 
                    return node 
                else: 
                    node = node.left.node  
        return node
    

    def check_balanced(self):
        if self == None or self.node == None: 
            return True
        
        # We always need to make sure we are balanced 
        self.update_heights()
        self.update_balances()
        return ((abs(self.balance) < 2) and self.node.left.check_balanced() and self.node.right.check_balanced())
    
        
    def inorder_traverse(self):
        if self.node == None:
            return [] 
        
        inlist = [] 
        l = self.node.left.inorder_traverse()
        for i in l: 
            inlist.append(i) 

        inlist.append(self.node.key)

        l = self.node.right.inorder_traverse()
        for i in l: 
            inlist.append(i) 
    
        return inlist
    

    def display(self, level=0, pref=''):
        '''
        Display the whole tree (but turned 90 degrees counter-clockwisely). Uses recursive def.
        '''        
        self.update_heights()  # Must update heights before balances 
        self.update_balances()  
        if(self.node != None): 
            print ('-' * level * 2, pref, self.node.key, "[" + str(self.height) + ":" + str(self.balance) + "]", 'L' if self.is_leaf() else ' ')    
            if self.node.left != None: 
                self.node.left.display(level + 1, '<')
            if self.node.left != None:
                self.node.right.display(level + 1, '>')



if __name__ == "__main__":
    a = AVLTree()

    print("\nSelect from an option below.")
    print("1. Use a sample list for the tree\n2. Insert integers into a blank tree")
    selec = inputInt()

    while True:
        if selec == 1:
            print("Inputing a list of integers into the AVL Tree:")
            inlist = [55, 81, 65, 20, 35, 79, 23, 14, 21, 103, 92, 45, 85, 51, 47, 48, 50, 46]
            print(inlist)
            print ("----- Inserting -------")
            for i in inlist:
                a.insert(i)
            break

        elif selec == 2:
            inlist = []
            while True:
                new = input("Enter integer to insert or E to end:")
                if new == 'E':
                    break
                else:
                    try:
                        inlist.append(int(new))
                    except ValueError:
                        print('Invalid input.')
            for i in inlist:
                a.insert(i)
            break

        else:
            print('Enter selection (1, 2):')
            selec = inputInt()

    while True:
        print("\nSelect from the menu options below.")
        print("1. Insert a new integer key into the AVL tree\n\
2. Delete an integer key from the AVL tree\n\
3. Print the in-order traversal sequence of the AVL tree\n\
4. Print all leaf nodes of the AVL tree, and all non-leaf nodes (separately)\n\
5. Display the AVL tree, showing the height and balance factor for each node\n\
6. Exit")
        print("Enter selection (1-6):")
        selec = inputInt()

        if selec == 1:
            print("Enter integer to insert:")
            newint = inputInt()
            a.insert(newint)

        elif selec == 2:
            print("Enter a key to delete:")
            delkey = inputInt()
            a.delete(a.node, delkey)
            
        elif selec == 3:
            print("Inorder traversal:", a.inorder_traverse())

        elif selec == 4:
            print("Leaf nodes:")
            a.get_leafs()
            print("\nNon-leaf nodes:")
            a.get_nonleafs()            

        elif selec == 5:
            print("AVL tree:")
            a.display()

        elif selec == 6:
            print('Goodbye!')
            break
    
