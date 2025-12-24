import tkinter as tk

COLOR_BG = "#1e1e1e"
COLOR_ENTRY_BG = "#2d2d2d"
COLOR_TEXT = "#ffffff"
COLOR_BTN_NUM = "#333333"
COLOR_BTN_OPS = "#ff9500"
COLOR_BTN_SPECIAL = "#a5a5a5"
COLOR_ERROR = "#ff4b4b"


def on_click(button_text):
    entry.config(bg=COLOR_ENTRY_BG)

    current_text = entry.get()

    if button_text == "=":
        try:
            result = eval(current_text)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            show_error_state()

    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        if current_text == "Error":
            entry.delete(0, tk.END)
        entry.insert(tk.END, button_text)


def show_error_state():
    entry.delete(0, tk.END)
    entry.insert(tk.END, "Error")
    entry.config(bg=COLOR_ERROR)

root = tk.Tk()
root.title("Sleek Calc")
root.geometry("320x480")
root.configure(bg=COLOR_BG)

entry = tk.Entry(root, font=("Helvetica", 32), bg=COLOR_ENTRY_BG, fg=COLOR_TEXT,
                 borderwidth=10, relief="flat", justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=20, pady=40, sticky="nsew")

buttons = [
    'C', '/', '*', '-',
    '7', '8', '9', '+',
    '4', '5', '6', '=',
    '1', '2', '3', '0'
]

row_val = 1
col_val = 0

for button in buttons:
    # Color Logic
    if button in ['/', '*', '-', '+', '=']:
        bg_color = COLOR_BTN_OPS
    elif button == 'C':
        bg_color = COLOR_BTN_SPECIAL
    else:
        bg_color = COLOR_BTN_NUM

    btn = tk.Button(root, text=button, font=("Helvetica", 16, "bold"),
                    bg=bg_color, fg=COLOR_TEXT, borderwidth=0,
                    activebackground="#555555", activeforeground="white",
                    cursor="hand2",
                    command=lambda x=button: on_click(x))

    btn.grid(row=row_val, column=col_val, padx=3, pady=3, sticky="nsew")

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(1, 5):
    root.grid_rowconfigure(i, weight=1)

root.mainloop()