class SimpleArrayShoppingListManagerClass:
    def __init__(self):
        self.shopping_list = []

    def insert_item(self, item):
        self.shopping_list.insert(0, item)

    def print_items(self):
        print(self.shopping_list)

    def delete_item(self, item):
        try:
            index = self.shopping_list.index(item)
            self.shopping_list.pop(index)
        except ValueError:
            print(f"Item '{item}' not found in the shopping list.")

    def get_last_item(self):
        if self.shopping_list:
            return self.shopping_list[-1]
        return None

    def selection_sort(self):
        n = len(self.shopping_list)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if self.shopping_list[j] < self.shopping_list[min_index]:
                    min_index = j
            self.shopping_list[i], self.shopping_list[min_index] = self.shopping_list[min_index], self.shopping_list[i]
