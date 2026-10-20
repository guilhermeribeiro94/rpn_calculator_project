"""Desktop interface for the RPN calculator."""

from pathlib import Path

import customtkinter as ctk
from PIL import Image

from calculator import evaluate_rpn
from history import HistoryPanel


class CalculatorApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.history = HistoryPanel(self)
        self.title("RPN Calculator")
        self.geometry("320x500")
        self.configure(fg_color="#202020")
        self.resizable(False, False)

        self.history_icon = ctk.CTkImage(
            dark_image=Image.open(
                Path(__file__).resolve().parent / "assets" / "history_icon.png"
            ),
            size=(50, 40),
        )
        self.history_button = ctk.CTkButton(
            self,
            text="",
            image=self.history_icon,
            anchor="e",
            width=50,
            height=40,
            fg_color="#202020",
            text_color="#FFFFFF",
            hover_color="#323232",
            command=self.history.show,
        )
        self.history_button.grid(
            row=0, column=0, columnspan=4, sticky="e", padx=0, pady=0
        )
        self._create_displays()
        self._create_keypad()

    def _create_displays(self):
        for index, label in enumerate(("Expression", "Result")):
            row = 1 + index * 2
            ctk.CTkLabel(
                self,
                text=label,
                anchor="w",
                fg_color="#202020",
                text_color="#FFFFFF",
                font=("Segoe UI", 14, "bold"),
            ).grid(row=row, column=0, columnspan=4, sticky="w", padx=5)
            entry = ctk.CTkEntry(
                self,
                justify="right",
                width=305,
                border_color="#202020",
                fg_color="#202020",
                text_color="#FFFFFF",
                font=("Segoe UI", 20, "bold"),
            )
            entry.grid(
                row=row + 1, column=0, columnspan=4, padx=8, pady=(0, 6) if index else 0
            )
            if index == 0:
                self.expression_entry = entry
            else:
                self.result_entry = entry

    def _create_keypad(self):
        rows = (
            ("CE", "C", "DEL", "/"),
            ("7", "8", "9", "*"),
            ("4", "5", "6", "-"),
            ("1", "2", "3", "+"),
            ("+/-", "0", "space", "="),
        )
        for row, labels in enumerate(rows, start=5):
            for column, text in enumerate(labels):
                if text == "=":
                    foreground, text_color, hover = "#4CC2FF", "#153647", "#47B1E9"
                elif text in {"CE", "C", "DEL", "/", "*", "-", "+"}:
                    foreground, text_color, hover = "#323232", "#FFFFFF", "#3B3B3B"
                else:
                    foreground, text_color, hover = "#3B3B3B", "#FFFFFF", "#323232"
                ctk.CTkButton(
                    self,
                    text=text,
                    anchor="center",
                    width=78,
                    height=62,
                    corner_radius=6,
                    fg_color=foreground,
                    text_color=text_color,
                    hover_color=hover,
                    font=("Segoe UI", 18),
                    command=lambda key=text: self.handle_button(key),
                ).grid(row=row, column=column, padx=1, pady=1)

    @staticmethod
    def _set_entry(entry, text):
        entry.delete(0, ctk.END)
        entry.insert(0, text)

    def _calculate(self):
        expression = self.expression_entry.get().strip()
        try:
            result = evaluate_rpn(expression)
        except ValueError as error:
            self._set_entry(self.result_entry, f"Error: {error}")
        else:
            self._set_entry(self.result_entry, str(result))
            self.history.add(expression, result)

    def handle_button(self, button_text):
        current_text = self.expression_entry.get()
        if button_text == "=":
            self._calculate()
            return
        if button_text == "CE":
            new_text = ""
        elif button_text == "C":
            new_text = ""
            self._set_entry(self.result_entry, "")
        elif button_text == "DEL":
            new_text = " ".join(current_text.split()[:-1])
        elif button_text == "+/-":
            tokens = current_text.split()
            if not tokens or not tokens[-1].lstrip("-").isdigit():
                return
            tokens[-1] = str(-int(tokens[-1]))
            new_text = " ".join(tokens)
        elif button_text == "space":
            new_text = current_text + " " if current_text else ""
        else:
            new_text = current_text + button_text
        self._set_entry(self.expression_entry, new_text)
