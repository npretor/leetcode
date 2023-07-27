import random 


class TreeNode:
    """
    Defaults to left-hand, then right. No sorting
    """
    def __init__(self, val) -> None:
        self.val = val
        self.left = None 
        self.right = None 

    def add(self, node):
        # If the left and right are full 
        if self.left and self.right:
            self.left.add(node)

        elif self.left and self.right == None:
            self.right = node 

        else:
            self.left = node 

class sortedNode:
    def __init__(self, val) -> None:
        self.val = val 
        self.left = None 
        self.right = None 

    def add(self, node):
        """
        If something is being added: 
            Check if any sub-nodes exist. 
        """
        
        # If value is larger than node, go right, else to left 
        if node.val == self.val:
            pass 
        
        if node.val > self.val:
            if self.left:
                self.left.add(node)
            else:
                self.left = node 

        if node.val < self.val:
            if self.right:
                self.right.add(node)
            else:
                self.right = node 

def randomIntTree():
    # Create random number list to add 
    n = 20
    randos = [random.randint(0, 100) for i in range(0, n)]

    # Populate tree  
    root = TreeNode(randos[0])
    for num in randos[1:]:
        root.add(TreeNode(num)) 

    return root 

def printTree(root, depth):
    
    spacing = '-'*depth
    print(spacing, root.val) 

    if root.left:
        printTree(root.left, depth+1) 
    if root.right:
        printTree(root.right, depth+1)   


# Make the tree 
# tree_root = randomIntTree()
# Print out 
# printTree(tree_root, 0)  


def sortedIntTree():
    n = 20
    randos = [random.randint(0, 100) for i in range(0, n)]

    root = sortedNode(randos[0]) 
    for num in randos[1:]:
        root.add(sortedNode(num))     

    return root 


t = sortedIntTree() 

printTree(t, 0)