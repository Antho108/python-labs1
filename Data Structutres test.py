class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __repr__(self):
        return f"Node({self.value})"


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def get_node(self, index):
        if index < 0 or index >= self.length:
            return None
        current_node = self.head
        for i in range(index):
            current_node = current_node.next
        return current_node

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.value))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
    

    # Create a new linked list
ll = LinkedList()


# Append a couple of nodes to the linked list
ll.append(10)
ll.append(20)
ll.append(30)

# Visualize list 
print(ll)

# Prepend a node to the list
ll.prepend(1)
print(ll)  # 5 -> 10 -> 20 -> 30 -> None

# Get the node at index 1
node = ll.get_node(1)
print(node.value)  # 10

# Show the node's string representation
print(node)  # Node(10)