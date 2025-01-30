class ListNode:
    """Node class for singly linked list."""
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class LinkedListWithHash:
    """Singly linked list combined with a hash table for O(1) access."""
    def __init__(self):
        self.head = None
        self.tail = None
        self.node_map = {}  # Hash table to store key -> node references

    def add_node(self, key, value):
        """Adds a new node at the end of the linked list in O(1) time."""
        new_node = ListNode(key, value)
        if self.tail:
            self.tail.next = new_node  
        else:
            self.head = new_node  
        self.tail = new_node 

        # Store reference in hash table for O(1) access
        self.node_map[key] = new_node

    def insert_after(self, existing_key, key, value):
        """
        Inserts a new node after an existing node identified by the key.
        Lookup is O(1) due to hash table storage.
        """
        if existing_key not in self.node_map:
            print(f"Key {existing_key} not found.")
            return

        existing_node = self.node_map[existing_key]
        new_node = ListNode(key, value)

        # Insert after the existing node
        new_node.next = existing_node.next
        existing_node.next = new_node

        # If inserting at the end, update tail pointer
        if existing_node == self.tail:
            self.tail = new_node

        # Store reference in hash table for O(1) lookup
        self.node_map[key] = new_node

    def get_value(self, key):
        """Retrieve value from the linked list in O(1) using hash table."""
        if key in self.node_map:
            return self.node_map[key].value
        return None

    def display(self):
        """Print the linked list values."""
        current = self.head
        while current:
            print(f"({current.key}: {current.value})", end=" -> ")
            current = current.next
        print("None")

# Example usage
ll_hash = LinkedListWithHash()
ll_hash.add_node(1, "One")
ll_hash.add_node(2, "Two")
ll_hash.add_node(3, "Three")

print("Initial list:")
ll_hash.display()

# Insert after key 2 in O(1)
ll_hash.insert_after(2, 4, "Four")
print("After inserting 4 after 2:")
ll_hash.display()

# Accessing values in O(1)
print("Value of key 3:", ll_hash.get_value(3))
