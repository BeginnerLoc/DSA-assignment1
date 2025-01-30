class Node:
    def __init__(self, label, value):
        self.label = label     # A unique "index" (may skip numbers to allow insertion)
        self.value = value
        self.next = None       # Singly linked pointer to the next node

class O1LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
        # Dictionary to map label -> { 'node': node_object, 'pred': predecessor_label }
        self.index_map = {}

        # We'll space out labels to avoid renumbering many nodes on insert
        self.label_step = 10
        self.next_label = 10

    def _update_map(self, label, node, pred_label):
        """Store (node, predecessor) in the dictionary for O(1) lookups."""
        self.index_map[label] = {
            'node': node,
            'pred': pred_label
        }

    def get(self, label):
        """
        Return the value at 'label' in O(1).
        """
        entry = self.index_map.get(label)
        if entry:
            return entry['node'].value
        return None  # or raise an exception if desired

    def add_end(self, value):
        """
        Add a new node at the end of the list in O(1).
        We'll assign it the current 'next_label' and increment.
        """
        new_node = Node(self.next_label, value)
        
        if not self.head:
            # List is empty
            self.head = new_node
            self.tail = new_node
            pred_label = None
        else:
            # Link after the tail
            self.tail.next = new_node
            pred_label = self.tail.label
            self.tail = new_node

        # Update our index_map
        self._update_map(self.next_label, new_node, pred_label)
        self.next_label += self.label_step  # Move label generator forward

    def insert_after(self, existing_label, new_label, value):
        """
        Insert a new node AFTER the node with 'existing_label' in O(1).
        """
        entry = self.index_map.get(existing_label)
        if not entry:
            raise KeyError(f"Label {existing_label} not found.")

        existing_node = entry['node']
        pred_label = existing_label

        new_node = Node(new_label, value)
        new_node.next = existing_node.next
        existing_node.next = new_node

        # If we inserted after the tail, update the tail reference
        if existing_node == self.tail:
            self.tail = new_node

        # Update map for the new node
        self._update_map(new_label, new_node, pred_label)

        # If there is a next node, its predecessor label is now 'new_label'
        if new_node.next:
            nxt_label = new_node.next.label
            self.index_map[nxt_label]['pred'] = new_label

    def remove(self, label):
        """
        Remove the node at 'label' in O(1).
        """
        entry = self.index_map.get(label)
        if not entry:
            raise KeyError(f"Label {label} not found.")

        node_to_remove = entry['node']
        pred_label = entry['pred']

        # Case 1: Removing the head
        if pred_label is None:
            self.head = node_to_remove.next
            # Update the new head's predecessor if there's a new head
            if self.head:
                self.index_map[self.head.label]['pred'] = None
        else:
            # We have a valid predecessor
            pred_node = self.index_map[pred_label]['node']
            pred_node.next = node_to_remove.next

            # If removing tail, update tail
            if node_to_remove == self.tail:
                self.tail = pred_node
            else:
                # Update the next node's predecessor
                if node_to_remove.next:
                    next_label = node_to_remove.next.label
                    self.index_map[next_label]['pred'] = pred_label

        # Remove from the dictionary
        del self.index_map[label]

    def display(self):
        """
        Print the singly linked list in order, using .next pointers.
        """
        current = self.head
        while current:
            print(f"({current.label}: {current.value}) -> ", end="")
            current = current.next
        print("None")

# Example usage:
if __name__ == "__main__":
    # Create the list
    sll = O1LinkedList()

    # Add some nodes
    sll.add_end("A")  # label=10
    sll.add_end("B")  # label=20
    sll.add_end("C")  # label=30
    sll.display()
    # (10: A) -> (20: B) -> (30: C) -> None

    # Insert a new node with label=15 after label=10
    sll.insert_after(10, 15, "A2")
    sll.display()
    # (10: A) -> (15: A2) -> (20: B) -> (30: C) -> None

    # Get the value at label=15
    print("Value at 15:", sll.get(15))  # A2

    # Remove the node at label=20
    sll.remove(20)
    sll.display()
    # (10: A) -> (15: A2) -> (30: C) -> None
