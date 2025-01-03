class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListShoppingListManagerClass:
    def __init__(self):
        self.head = None

    def insert_item(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

    def print_items(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def delete_item(self, item):
        current = self.head
        previous = None
        while current:
            if current.data == item:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                return
            previous = current
            current = current.next
        print(f"Item '{item}' not found in the shopping list.")

    def get_last_item(self):
        current = self.head
        if not current:
            return None
        while current.next:
            current = current.next
        return current.data

    def find_smallest(self):
        if not self.head:
            return None
        smallest = self.head.data
        current = self.head.next
        while current:
            if current.data < smallest:
                smallest = current.data
            current = current.next
        return smallest

    def selection_sort(self):
        current = self.head
        while current:
            min_node = current
            next_node = current.next
            while next_node:
                if next_node.data < min_node.data:
                    min_node = next_node
                next_node = next_node.next
            current.data, min_node.data = min_node.data, current.data
            current = current.next
