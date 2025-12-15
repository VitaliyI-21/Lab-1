import tkinter as tk

def press(key):
    if key == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Помилка")
    elif key == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, key)


# Головне вікно
root = tk.Tk()
root.title("Калькулятор")
root.geometry("300x400")
root.resizable(False, False)

# Поле вводу
entry = tk.Entry(root, font=("Arial", 20), justify="right")
entry.pack(fill=tk.BOTH, ipadx=8, ipady=15, padx=10, pady=10)

# Кнопки
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+",
    "C"
]

frame = tk.Frame(root)
frame.pack()

row = 0
col = 0

for btn in buttons:
    action = lambda x=btn: press(x)
    b = tk.Button(
        frame,
        text=btn,
        font=("Arial", 16),
        width=5,
        height=2,
        command=action
    )
    b.grid(row=row, column=col, padx=5, pady=5)

    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
