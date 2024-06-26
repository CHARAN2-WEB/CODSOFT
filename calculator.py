import tkinter as tk

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")
root = tk.Tk()
root.title("Arithmetic Calculator")
entry = tk.Entry(root, width=20, font=('Arial', 14))
entry.grid(row=0, column=0, columnspan=4)
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row_val = 1
col_val = 0
for button in buttons:
    action = lambda x=button: entry.insert(tk.END, x) if x not in ['=', 'C'] else calculate() if x == '=' else entry.delete(0, tk.END)
    tk.Button(root, text=button, width=5, height=2, command=action).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1
root.mainloop()
