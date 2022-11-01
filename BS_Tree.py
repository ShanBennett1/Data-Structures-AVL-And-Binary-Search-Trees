class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0

    # Return True if the element is in the tree
    def search(self, e):
        current = self.root # Start from the root
        counter = 0
        while current != None:
            if e < current.element:
                current = current.left
                counter +=1
            elif e > current.element:
                current = current.right
                counter +=1
            else: # element matches current.element
                #print(counter)
                return True # Element is found

        return False

    # Insert element e into the binary search tree
    # Return True if the element is inserted successfully
    def insert(self, e):
        if self.root == None:
          self.root = self.createNewNode(e) # Create a new root
        else:
          # Locate the parent node
          parent = None
          current = self.root
          while current != None:
            if e < current.element:
              parent = current
              current = current.left
            elif e > current.element:
              parent = current
              current = current.right
            else:
              return False # Duplicate node not inserted

          # Create the new node and attach it to the parent node
          if e < parent.element:
            parent.left = self.createNewNode(e)
          else:
            parent.right = self.createNewNode(e)

        self.size += 1 # Increase tree size
        return True # Element inserted

    # Create a new TreeNode for element e
    def createNewNode(self, e):
      return TreeNode(e)
    """
    # Return the size of the tree
    def getSize(self):
      return self.size"""

    # Inorder traversal from the root
    def inorder(self):
      self.inorderHelper(self.root)

    # Inorder traversal from a subtree
    def inorderHelper(self, r):
      if r != None:
        self.inorderHelper(r.left)
        print(r.element, end = " ")
        self.inorderHelper(r.right)

    # Postorder traversal from the root
    def postorder(self):
      self.postorderHelper(self.root)

    # Postorder traversal from a subtree
    def postorderHelper(self, root):
      if root != None:
        self.postorderHelper(root.left)
        self.postorderHelper(root.right)
        print(root.element, end = " ")

    # Preorder traversal from the root
    def preorder(self):
      self.preorderHelper(self.root)

    # Preorder traversal from a subtree
    def preorderHelper(self, root):
      if root != None:
        print(root.element, end = " ")
        self.preorderHelper(root.left)
        self.preorderHelper(root.right)

    
    # Return true if the tree is empty
    def isEmpty(self):
      return self.size == 0

    # Remove all elements from the tree
    def clear(self):
      self.root == None
      self.size == 0

    # Return the root of the tree
    def getRoot(self):
      return self.root

    # Return the minimum number
    def getMinNum(self, current):
     
        while current.left:
            current = current.left
        return current

    #Count nodes in the tree
    def countNodes(self, e):
        #e = num
        root = self.root
        if root is None:
            return 0 ;
        
        current = self.root
        while current != None:
            if e < current.element:
              current = current.left
            elif e > current.element:
              current = current.right
            else:
                result = self.countNodesHelper(current)
                print("\n\nNumber of nodes:\n",result - 1)
                return                     


    def countNodesHelper(self, root):
        if root is None:
            return 0
        else:
            print(root.element, end = " ")
            l = self.countNodesHelper(root.left)
            r = self.countNodesHelper(root.right)
            return l + r + 1

       
    #Print all leaf nodes in the BST
    def printLeafNodes(self):
        self.printLeafNodesHelper(self.root)

    def printLeafNodesHelper(self, root):

        if (not root):
            return

        if (not root.left and not root.right):
            print(root.element, end = " ")
            return

        if root.left:
            self.printLeafNodesHelper(root.left)

        if root.right:
            self.printLeafNodesHelper(root.right)


    #Print all non leaf nodes in the BST
    def printNonLeafNodes(self):
        self.printNonLeafNodesHelper(self.root)

    def printNonLeafNodesHelper(self, root):

        if (not root):
            return

        if (root.left or root.right):
            print(root.element, end = " ")
            self.printNonLeafNodesHelper(root.left)
            self.printNonLeafNodesHelper(root.right)
            return

        if root.left is None:
            self.printNonLeafNodesHelper(root.left)

        if root.right is None:
            self.printNonLeafNodesHelper(root.right)

    #Get depth of specific node from the BST
    def getDepth(self, num):
        e = num
        root = self.root
        if root is None:
            return 0 ;
            
        current = self.root
        while current != None:
            if e < current.element:             
              current = current.left
            elif e > current.element:             
              current = current.right
            else:
                l = self.depthHelper(current)
                print("Depth of", e, "is", l-1)
                return

    def depthHelper(self, root):
        
        if root is None:
            return 0 ;
        
        else:
            # Find the depth of each subtree
            lDepth = self.depthHelper(root.left)
            rDepth = self.depthHelper(root.right)
 
            # Use the larger one
            if (lDepth > rDepth): 
                return lDepth+1
            else:
                return rDepth+1
      
    #Insert new integer into the BST 
    def insertNewInt(self, num):
        insertNum = self.insert(int(num))
        if insertNum is False:
            print("ERROR: node key already exists in the BST!")
        else:
            print("Number inserted")


    #Delete a specific node from the BST
    def deleteNode(self, delNum):
        self.deleteNodeHelper(self.root,delNum)
        
    def deleteNodeHelper(self, root, delNum): 
        root = self.root
        parent = None
        current = root

        # search number in the binary search tree and set the parent 
        while current and current.element != delNum:
            parent = current

            if delNum < current.element:
                current = current.left
            else:
                current = current.right
        if current is None:
            print("ERROR: Node ",delNum, " Not found")
            return root

        # Node to be deleted is a leaf node
        if current.left is None and current.right is None:

            if current != root:
                if parent.left == current:
                    parent.left = None
                else:
                    parent.right = None
            else:
                self.root = None

        # Node to be deleted has 2 children
        elif current.left and current.right:
            successor = self.getMinNum(current.right)
            val = successor.element
            self.deleteNodeHelper(root, successor.element)
            current.element = val

        # Node to be deleted has one child
        else:
            if current.left:
                child = current.left
            else:
                child = current.right

            if current != root:
                if current == parent.left:
                    parent.left = child
                else:
                    parent.right = child
            else:
                self.root = child
       
        return root


