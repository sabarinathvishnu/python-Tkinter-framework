import tkinter as tk
from tkinter import messagebox


class ShoppingListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Shopping List")

        self.item_entry = tk.Entry(root, width=40)
        self.item_entry.grid(row=0, column=0, padx=10, pady=10)

        self.add_button = tk.Button(root, text="Add Item", command=self.add_item)
        self.add_button.grid(row=0, column=1, padx=10, pady=10)

        self.remove_button = tk.Button(root, text="Remove Item", command=self.remove_item)
        self.remove_button.grid(row=1, column=1, padx=10, pady=10)

        self.clear_button = tk.Button(root, text="Clear List", command=self.clear_list)
        self.clear_button.grid(row=2, column=1, padx=10, pady=10)

        self.item_listbox = tk.Listbox(root, width=50, height=15)
        self.item_listbox.grid(row=1, column=0, rowspan=2, padx=10, pady=10)

    def add_item(self):
        item = self.item_entry.get().strip()
        if item:
            self.item_listbox.insert(tk.END, item)
            self.item_entry.delete(0, tk.END)
            self.item_entry.focus()
        else:
            messagebox.showwarning("Input Error", "Cannot add an empty item.")

    def remove_item(self):
        try:
            selected_index = self.item_listbox.curselection()[0]
            self.item_listbox.delete(selected_index)
        except IndexError:
            messagebox.showwarning("Selection Error", "No item selected.")

    def clear_list(self):
        self.item_listbox.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ShoppingListApp(root)
    root.mainloop()
