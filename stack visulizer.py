import tkinter as tk
from tkinter import messagebox

stack = []

def update_display():
    for widget in stack_frame.winfo_children():
        widget.destroy()

    for value in reversed(stack):
        box = tk.Label(
            stack_frame,
            text=str(value),
            width=20,
            height=2,
            bg="#cfe2f3",
            font=("Arial", 14),
            relief="solid",
            bd=1
        )
        box.pack(pady=5)

def push():
    value = entry.get()
    if value == "":
        return

    stack.append(value)
    entry.delete(0, tk.END)
    update_display()
    status.config(text="Pushed " + str(value))

def pop():
    if len(stack) == 0:
        messagebox.showwarning("Stack", "Stack Underflow")
        return

    value = stack.pop()
    update_display()
    status.config(text="Popped " + str(value))

def peek():
    if len(stack) == 0:
        messagebox.showwarning("Stack", "Stack Empty")
        return

    messagebox.showinfo("Top Element", stack[-1])

def clear_stack():
    stack.clear()
    update_display()
    status.config(text="Stack Cleared")

root = tk.Tk()
root.title("Stack Visualizer")
root.geometry("400x500")

top_frame = tk.Frame(root)
top_frame.pack(pady=10)

tk.Label(top_frame, text="Value").grid(row=0, column=0, padx=5)

entry = tk.Entry(top_frame, width=10)
entry.grid(row=0, column=1, padx=5)

push_btn = tk.Button(top_frame, text="Push", width=8, command=push)
push_btn.grid(row=0, column=2, padx=5)

pop_btn = tk.Button(top_frame, text="Pop", width=8, command=pop)
pop_btn.grid(row=0, column=3, padx=5)

peek_btn = tk.Button(top_frame, text="Peek", width=8, command=peek)
peek_btn.grid(row=0, column=4, padx=5)

clear_btn = tk.Button(top_frame, text="Clear", width=8, command=clear_stack)
clear_btn.grid(row=0, column=5, padx=5)

stack_frame = tk.Frame(root)
stack_frame.pack(pady=20)

status = tk.Label(root, text="", anchor="w")
status.pack(fill="x", side="bottom")

root.mainloop()