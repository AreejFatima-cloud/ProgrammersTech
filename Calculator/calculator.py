from tkinter import*
import math

def ButtonClick(symbol):
    global operator
    operator= operator+ str(symbol)
    display_text.delete(0, "end")
    display_text.insert(0, operator)
    
def ButtonPercentage():
    global operator
    try:
        result = str(eval(operator) / 100)
        input_value.set(result)
        operator = ""
    except:
        input_value.set("Error")
        operator = ""
        
def  ButtonClear():
    global operator
    operator= ""
    input_value.set("")
    
def ButtonEquals():
    global operator
    try:
        operator = str(eval(operator))
        display_text.delete(0, "end")
        display_text.insert(0, operator)
    
    except:
        ButtonClear()
        display_text.insert(0, "Error")
      
def ButtonDelete():
    global operator
    operator = operator[:-1]
    input_value.set(operator)
    
def ButtonExponent():
    global operator
    try:
        result = math.exp(float(operator))
        operator = str(result)
        input_value.set(operator)
    except ValueError:
        input_value.set("Error")
        
root =Tk()
root.title("Calculator")
root.configure(bg='#071739')
operator = ""
input_value = StringVar()

display_text = Entry(root, font=("Arial", 20, "bold"), textvariable=input_value, bd=0, insertwidth=4, bg='#1E1E1E', fg="white", justify="right")
display_text.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=25, pady=15, padx=15, sticky="nsew")

button_bg = '#333333'
button_fg = 'white'
button_active_bg = '#071739'
button_active_fg = 'white'

# For Row 1
btn_clear = Button(root, width=9, bd=8, bg='#4B6382', fg=button_fg, font=("Arial", 20, "bold"), text="C", command=ButtonClear,
                      activebackground=button_active_bg, activeforeground=button_active_fg)
btn_clear.grid(row=1, columnspan=2)

btn_del = Button(root, width=4, bd=8, bg='#4B6382', fg=button_fg, font=("Arial", 20, "bold"), text="<-", command=ButtonDelete,
                    activebackground=button_active_bg, activeforeground=button_active_fg)
btn_del.grid(row=1, column=2)

btn_div = Button(root, padx=16,width=3, bd=8,bg='#111822', fg=button_fg, font=("Arial", 20, "bold"), text="/", command=lambda: ButtonClick("/"),
                    activebackground=button_active_bg, activeforeground=button_active_fg)
btn_div.grid(row=1, column=3)

# For Row 2
btn_7 = Button(root, padx=16, bd=8, fg=button_fg, font=("Arial", 20, "bold"), text="7", bg=button_bg, command=lambda: ButtonClick(7),
                  activebackground=button_active_bg, activeforeground=button_active_fg)
btn_7.grid(row=2, column=0)

btn_8 = Button(root, padx=16, bd=8, fg=button_fg, font=("Arial", 20, "bold"), text="8", bg=button_bg, command=lambda: ButtonClick(8),
                  activebackground=button_active_bg, activeforeground=button_active_fg)
btn_8.grid(row=2, column=1)
btn_9 = Button(root, padx=16, bd=8, fg=button_fg, font=("Arial", 20, "bold"), text="9", bg=button_bg, command=lambda: ButtonClick(9),
                  activebackground=button_active_bg, activeforeground=button_active_fg)
btn_9.grid(row=2, column=2)

btn_add = Button(root, padx=16,width=3, bd=8, fg=button_fg, font=("Arial", 20, "bold"), text="+", bg='#111822', command=lambda: ButtonClick("+"),
                    activebackground=button_active_bg, activeforeground=button_active_fg)
btn_add.grid(row=2, column=3)

# For Row 3
btn_4 = Button(root, padx=16, bd=8, fg=button_fg, font=("Arial", 20, "bold"), text="4", bg=button_bg, command=lambda: ButtonClick(4),
                  activebackground=button_active_bg, activeforeground=button_active_fg)
btn_4.grid(row=3, column=0)

btn_5 = Button(root, padx=16, bd=8, fg=button_fg, font=("Arial", 20, "bold"), text="5", bg=button_bg, command=lambda: ButtonClick(5),
                  activebackground=button_active_bg, activeforeground=button_active_fg)
btn_5.grid(row=3, column=1)

btn_6 = Button(root, padx=16, bd=8, fg=button_fg, font=("Arial", 20, "bold"), text="6", bg=button_bg, command=lambda: ButtonClick(6),
                  activebackground=button_active_bg, activeforeground=button_active_fg)
btn_6.grid(row=3, column=2)

btn_sub = Button(root, padx=16, width=3,bd=8, fg=button_fg, font=("Arial", 20, "bold"), text="-", bg='#111822', command=lambda: ButtonClick("-"),
                    activebackground=button_active_bg, activeforeground=button_active_fg)
btn_sub.grid(row=3, column=3)

# For Row 4
btn_1 = Button(root, padx=16, bd=8, fg=button_fg, font=("Arial", 20, "bold"), text="1", bg=button_bg, command=lambda: ButtonClick(1),
                  activebackground=button_active_bg, activeforeground=button_active_fg)
btn_1.grid(row=4, column=0)

btn_2 = Button(root, padx=16, bd=8, fg=button_fg, font=("Arial", 20, "bold"), text="2", bg=button_bg, command=lambda: ButtonClick(2),
                  activebackground=button_active_bg, activeforeground=button_active_fg)
btn_2.grid(row=4, column=1)

btn_3 = Button(root, padx=16, bd=8, fg=button_fg, font=("Arial", 20, "bold"), text="3", bg=button_bg, command=lambda: ButtonClick(3),
                  activebackground=button_active_bg, activeforeground=button_active_fg)
btn_3.grid(row=4, column=2)

btn_mul = Button(root, padx=16, width=3,bd=8, fg=button_fg, font=("Arial", 20, "bold"), text="*", bg='#111822', command=lambda: ButtonClick("*"),
                    activebackground=button_active_bg, activeforeground=button_active_fg)
btn_mul.grid(row=4, column=3)

# For Row 5
btn_0 = Button(root, padx=16, bd=8, fg=button_fg, font=("Arial", 20, "bold"), text="0", bg=button_bg, command=lambda: ButtonClick(0),
                  activebackground=button_active_bg, activeforeground=button_active_fg)
btn_0.grid(row=5, column=0)

btn_exp = Button(root, padx=16, bd=8, fg=button_fg, font=("Arial", 20, "bold"), text="e", bg='#4B6382', command=ButtonExponent,
                    activebackground=button_active_bg, activeforeground=button_active_fg)
btn_exp.grid(row=5, column=1)

btn_equals = Button(root, padx=16,width=8, bd=8, fg=button_fg, font=("Arial", 20, "bold"), text="=", bg='#4B6382', command=ButtonEquals,
                       activebackground=button_active_bg, activeforeground=button_active_fg)
btn_equals.grid(row=5, column=2, columnspan= 2)


root.mainloop()
