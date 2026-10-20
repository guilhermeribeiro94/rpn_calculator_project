<h1 align="center">🧮 RPN Calculator v2.0</h1>

---

<!-- BADGES -->
<p align="center">
  <img src="https://img.shields.io/badge/Status-Completed-green?style=for-the-badge">

  <img src="https://img.shields.io/badge/Programming Language-Python-white?style=for-the-badge">
  <img src="https://img.shields.io/badge/Interface-CustomTkinter-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge">
</p>

---

## 🧭 Table of Contents

1. [📘 Project Description](#-project-description)  
2. [📊 Project Status](#-project-status)  
3. [⚙️ Features & Demonstration](#️-features--demonstration)  
4. [🔗 Access the Project](#-access-the-project)  
5. [🧩 Technologies Used](#-technologies-used)  
6. [👨‍💻 Developer](#-developer)  
7. [📝 License](#-license)  

---

## 📘 Project Description

**RPN Calculator v2.0** is a Python-based calculator using **Reverse Polish Notation (RPN)** — a mathematical method where operators follow operands, eliminating the need for parentheses.

🔹 **Highlights of version**  
- Dark mode UI built with **CustomTkinter**  
- Rounded grid-based buttons  
- Dual display: **Expression** and **Result**  
- True stack-based logic (LIFO behavior)  
- Smart input cleaning and error handling  

---

## 📊 Project Status

✅ **Completed**   

---

## ⚙️ Features & Demonstration

### Main Features
- ➕ ➖ ✖️ ➗ Basic arithmetic operations  
- 🧱 Stack logic (Push/Pop)  
- 💡 Error handling for invalid tokens or division by zero  
- 🕹️ Functional keys: `CE`, `C`, `DEL`, `+/-`, `space`, `=`  
- 🎨 Dark mode theme with **CustomTkinter**

### Example
> ```
> Input: 5 3 +
> Stack: [8]
> Output: 8
> ```

---

## 🔗 Access the Project

1. Clone the source code:

```sh
git clone https://github.com/guilhermeribeiro94/rpn_calculator_project.git
```

2. Enter the project directory and install the dependencies (preferably in a virtual environment):

```sh
cd rpn_calculator_project
python -m pip install -r requirements.txt
```

3. Run the application:

```sh
python rpn_calculator_v2.0.py
```

## 🧩 Technologies Used

| Technology | Description |
|-------------|--------------|
| **Python** | Core programming language |
| **Tkinter** | Base framework |
| **CustomTkinter** | Modern library |

---

## 👨‍💻 Developer

**Guilherme Aurélio Destefano Ribeiro**

🔗 [LinkedIn](https://www.linkedin.com/in/guilhermedestefanoribeiro)

---

## 📝 License

This project is licensed under the **MIT License** — see [LICENSE.md](LICENSE.md) for more information.

---

## Project structure

- `rpn_calculator_v2.0.py`: application entry point.
- `calculator.py`: RPN evaluation, independent of the interface.
- `app.py`: calculator window, keypad, and input handling.
- `history.py`: session history and its window.
- `assets/`: images used by the interface.
- `requirements.txt`: Python dependencies.
- `tests/`: calculation and interface regression tests.

Start the application with:

```sh
python rpn_calculator_v2.0.py
```

The history is kept for the current session. Close the application to discard it.

Run the calculation tests without a graphical display:

```sh
python -m unittest discover -s tests -p test_calculator.py -v
```

Run all tests with a graphical display available:

```sh
python -m unittest discover -s tests -v
```

On a headless Linux machine, run the full suite through `xvfb-run -a`.
