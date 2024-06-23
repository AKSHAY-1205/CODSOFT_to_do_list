import tkinter as tk
from tkinter import messagebox

class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = 'Completed' if self.completed else 'Pending'
        return f"{self.description} - {status}"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks.pop(task_index)

    def get_tasks(self):
        return self.tasks

    def __str__(self):
        tasks_str = '\n'.join([f"{i + 1}. {str(task)}" for i, task in enumerate(self.tasks)])
        return f"Tasks:\n{tasks_str}"

class ToDoListApp:
    def __init__(self, root):
        self.to_do_list = ToDoList()

        self.root = root
        self.root.title("To-Do List Application")

        self.task_entry = tk.Entry(root, width=50)
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.tasks_listbox = tk.Listbox(root, width=50, height=10)
        self.tasks_listbox.pack(pady=10)

        self.complete_button = tk.Button(root, text="Mark as Completed", command=self.mark_completed)
        self.complete_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.update_tasks_listbox()

    def add_task(self):
        task_description = self.task_entry.get()
        if task_description:
            task = Task(task_description)
            self.to_do_list.add_task(task)
            self.update_tasks_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task description")

    def mark_completed(self):
        selected_task_index = self.tasks_listbox.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            self.to_do_list.tasks[index].mark_completed()
            self.update_tasks_listbox()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to mark as completed")

    def delete_task(self):
        selected_task_index = self.tasks_listbox.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            self.to_do_list.remove_task(index)
            self.update_tasks_listbox()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to delete")

    def update_tasks_listbox(self):
        self.tasks_listbox.delete(0, tk.END)
        for task in self.to_do_list.get_tasks():
            self.tasks_listbox.insert(tk.END, str(task))

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
