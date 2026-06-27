Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import tkinter as tk
... from tkinter import messagebox
... import threading
... import time
... from datetime import datetime
... 
... # Global list to store tasks
... tasks = []
... 
... def add_task():
...     task = task_entry.get()
...     reminder_time = reminder_entry.get()
...     if task:
...         tasks.append((task, reminder_time))
...         task_list.insert(tk.END, f"{task} (Reminder: {reminder_time})")
...         task_entry.delete(0, tk.END)
...         reminder_entry.delete(0, tk.END)
...     else:
...         messagebox.showwarning("Warning", "Please enter a task!")
... 
... def delete_task():
...     try:
...         selected_index = task_list.curselection()[0]
...         task_list.delete(selected_index)
...         tasks.pop(selected_index)
...     except IndexError:
...         messagebox.showwarning("Warning", "Please select a task to delete!")
... 
... def check_reminders():
...     while True:
...         now = datetime.now().strftime("%H:%M")
...         for task, reminder_time in tasks:
...             if reminder_time == now:
...                 messagebox.showinfo("Reminder", f"Time for: {task}")
...         time.sleep(60)  # check every minute
... 
... # GUI setup
root = tk.Tk()
root.title("To-Do List with Reminders")

frame = tk.Frame(root)
frame.pack(pady=10)

task_entry = tk.Entry(frame, width=30)
task_entry.grid(row=0, column=0, padx=5)

reminder_entry = tk.Entry(frame, width=10)
reminder_entry.grid(row=0, column=1, padx=5)
reminder_entry.insert(0, "HH:MM")

add_button = tk.Button(frame, text="Add Task", command=add_task)
add_button.grid(row=0, column=2, padx=5)

delete_button = tk.Button(frame, text="Delete Task", command=delete_task)
delete_button.grid(row=0, column=3, padx=5)

task_list = tk.Listbox(root, width=50, height=10)
task_list.pack(pady=10)

# Start reminder thread
reminder_thread = threading.Thread(target=check_reminders, daemon=True)
reminder_thread.start()

