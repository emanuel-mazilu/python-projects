import tkinter as tk

# the display string
expresion = ""

    # TODO 
    # Divizion by 0
    # invalid expresions

def onclick(i):
    
    global expresion
    # Evaluate the expresion on the display ex: 2+3/2-6*5
    if i == "=":
        text_input.set(eval(expresion))
        expresion = ""
    # clear the memory and the display
    elif i == "C":
        text_input.set("")
        expresion = ""
    # adds numbers and operators one after another
    else:
        expresion = expresion + str(i)
        text_input.set(expresion)

# create main window
calc = tk.Tk()
calc.title("Calculator")

# Used StrigVar to easily change the value of text variable as it can not be done
# with normal variable
text_input = tk.StringVar()

# the display of the calculator
tk.Entry(calc, font=("arial", 20, "bold"), textvariable=text_input, bd=5, insertwidth = 4,
                    justify='right').grid(columnspan=4)

# make the buttons and add them to the window in grid style
# starting from the bottom (now i'm here :)) ) and set the text
# with the signs contained in the sign list using an i iterator
# when button presed 'command' call onclick function sendig the symbol coresponding to the btn

i = 0
signs = [0, "C", "=", "+", 1, 2, 3, "-", 4, 5, 6, "*", 7, 8, 9, "/" ]
for r in range(5, 1, -1):
    for c in range(4):
        tk.Button(calc, padx=28, pady=16, bd=1, font=('arial', 20, 'bold'), text=signs[i], 
                        command=lambda sign=signs[i] :onclick(sign)).grid(row=r, column=c)
        i += 1

# display main window and keep it open
calc.mainloop()