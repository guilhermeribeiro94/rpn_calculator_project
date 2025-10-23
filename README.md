# 🧮 RPN Calculator v2.0

### 📖 Overview
This project is a **Reverse Polish Notation (RPN) Calculator** implemented in **Python** with a clean, modern interface using **CustomTkinter**.

The calculator evaluates arithmetic expressions in **postfix notation**, using a **stack-based algorithm** that strictly follows the **LIFO (Last In, First Out)** principle.

Version **2.0** introduces a redesigned UI, rounded buttons, modern dark theme, and improved input handling.

---

## ⚙️ Features
✅ Stack-based RPN evaluation (push/pop logic)  
✅ Supports `+`, `-`, `*`, `/` operations  
✅ Handles invalid input and missing operands  
✅ Dual display:
- **Expression** (top input)
- **Result** (bottom output)  
✅ Functional keys:
- `CE` → Clear Entry  
- `C` → Clear All  
- `DEL` → Delete last token  
- `+/-` → Toggle sign  
- `space` → Add spacing between numbers  
✅ Responsive layout (grid system)  
✅ Polished **CustomTkinter** visual design

---

## 🧩 Technologies Used
- **Python 3.11+**
- **CustomTkinter** – Modern, themeable GUI framework
- **Tkinter** (base framework)

---

## 🧠 How It Works
The calculator reads an **RPN expression**, splits it into tokens, and processes them sequentially using a **stack**.

1. **Numbers** are pushed to the stack.  
2. **Operators** pop the top two numbers, perform the operation, and push the result back.

If the input is valid, one number remains — the final result.

### Example:
Input: 5 3 +
Output: 8