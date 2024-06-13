import tkinter as tk
from tkinter import ttk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("300x400")
        self.current_input = ""

        self.display = ttk.Entry(root, font=("Arial", 20), justify='right')
        self.display.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8)

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0), ('(', 5, 1), (')', 5, 2), ('%', 5, 3),
        ]

        for (text, row, col) in buttons:
            ttk.Button(self.root, text=text, command=lambda t=text: self.on_button_click(t)).grid(row=row, column=col, sticky="nsew", ipadx=10, ipady=10)

        for i in range(6):
            self.root.grid_rowconfigure(i, weight=1)
            self.root.grid_columnconfigure(i, weight=1)

    def on_button_click(self, char):
        if char == '=':
            try:
                self.current_input = str(eval(self.current_input))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, self.current_input)
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
                self.current_input = ""
        elif char == 'C':
            self.current_input = ""
            self.display.delete(0, tk.END)
        else:
            self.current_input += str(char)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.current_input)

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
