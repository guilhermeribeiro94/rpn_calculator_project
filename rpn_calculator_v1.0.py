# Reverse Polish Notation (RPN) Calculator
# This program implements a simple RPN calculator that uses a stack to evaluate expressions.
import tkinter as tk


# Function to evaluate the RPN expression
def rpn_calculator():
    # Get the expression from the display and split it into tokens
    rpn_expression = display_1.get().strip()
    notation = rpn_expression.split()
    stack = list()

    for item in notation:
        if item in '+-*/':
            # Check if there are at least two operands on the stack if not, raise an error
            if len(stack) < 2:
                raise ValueError('Missing numbers')
            # POP - Removes the top two items from the stack for calculation
            b = stack.pop()
            a = stack.pop()
            # PUSH - Adds the result of the operation back to the stack
            if item == '+':
                stack.append(a + b)
            elif item == '-':
                stack.append(a - b)
            elif item == '*':
                stack.append(a * b)
            elif item == '/':
                stack.append(int(a / b))
        else:
            try:
                # PUSH - Adds the item to the stack as an integer
                stack.append(int(item))
            except ValueError:
                # If the item is not a valid integer, raise an error
                raise ValueError(f'Invalid token {item}')

    # If there is not exactly one item left on the stack after processing all tokens, raise an error
    if len(stack) != 1:
        raise ValueError('Too many numbers')

    return stack[0]


# Function to handle button clicks and update the display
def calculator_buttons(button_text):
    # If the button is 'CE' clear the current input
    if button_text == 'CE':
        display_1.delete(0, tk.END)
    # If the button is 'C', clear both displays
    elif button_text == 'C':
        display_1.delete(0, tk.END)
        display_2.delete(0, tk.END)
    # If the button is 'DEL', remove the last token from the input
    elif button_text == 'DEL':
        current_text = display_1.get()
        if current_text:
            new_text = ' '.join(current_text.split()[:-1])
            display_1.delete(0, tk.END)
            display_1.insert(tk.END, new_text)
    # If the button is '+/-', toggle the sign of the last number in the input
    elif button_text == '+/-':
        current_text = display_1.get()
        if current_text:
            tokens = current_text.split()
            if tokens[-1].lstrip('-').isdigit():
                tokens[-1] = str(-int(tokens[-1]))
                new_text = ' '.join(tokens)
                display_1.delete(0, tk.END)
                display_1.insert(tk.END, new_text)
    # If the button is 'space', add a space to the input
    elif button_text == 'space':
        current_text = display_1.get()
        if current_text:
            new_text = current_text + ' '
            display_1.delete(0, tk.END)
            display_1.insert(tk.END, new_text)
    # If the button is '=', evaluate the RPN expression
    elif button_text == '=':
        try:
            result = rpn_calculator()
            display_2.delete(0, tk.END)
            display_2.insert(tk.END, str(result))
        except ValueError as e:
            display_2.delete(0, tk.END)
            display_2.insert(tk.END, f'Error: {e}')
    else:
        # For all other buttons, append the button text to the current input
        current_text = display_1.get()
        if current_text != '':
            new_text = current_text + button_text
        else:
            new_text = button_text 
        display_1.delete(0, tk.END)
        display_1.insert(tk.END, new_text)


# Create the main window for the RPN calculator interface
interface = tk.Tk()
interface.title('RPN Calculator')
interface.geometry('320x500')
interface.configure(bg='#202020')
interface.resizable(False, False)

# Create a display area for the expression
display_expression= tk.Label(interface, text='Expression', anchor='w', bg='#202020', fg='#FFFFFF', font=('Segoe UI', 10, 'bold'))
display_expression.grid(row=0, column=0, columnspan=4, sticky='w', pady=2)
display_1 = tk.Entry(interface, relief='flat', justify='right', bg='#202020', fg='white', font=('Segoe UI', 20))
display_1.grid(row=1, column=0, columnspan=4, padx=8, pady=2)

# Create a display area for the result
display_result= tk.Label(interface, text='Result', anchor='w', bg='#202020', fg='#FFFFFF', font=("Segoe UI", 10, 'bold'))
display_result.grid(row=2, column=0, columnspan=4, sticky='w', pady=2)
display_2 = tk.Entry(interface, relief='flat', justify='right', bg='#202020', fg='white', font=('Segoe UI', 20))
display_2.grid(row=3, column=0, columnspan=4, padx=8, pady=(0, 35))

# Create the buttons for the calculator
buttons = [ 'CE', 'C', 'DEL', '/',
            '7', '8', '9', '*',
            '4', '5', '6', '-',         
            '1', '2', '3', '+',
            '+/-', '0', 'space', '=']

# Create a function to handle button clicks
for r in range(5):
    for c in range(4):
        button_image = buttons[(r * 4) + c]
        if button_image == '=':
            color_bg = '#4CC2FF'
            color_fg = '#153647'
        elif button_image in ['CE', 'C', 'DEL', '/', '*', '-', '+']:
            color_bg = '#323232'
            color_fg = '#FFFFFF'
        else:
            color_bg = '#3B3B3B'
            color_fg = '#FFFFFF'
        button = tk.Button(interface, text=button_image, width=6, height=2, bg=color_bg, fg=color_fg, relief='flat', font=('Arial', 14), command=lambda bti=button_image: calculator_buttons(bti))
        button.grid(row=4+r, column=c, padx=0, pady=2)

# Initialize the loop for the interface
interface.mainloop()

