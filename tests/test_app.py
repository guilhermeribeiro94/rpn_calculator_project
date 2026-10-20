"""Integration checks with real widgets; requires a graphical display or Xvfb."""

import unittest

import customtkinter as ctk

from app import CalculatorApp
from history import HistoryPanel


class AppTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = CalculatorApp()
        cls.app.update()

    @classmethod
    def tearDownClass(cls):
        cls.app.destroy()

    def setUp(self):
        self.app.handle_button("C")
        self.app.history.clear()

    def tearDown(self):
        window = self.app.history.window
        if window is not None and window.winfo_exists():
            window.destroy()

    def enter(self, expression):
        self.app.handle_button("C")
        self.app.expression_entry.insert(0, expression)
        self.app.handle_button("=")
        self.app.update()

    def test_history_window_lifecycle(self):
        history = self.app.history
        self.app.history_button.invoke()
        self.app.update()
        window = history.window
        self.assertEqual(history.text.get("1.0", "end").strip(), "No calculations yet.")
        self.app.history_button.invoke()
        self.assertIs(history.window, window)
        self.enter("5 3 +")
        self.enter("6 7 *")
        self.enter("5 +")
        self.assertEqual(
            history.text.get("1.0", "end").strip(), "6 7 * = 42\n\n5 3 + = 8"
        )
        self.assertEqual(history.text.cget("state"), "disabled")
        window.destroy()
        self.app.history_button.invoke()
        self.app.update()
        self.assertIsNot(history.window, window)
        self.assertIn("5 3 + = 8", history.text.get("1.0", "end"))
        for widget in history.window.winfo_children():
            if isinstance(widget, ctk.CTkButton):
                widget.invoke()
        self.assertEqual(history.entries, [])
        self.assertEqual(history.text.get("1.0", "end").strip(), "No calculations yet.")

    def test_input_controls(self):
        for key in ["5", "space", "3", "+/-", "space", "+", "="]:
            self.app.handle_button(key)
        self.assertEqual(self.app.result_entry.get(), "2")
        self.app.handle_button("DEL")
        self.assertEqual(self.app.expression_entry.get(), "5 -3")
        self.app.handle_button("CE")
        self.assertEqual(self.app.expression_entry.get(), "")
        self.assertEqual(self.app.result_entry.get(), "2")
        self.assertEqual(self.app.history.entries, [("5 -3 +", 2)])
        self.app.handle_button("C")
        self.assertEqual(self.app.result_entry.get(), "")
        self.assertEqual(len(self.app.history.entries), 1)
        self.app.expression_entry.insert(0, "   ")
        self.app.handle_button("+/-")
        self.assertEqual(self.app.expression_entry.get(), "   ")

    def test_histories_have_independent_state(self):
        self.enter("5 3 +")
        other = HistoryPanel(self.app)
        self.assertEqual(other.entries, [])
        other.add("6 7 *", 42)
        self.assertEqual(self.app.history.entries, [("5 3 +", 8)])
