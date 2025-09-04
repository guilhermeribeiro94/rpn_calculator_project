# Reverse Polish Notation (RPN) Calculator
# This program implements a simple RPN calculator that uses a stack to evaluate expressions.
from PIL import Image
import customtkinter as ctk


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
        display_1.delete(0, ctk.END)
    # If the button is 'C', clear both displays
    elif button_text == 'C':
        display_1.delete(0, ctk.END)
        display_2.delete(0, ctk.END)
    # If the button is 'DEL', remove the last token from the input
    elif button_text == 'DEL':
        current_text = display_1.get()
        if current_text:
            new_text = ' '.join(current_text.split()[:-1])
            display_1.delete(0, ctk.END)
            display_1.insert(ctk.END, new_text)
    # If the button is '+/-', toggle the sign of the last number in the input
    elif button_text == '+/-':
        current_text = display_1.get()
        if current_text:
            tokens = current_text.split()
            if tokens[-1].lstrip('-').isdigit():
                tokens[-1] = str(-int(tokens[-1]))
                new_text = ' '.join(tokens)
                display_1.delete(0, ctk.END)
                display_1.insert(ctk.END, new_text)
    # If the button is 'space', add a space to the input
    elif button_text == 'space':
        current_text = display_1.get()
        if current_text:
            new_text = current_text + ' '
            display_1.delete(0, ctk.END)
            display_1.insert(ctk.END, new_text)
    # If the button is '=', evaluate the RPN expression
    elif button_text == '=':
        try:
            result = rpn_calculator()
            display_2.delete(0, ctk.END)
            display_2.insert(ctk.END, str(result))
        except ValueError as e:
            display_2.delete(0, ctk.END)
            display_2.insert(ctk.END, f'Error: {e}')
    else:
        # For all other buttons, append the button text to the current input
        current_text = display_1.get()
        if current_text != '':
            new_text = current_text + button_text
        else:
            new_text = button_text
        display_1.delete(0, ctk.END)
        display_1.insert(ctk.END, new_text)


# Create the main window for the RPN calculator interface
interface = ctk.CTk()
interface.title('RPN Calculator')
interface.geometry('320x500')
interface.configure(fg_color='#202020')
interface.resizable(False, False)

# Create a display area for the history
history_icon = ctk.CTkImage(dark_image=Image.open('history_icon.png'), size=(50, 40))
history_button = ctk.CTkButton(interface,text='', image=history_icon, anchor='e', width=50, height=40,
                               fg_color='#202020', text_color='#FFFFFF', hover_color='#323232')
history_button.grid(row=0, column=0, columnspan=4, sticky='e', padx=0, pady=0)

# Create a display area for the expression
display_expression= ctk.CTkLabel(interface, text='Expression', anchor='w', fg_color='#202020', text_color='#FFFFFF',
                                 font=('Segoe UI', 14, 'bold'))
display_expression.grid(row=1, column=0, columnspan=4, sticky='w', padx=5, pady=0)

display_1 = ctk.CTkEntry(interface, justify='right', width=305, border_color='#202020', fg_color='#202020',
                         text_color='#FFFFFF', font=('Segoe UI', 20, 'bold'))
display_1.grid(row=2, column=0, columnspan=4, padx=8, pady=0)

# Create a display area for the result
display_result= ctk.CTkLabel(interface, text='Result', anchor='w', fg_color='#202020', text_color='#FFFFFF',
                             font=("Segoe UI", 14, 'bold'))
display_result.grid(row=3, column=0, columnspan=4, sticky='w', padx=5, pady=0)

display_2 = ctk.CTkEntry(interface, justify='right', width=305, border_color='#202020', fg_color='#202020',
                         text_color='#FFFFFF', font=('Segoe UI', 20, 'bold'))
display_2.grid(row=4, column=0, columnspan=4, padx=8, pady=(0, 6))

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
            color_fg = '#4CC2FF'
            color_t = '#153647'
            color_h = '#47B1E9'
        elif button_image in ['CE', 'C', 'DEL', '/', '*', '-', '+']:
            color_fg = '#323232'
            color_t = '#FFFFFF'
            color_h = '#3B3B3B'
        else:
            color_fg = '#3B3B3B'
            color_t = '#FFFFFF'
            color_h = '#323232'
        button = ctk.CTkButton(interface, text=button_image, anchor='center', width=78, height=62, corner_radius=6,
                               fg_color=color_fg, text_color=color_t, hover_color=color_h, font=('Segoe UI', 18),
                               command=lambda bti=button_image: calculator_buttons(bti))
        button.grid(row=5+r, column=c, padx=1, pady=1)

# Initialize the loop for the interface
interface.mainloop()

