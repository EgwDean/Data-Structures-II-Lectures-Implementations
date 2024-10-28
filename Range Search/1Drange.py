'''

Πράξεις search και insert σε φυλλοπροσανατολισμενο δεντρο
σύμφωνα με τον αλγόριθμο στο βιβλίο του Τσακαλίδη (δες σελ.35)


Υλοποίηση 1D Range Search - Η αργή μέθοδος:
            Βήμα 1: postorder traversal για δημιουργία linked list των φύλλων
            Βήμα 2: Αναζήτηση στη λίστα στο επιθυμητό range

Total complexity: postorder + list access = O(n) + O(k) = O(n)     --> ΑΥΤΗ ΥΛΟΠΟΙΕΙΤΑΙ ΠΑΡΑΚΑΤΩ !!!


Υλοποίηση 1D Range Search με χρήση right-left turns και Linked list για τα φύλλα
Η μέθοδος που περιγράφεται στις διαφάνειες μαθήματος:
            Βήμα 1:  Search(x) 
            Βήμα 2:  Search(y)
            Βήμα 3:  Επιστροφή των x, y και όλων των υπόλοιπων ενδιάμεσων φύλλων με χρήση right-left turns.
            
'''


class TreeNode:
    def __init__(self, key=None):
        self.key = key
        self.left = None
        self.right = None


class LinkedListNode:
    def __init__(self, key=None):
        self.key = key
        self.next = None


class BinarySearchTree:
    def __init__(self):
        self.root = None     # root node
        self.head = None     # Head of the linked list
        self.current = None  # Pointer to the current node in the linked list

    def insert(self, x):
        if self.root is None:
            self.root = TreeNode(x)  # Create the root if the tree is empty
        else:
            last_node = self.search(x)  # Get the last node visited during search
            if last_node.key == x:
                print("The value you want to insert already exists.")  # Value already exists
                return
            else:
                
                # Tsakalidis method
                minValue = min(x, last_node.key)
                maxValue = max(x, last_node.key)

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

    # Function to visualize the leaf-oriented tree
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
            print(f"Leaf node I end up searching for {x_value}:")
            self.display(x_node)
        else:
            print(f"{x_value} not found in the tree.")

        if y_node is not None:
            print(f"Leaf node I end up searching for {y_value}:")
            self.display(y_node)
        else:
            print(f"{y_value} not found in the tree.")

   

    def create_leaf_linked_list(self):
        self.head = None
        self.current = None

        def post_order(node):
            if node is None:
                return

            post_order(node.left)   # Visit left subtree
            post_order(node.right)  # Visit right subtree

            # Check if it's a leaf node
            if node.left is None and node.right is None:
                new_node = LinkedListNode(node.key)
                if self.head is None:
                    self.head = new_node       # First leaf node
                    self.current = self.head
                else:
                    self.current.next = new_node  # Link new node
                    self.current = new_node       # Move current pointer

        post_order(self.root)

    
    
    def print_leaf_linked_list(self):
        current = self.head
        print("Linked List of Leaf Nodes:", end=" ")
        while current is not None:
            print(current.key, end=" -> ")
            current = current.next
        print("None")
        
        


    def find_elements_in_range(self, min_val, max_val):
        # Initialize the result list
        result = []
        # Start from the head of the linked list
        current = self.head
        # Traverse through the linked list
        while current is not None:
            # Check if the current node's key is within the specified range
            if min_val <= current.key <= max_val:
                result.append(current.key)
            # Move to the next node
            current = current.next
        return result




# Example usage:
bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(20)
bst.insert(30)
bst.insert(9)
bst.insert(17)

# Display the tree structure
print("Binary Search Tree Structure:")
bst.display(bst.root)

# Create linked list of leaf nodes
bst.create_leaf_linked_list()                 # O(n) complexity
bst.print_leaf_linked_list()

#bst.Search1d(7, 22)                                                       

result = bst.find_elements_in_range(7, 22)    # O(n) complexity
print(result)                                            
