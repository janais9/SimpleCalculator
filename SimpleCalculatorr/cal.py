import tkinter as tk

def click_button(value):
    entry_var.set(entry_var.get() + str(value))
def calculate():
    try:
        result = str(eval(entry_var.get()))
        entry_var.set(result)
    except:
        entry_var.set("Error")

def clear():
    entry_var.set("")

root = tk.Tk()
root.title("Jana Calculator")

entry_var = tk.StringVar()

entry = tk.Entry(root, textvariable=entry_var, font=('Arial', 20), bd=5, relief='ridge', justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row = 1
col = 0
for button in buttons:
    if button == '=':
        tk.Button(root, text=button, width=5, height=2, font=('Arial', 15),bg='lightblue', fg='green', command=calculate).grid(row=row, column=col, padx=5, pady=5)
    else:
        tk.Button(root, text=button, width=5, height=2, font=('Arial', 15),
                  command=lambda b=button: click_button(b)).grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

tk.Button(root, text='C', width=5, height=2, font=('Arial', 15), bg='blue', fg='black',command=clear).grid(row=row, column=0, padx=5, pady=5)

root.mainloop()
