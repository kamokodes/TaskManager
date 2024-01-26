import tkinter as tk
from tkinter import messagebox

class TaskManager:
    def __init__(self, master):
        self.master = master
        self.master.title("Task Manager")

        self.tasks = []

        self.task_entry = tk.Entry(master, width=40)
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.task_listbox = tk.Listbox(master, width=40, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10)

        self.remove_button = tk.Button(master, text="Remove Task", command=self.remove_task)
        self.remove_button.pack()

        self.clear_button = tk.Button(master, text="Clear All", command=self.clear_tasks)
        self.clear_button.pack()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def remove_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            self.task_listbox.delete(selected_index)
            self.tasks.pop(selected_index[0])

    def clear_tasks(self):
        confirmed = messagebox.askyesno("Confirmation", "Are you sure you want to clear all tasks?")
        if confirmed:
            self.tasks = []
            self.task_listbox.delete(0, tk.END)

def main():
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()

if __name__ == "__main__":
    main()
