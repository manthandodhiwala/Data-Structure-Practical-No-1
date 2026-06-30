import tkinter as tk
from tkinter import messagebox


class Stack:
    def __init__(self):
        self.name_stack = []

    def push(self, name):
        self.name_stack.append(name)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from an empty stack!")
        return self.name_stack.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from an empty stack!")
        return self.name_stack[-1]

    def is_empty(self):
        return len(self.name_stack) == 0

    def size(self):
        return len(self.name_stack)


class StackGUI:
    def __init__(self, root):
        self.stack = Stack()

        root.title("Student Stack Operations")
        root.geometry("500x500")
        root.config(bg="lightblue")

        title = tk.Label(
            root,
            text="STUDENT STACK OPERATIONS",
            font=("Arial", 18, "bold"),
            bg="lightblue",
            fg="darkblue",
        )
        title.pack(pady=10)

        tk.Label(root, text="Enter Student Name:",
                 bg="lightblue",
                 font=("Arial", 12)).pack()

        self.entry = tk.Entry(root, width=30, font=("Arial", 12))
        self.entry.pack(pady=5)

        tk.Button(root, text="Push", width=20, bg="green", fg="white",
                  command=self.push).pack(pady=5)

        tk.Button(root, text="Pop", width=20, bg="red", fg="white",
                  command=self.pop).pack(pady=5)

        tk.Button(root, text="Peek", width=20, bg="orange",
                  command=self.peek).pack(pady=5)

        tk.Button(root, text="Is Empty?", width=20, bg="purple",
                  fg="white", command=self.is_empty).pack(pady=5)

        tk.Button(root, text="Stack Size", width=20, bg="blue",
                  fg="white", command=self.size).pack(pady=5)

        tk.Label(root, text="Current Stack",
                 font=("Arial", 14, "bold"),
                 bg="lightblue").pack(pady=10)

        self.listbox = tk.Listbox(root, width=35, height=10,
                                  font=("Arial", 12))
        self.listbox.pack()

    def update_stack(self):
        self.listbox.delete(0, tk.END)
        for item in reversed(self.stack.name_stack):
            self.listbox.insert(tk.END, item)

    def push(self):
        name = self.entry.get().strip()

        if name == "":
            messagebox.showwarning("Warning", "Please enter a student name.")
            return

        self.stack.push(name)
        self.update_stack()
        self.entry.delete(0, tk.END)
        messagebox.showinfo("Success", f"{name} has been pushed into the stack.")

    def pop(self):
        try:
            name = self.stack.pop()
            self.update_stack()
            messagebox.showinfo("Pop", f"{name} has been popped from the stack.")
        except IndexError as e:
            messagebox.showerror("Error", str(e))

    def peek(self):
        try:
            messagebox.showinfo("Top Item", self.stack.peek())
        except IndexError as e:
            messagebox.showerror("Error", str(e))

    def is_empty(self):
        if self.stack.is_empty():
            messagebox.showinfo("Stack", "The stack is empty.")
        else:
            messagebox.showinfo("Stack", "The stack is not empty.")

    def size(self):
        messagebox.showinfo("Stack Size",
                            f"Number of items: {self.stack.size()}")


# Main Program
root = tk.Tk()
app = StackGUI(root)
root.mainloop()
