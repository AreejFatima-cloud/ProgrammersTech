from tkinter import *
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.configure(bg='black')
        
        self.operator = ""
        self.input_value = StringVar()
        
        self.create_widgets()
        
    def create_widgets(self):
        button_bg = 'black'
        button_fg = 'white'
        button_active_bg = '#071739'
        button_active_fg = 'white'
        
        self.display_text = Entry(self.root, font=("Arial", 20, "bold"), textvariable=self.input_value, bd=0, insertwidth=4, bg='dark gray', fg=button_fg, justify="right")
        self.display_text.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=25, pady=15, padx=15, sticky="nsew")

        buttons = [
            ('C', self.clear, 1, 0), ('%', self.percentage, 1, 1), ('<', self.delete, 1, 2), ('/', lambda: self.click("/"), 1, 3),
            ('7', lambda: self.click(7), 2, 0), ('8', lambda: self.click(8), 2, 1), ('9', lambda: self.click(9), 2, 2), ('+', lambda: self.click("+"), 2, 3),
            ('4', lambda: self.click(4), 3, 0), ('5', lambda: self.click(5), 3, 1), ('6', lambda: self.click(6), 3, 2), ('-', lambda: self.click("-"), 3, 3),
            ('1', lambda: self.click(1), 4, 0), ('2', lambda: self.click(2), 4, 1), ('3', lambda: self.click(3), 4, 2), ('*', lambda: self.click("*"), 4, 3),
            ('0', lambda: self.click(0), 5, 0), ('e', self.exponent, 5, 1), ('=', self.equals, 5, 2, 2)
        ]

        for (text, command, row, column, *span) in buttons:
            Button(self.root, text=text, command=command, width=4, bd=8, font=("Arial", 20, "bold"), bg=button_bg, fg=button_fg,
                   activebackground=button_active_bg, activeforeground=button_active_fg).grid(row=row, column=column, columnspan=span[0] if span else 1, sticky="nsew")

    def click(self, symbol):
        self.operator += str(symbol)
        self.update_display(self.operator)

    def percentage(self):
        try:
            result = str(eval(self.operator) / 100)
            self.update_display(result)
            self.operator = result
        except:
            self.update_display("Error")
            self.operator = ""
        
    def clear(self):
        self.operator = ""
        self.update_display("")

    def equals(self):
        try:
            result = str(eval(self.operator))
            self.update_display(result)
            self.operator = result
        except:
            self.clear()
            self.update_display("Error")

    def delete(self):
        self.operator = self.operator[:-1]
        self.update_display(self.operator)
    
    def exponent(self):
        try:
            result = str(math.exp(float(self.operator)))
            self.update_display(result)
            self.operator = result
        except ValueError:
            self.update_display("Error")

    def update_display(self, value):
        self.display_text.delete(0, "end")
        self.display_text.insert(0, value)


if __name__ == "__main__":
    root = Tk()
    calc = Calculator(root)
    root.mainloop()
