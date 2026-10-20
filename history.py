"""Session history and its reusable window."""

import customtkinter as ctk


class HistoryPanel:
    def __init__(self, parent):
        self.parent = parent
        self.entries = []
        self.window = None
        self.text = None

    def add(self, expression, result):
        self.entries.append((expression, result))
        self.refresh()

    def refresh(self):
        if self.window is None or not self.window.winfo_exists():
            return
        self.text.configure(state="normal")
        self.text.delete("1.0", ctk.END)
        entries = (
            f"{expression} = {result}" for expression, result in reversed(self.entries)
        )
        self.text.insert("1.0", "\n\n".join(entries) or "No calculations yet.")
        self.text.configure(state="disabled")

    def clear(self):
        self.entries.clear()
        self.refresh()

    def show(self):
        if self.window is not None and self.window.winfo_exists():
            self.window.deiconify()
            self.window.lift()
            self.window.focus_set()
            return

        self.window = ctk.CTkToplevel(self.parent)
        self.window.title("Calculation History")
        self.window.geometry("360x400")
        self.window.minsize(300, 250)
        self.window.configure(fg_color="#202020")
        self.window.transient(self.parent)
        self.window.grid_columnconfigure(0, weight=1)
        self.window.grid_rowconfigure(1, weight=1)

        ctk.CTkLabel(
            self.window,
            text="History",
            text_color="#FFFFFF",
            font=("Segoe UI", 20, "bold"),
        ).grid(row=0, column=0, sticky="w", padx=16, pady=(12, 4))
        self.text = ctk.CTkTextbox(
            self.window,
            wrap="word",
            fg_color="#323232",
            text_color="#FFFFFF",
            font=("Segoe UI", 16),
        )
        self.text.grid(row=1, column=0, sticky="nsew", padx=16, pady=8)
        ctk.CTkButton(
            self.window,
            text="Clear history",
            command=self.clear,
            fg_color="#323232",
            hover_color="#3B3B3B",
        ).grid(row=2, column=0, sticky="ew", padx=16, pady=(4, 16))
        self.refresh()
