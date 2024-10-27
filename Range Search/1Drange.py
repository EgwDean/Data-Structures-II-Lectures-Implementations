
'''

Πράξεις search και insert σε φυλλοπροσανατολισμενο δεντρο
σύμφωνα με τον αλγόριθμο στο βιβλίο του Τσακαλίδη (δες σελ.35)

Υλοποίηση 1D Range Search χωρίς Linked list (θα προστεθεί)
Η μέθοδος περιγράφεται στις διαφάνειες μαθήματος:
            Βήμα 1:  Search(x) 
            Βήμα 2:  Search(y)
            Βήμα 3:  Επιστροφή των x, y και όλων των υπόλοιπων ενδιάμεσων φύλλων (μέσω της Linked list)

'''

class TreeNode:
    def __init__(self, key=None):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, x):
        if self.root is None:
            self.root = TreeNode(x)  # Create the root if the tree is empty
        else:
            last_node = self.search(x)  # Get the last node visited during search
            if last_node.key == x:
                print("The value you want to insert already exists.")  # Value already exists
                return
         
            else:
                minValue = min(x,last_node.key)
                maxValue = max(x,last_node.key)
                last_node.key = minValue
                last_node.left = TreeNode(minValue)
                last_node.right = TreeNode(maxValue)
            
            
     
    def search(self, x):
        return self._search_recursive(self.root, x)

    def _search_recursive(self, node, x):
        if node is None:
            return None  # If the node is None, return None

        elif x <= node.key:
            if node.left is None:
                return node  # If there's no left child, return current node
            return self._search_recursive(node.left, x)  # Continue searching left
        else:  # x > node.key
            if node.right is None:
                return node  # If there's no right child, return current node
            return self._search_recursive(node.right, x)  # Continue searching right
   

   
    # Function to visualize the leaf-oriented tree(ChatGPT)
    def display(self, node, prefix="", is_left=True):
        if node is not None:
            # Display the right child first
            self.display(node.right, prefix + ("|   " if is_left else "    "), False)
            # Print the current node
            print(prefix + ("└── " if not is_left else "┌── ") + str(node.key))
            # Display the left child
            self.display(node.left, prefix + ("    " if is_left else "|   "), True)

    def Search1d(self, x_value, y_value):
        x_node = self.search(x_value)
        y_node = self.search(y_value)
       
        if x_node is not None:
            print(f"Leaf node i end up, searching for {x_value}:")
            self.display(x_node)  
        else:
            print(f"{x_value} not found in the tree.")

        if y_node is not None:
            print(f"Leaf node i end up, searching for {y_value}:")
            self.display(y_node)  
        else:
            print(f"{y_value} not found in the tree.")

# Example usage:
bst = BinarySearchTree()
bst.insert(10)
bst.insert(20)
bst.insert(5)
bst.insert(30)
bst.insert(9)
bst.insert(17)

# Display the tree structure
print("Binary Search Tree Structure:")
bst.display(bst.root)

bst.Search1d(9,25)

print(f"\nHow do i print the leaf nodes in between?")
