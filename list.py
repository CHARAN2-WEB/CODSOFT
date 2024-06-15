import tkinter as tk
from tkinter import messagebox, simpledialog

class ToDoApp:
    def __init__(self, root):
        self.tasks = []
        self.root = root
        self.root.title("To-Do List")

        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)

        self.listbox = tk.Listbox(self.frame, width=50, height=15)
        self.listbox.pack(side=tk.LEFT)

        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

        self.entry = tk.Entry(self.root, width=50)
        self.entry.pack(pady=10)

        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.update_button = tk.Button(self.root, text="Update Task", command=self.update_task)
        self.update_button.pack(pady=5)

        self.delete_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=5)

    def add_task(self):
        task = self.entry.get()
        if task != "":
            self.listbox.insert(tk.END, task)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def update_task(self):
        try:
            index = self.listbox.curselection()[0]
            task = simpledialog.askstring("Update Task", "Enter the new task:", initialvalue=self.listbox.get(index))
            if task:
                self.listbox.delete(index)
                self.listbox.insert(index, task)
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task.")

    def delete_task(self):
        try:
            index = self.listbox.curselection()[0]
            self.listbox.delete(index)
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
