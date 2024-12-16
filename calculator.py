import tkinter as tk

# Function to update the expression in the entry box
def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

# Function to evaluate the final expression
def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = total
    except:
        equation.set("Error")
        expression = ""

# Function to clear the entry box
def clear():
    global expression
    expression = ""
    equation.set("")

if __name__ == "__main__":
    # Create a GUI window
    gui = tk.Tk()
    gui.configure(background="light blue")  # Set the background color of the window
    gui.title("GUI Calculator")
    gui.geometry("400x500")

    # Set up the style for buttons
    button_style = {
        'font': ('Arial', 18),
        'fg': 'black',
        'height': 2,
        'width': 5,
        'bd': 3,
        'relief': 'raised'
    }

    # Initialize the expression and set up the display
    expression = ""
    equation = tk.StringVar()
    expression_field = tk.Entry(gui, textvariable=equation, font=('Arial', 24), bd=10, insertwidth=2, width=14, borderwidth=4, bg='white')
    expression_field.grid(columnspan=4, ipadx=8, pady=10)

    # Create buttons and place them in the grid
    buttons = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
        ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ]

    for (text, row, col) in buttons:
        bg_color = 'blue' if text == '=' else 'light blue'
        button = tk.Button(gui, text=text, command=equalpress if text == '=' else lambda t=text: press(t), bg=bg_color, **button_style)
        button.grid(row=row, column=col, padx=5, pady=5)

    # Create clear button
    clear_button = tk.Button(gui, text='Clear', command=clear, bg='red', **button_style)
    clear_button.grid(row=5, column=0, columnspan=4, pady=10)

    # Start the GUI
    gui.mainloop()