class TreeNode:
    def __init__(self, e):
      self.element = e
      self.left = None # Point to the left node, default None
      self.right = None # Point to the right node, default None

##### Main code

def main():
    intTree = BinaryTree()
    selection = 0
    
    while True:
        print("Please select an option")
        print("1) Pre-load integers to build a BST: ")
        print("2) Manually enter integer values to build a BST: ")
        selection = input("> ")
        if selection == "1":
            numbers = [55, 81, 65, 20, 35, 79, 23, 14, 21, 103, 92, 45, 85, 51, 47, 48, 50, 46]
            for e in numbers:
                intTree.insert(e)
            break

        elif selection == "2":
            number = ""
            numbers = []
            while number != "x":
                number = input("Enter a number (enter X when done): ")
                if number.lower() == "x":
                    break
                else:
                    numbers.append(int(number))
    
            for e in numbers:
              intTree.insert(e)
              selection == 0
            break
        
        else:
            print("\nInvalid input! Try again \n")
           
    selection = 0
    while selection != 7:
        print("\n\nPlease select an option")
        print("1) Print the pre-order, in-order, and post-order of the BST")
        print("2) Print all leaf nodes of the BST, and all non-leaf nodes")
        print("3) Print the total number of nodes of a sub-tree")
        print("4) Print the depth of a subtree rooted at a particular node")
        print("5) Insert a new integer key into the BST")
        print("6) Delete an integer key from the BST")
        print("7) Exit")
        selection = input("> ")

        if selection == "1":
            
            print("\nPreorder traversal:")
            intTree.preorder()
            print("\n\nInorder traversal:")
            intTree.inorder()
            print("\n\nPostorder traversal:")
            intTree.postorder()

        elif selection == "2":
            print("\n\nLeaf Nodes:")
            intTree.printLeafNodes()
            print("\n\nNonLeaf Nodes:")
            intTree.printNonLeafNodes()

        elif selection == "3":
            num = int(input("Please enter the node number: "))
            print("\n\nNodes:")
            if intTree.search(num) is False:
                print("Error: node ", num, "not found!")
            else:
                intTree.countNodes(int(num))

        elif selection == "4":
            print("Enter a number: ")
            num = int(input("> "))
            if intTree.search(num) is False:
                print("Error: node ", num, "not found!")
            else:
                intTree.getDepth(num)
            
        elif selection == "5":
            print("Enter a number to insert")
            insNum = int(input("> "))
            intTree.insertNewInt(insNum)

        elif selection == "6":
            print("Enter a number to delete")
            delNum = int(input("> "))
            intTree.deleteNode(int(delNum))
            
        elif selection == "7":
            print("Goodbye!")
            break

        elif selection == "8":
            print("entire tree root is: ", intTree.root.element)

        else:
            print("\nInvalid input! Try again \n")


      
if __name__ == "__main__":
    main() 
