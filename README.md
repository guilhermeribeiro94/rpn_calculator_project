# 🧮 RPN Calculator v2.0

A desktop calculator built with Python and CustomTkinter. It evaluates integer expressions in **Reverse Polish Notation (RPN)**, where operators follow their operands.

## Table of contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [History](#history)
- [Limitations](#limitations)
- [Project structure](#project-structure)
- [Tests](#tests)
- [Technologies](#technologies)
- [Developer](#developer)
- [License](#license)

## Features

- Addition, subtraction, multiplication, and integer division.
- Stack-based RPN evaluation.
- Separate expression and result displays.
- Dark interface with an on-screen keypad.
- Session history accessible through the clock icon.
- Error messages for invalid tokens, missing operands, and extra operands.

## Requirements

- Python with `pip` and `venv`; development and tests have been validated with **Python 3.12**.
- Tkinter/Tk support and a graphical display to use the interface.
- Python dependencies listed in `requirements.txt`: CustomTkinter and Pillow.

Check Tkinter with:

```sh
python -m tkinter
```

This should open a small test window. If Tkinter is missing, install Tk support for your Python distribution. On Debian/Ubuntu with the system Python, the package is usually `python3-tk`; `python3-venv` may also be needed. Tkinter is not installed through `pip`.

Use `python3` instead of `python` below if that is how your Python installation is named.

## Installation

Clone the repository and create a virtual environment:

```sh
git clone https://github.com/guilhermeribeiro94/rpn_calculator_project.git
cd rpn_calculator_project
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Or on macOS/Linux:

```sh
source .venv/bin/activate
```

Install the dependencies:

```sh
python -m pip install -r requirements.txt
```

## Usage

With the virtual environment activated, start the application:

```sh
python rpn_calculator_v2.0.py
```

Separate operands and operators with spaces, then press `=`. For example:

```text
5 3 +          → 8
5 1 2 + 4 * + 3 - → 14
7 2 /          → 3
-7 2 /         → -3
```

| Button | Action |
| --- | --- |
| `CE` | Clear the expression. |
| `C` | Clear the expression and result; keep history. |
| `DEL` | Remove the last token. |
| `+/-` | Toggle the sign of the last integer token. |
| `space` | Add a separator between tokens. |
| `=` | Evaluate the expression and record a successful calculation. |

## History

Click the clock icon to open the history window. Successful calculations appear with their expression and result, newest first. The list updates while the window is open.

- Closing and reopening the history window preserves its entries.
- **Clear history** removes all entries without clearing the calculator displays.
- Failed calculations are not recorded.
- History is held in memory for the current session and is discarded when the application closes.

## Limitations

- Operands must be integers; decimal input is not supported.
- Division truncates toward zero: `7 2 /` gives `3`, and `-7 2 /` gives `-3`.
- Division by zero currently raises an exception that the interface does not convert into a display error message. This is a known issue.
- The application is a desktop GUI and requires a display. It does not provide a web interface.

## Project structure

```text
rpn_calculator_project/
├── rpn_calculator_v2.0.py  # Application entry point
├── app.py                 # Window, keypad, and input handling
├── calculator.py          # RPN evaluation independent of the interface
├── history.py             # Session history and its window
├── assets/
│   └── history_icon.png
├── tests/
│   ├── test_calculator.py  # Evaluation regression tests
│   └── test_app.py         # Integration tests with real widgets
├── requirements.txt
├── README.md
└── LICENSE.md
```

## Tests

Run these commands from the repository root with the virtual environment activated.

Calculation tests do not require a display:

```sh
python -m unittest discover -s tests -p test_calculator.py -v
```

Run all tests, including the interface tests, with a graphical display available:

```sh
python -m unittest discover -s tests -v
```

On a headless Linux machine with Xvfb and `xauth` installed:

```sh
xvfb-run -a python -m unittest discover -s tests -v
```

The tests cover arithmetic, invalid expressions, the existing division-by-zero exception, input controls, and the history window lifecycle. The division-by-zero test preserves the known exception behavior; it does not indicate that the interface handles it.

## Technologies

| Technology | Role |
| --- | --- |
| Python | Application and calculation logic |
| Tkinter | Base GUI framework |
| CustomTkinter | Interface widgets |
| Pillow | History icon loading |
| unittest | Calculation and interface tests |

## Developer

**Guilherme Aurélio Destefano Ribeiro**

[LinkedIn](https://www.linkedin.com/in/guilhermedestefanoribeiro)

## License

This project is licensed under the [MIT License](LICENSE.md).
