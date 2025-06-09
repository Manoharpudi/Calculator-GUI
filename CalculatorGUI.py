import tkinter as tk
from tkinter import messagebox

def calculator(op):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            if num2 == 0:
                messagebox.showerror("Error", "Can't divide with Zero")
                return
            result = num1 / num2
        else:
            messagebox.showerror("Error", "Enter valid operator")

        result_label.config(text=f"Result: {result}")

    except ValueError:
        messagebox.showerror("Error", "Enter Numeric Value")

def clear():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result_label.config(text='Result:')

root = tk.Tk()
root.title("Calculator")
root.configure(bg="white")

tk.Label(root, text="Enter the First Number", bg='white').grid(row=0, column=0, padx=20, pady=10, sticky='w')
entry1 = tk.Entry(root, width=20, bd=2, relief='solid')
entry1.grid(row=0, column=1, pady=10)
tk.Label(root, text="Enter the Second Number", bg='white').grid(row=1, column=0, padx=20, pady=10, sticky='w')
entry2 = tk.Entry(root, width=20, bd=2, relief='solid')
entry2.grid(row=1, column=1, pady=10)

btn_frame = tk.Frame(root, bg='white')
btn_frame.grid(row=2, column=0, columnspan=2, padx=20, pady=10, sticky='w')

for i, op in enumerate(["+", "-", "*", "/"]):
    tk.Button(btn_frame, text=op, width=5, bd=2, relief='solid', command=lambda o=op: calculator(o)).grid(row=0, column=i, padx=5)

tk.Button(root, text="Clear", command=clear, width=10, bd=2, relief='solid', bg='white').grid(row=3, column=0, columnspan=2, padx=20, pady=10, sticky='w')

result_label = tk.Label(root, text="Result:", bg='white')
result_label.grid(row=4, column=0, columnspan=2, padx=20, pady=10, sticky='w')

root.mainloop()