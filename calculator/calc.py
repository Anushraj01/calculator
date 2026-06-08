import tkinter as tk
from tkinter import ttk
import math

class ModernCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Sleek Calc")
        self.root.geometry("380x600")
        self.root.configure(bg="#1e1e2e")  # Premium dark background (Catppuccin Mocha theme)
        self.root.resizable(False, False)

        # Application State
        self.expression = ""
        self.current_input = "0"
        self.new_input_start = True

        # Custom Color Palette
        self.colors = {
            "bg": "#1e1e2e",            # Main window background
            "display_bg": "#11111b",    # Display screen background
            "text_primary": "#cdd6f4",  # High contrast text
            "text_secondary": "#7f849c",# Formula/history text
            "btn_num": "#313244",       # Number keys
            "btn_num_hover": "#45475a", 
            "btn_fn": "#181825",        # Functions like C, Backspace, %
            "btn_fn_hover": "#313244",
            "btn_op": "#f38ba8",        # Math operators (+, -, *, /)
            "btn_op_hover": "#f38ba8",
            "btn_eq": "#a6e3a1",        # Equals button
            "btn_eq_hover": "#b4befe",
            "text_eq": "#11111b"        # Dark text for contrast on equal button
        }

        # Configure styles
        self.setup_ui()
        self.bind_keyboard()

    def setup_ui(self):
        """Builds the graphical user interface components."""
        # Main Display Container
        display_container = tk.Frame(self.root, bg=self.colors["display_bg"], height=140)
        display_container.pack(fill=tk.BOTH, padx=15, pady=(20, 10))
        display_container.pack_propagate(False)

        # Formula / Expression Display (Top Line)
        self.formula_label = tk.Label(
            display_container,
            text="",
            font=("Helvetica", 12),
            anchor="e",
            bg=self.colors["display_bg"],
            fg=self.colors["text_secondary"],
            padx=15
        )
        self.formula_label.pack(fill=tk.X, pady=(15, 5))

        # Main Value Display (Bottom Line)
        self.display_label = tk.Label(
            display_container,
            text="0",
            font=("Helvetica", 32, "bold"),
            anchor="e",
            bg=self.colors["display_bg"],
            fg=self.colors["text_primary"],
            padx=15
        )
        self.display_label.pack(fill=tk.X)

        # Buttons Grid Container
        grid_frame = tk.Frame(self.root, bg=self.colors["bg"])
        grid_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=(0, 20))

        # Configure row and column weights for perfect button scaling
        for i in range(5):
            grid_frame.rowconfigure(i, weight=1)
        for j in range(4):
            grid_frame.columnconfigure(j, weight=1)

        # Define button layout (Label, Type, Grid Position)
        # Types: 'num' (Number/Decimal), 'op' (Operator), 'fn' (Function), 'eq' (Equal)
        buttons = [
            ("C", "fn", 0, 0), ("⌫", "fn", 0, 1), ("%", "fn", 0, 2), ("/", "op", 0, 3),
            ("7", "num", 1, 0), ("8", "num", 1, 1), ("9", "num", 1, 2), ("*", "op", 1, 3),
            ("4", "num", 2, 0), ("5", "num", 2, 1), ("6", "num", 2, 2), ("-", "op", 2, 3),
            ("1", "num", 3, 0), ("2", "num", 3, 1), ("3", "num", 3, 2), ("+", "op", 3, 3),
            ("+/-", "num", 4, 0), ("0", "num", 4, 1), (".", "num", 4, 2), ("=", "eq", 4, 3)
        ]

        # Dynamically build and style the buttons
        for text, btn_type, row, col in buttons:
            self.create_button(grid_frame, text, btn_type, row, col)

    def create_button(self, parent, text, btn_type, row, col):
        """Creates an interactive styled button and binds hover behaviors."""
        # Assign colors based on button categories
        if btn_type == "num":
            bg_color = self.colors["btn_num"]
            hover_color = self.colors["btn_num_hover"]
            fg_color = self.colors["text_primary"]
        elif btn_type == "op":
            bg_color = self.colors["btn_fn"]
            hover_color = self.colors["btn_num_hover"]
            fg_color = self.colors["btn_op"]
        elif btn_type == "fn":
            bg_color = self.colors["btn_fn"]
            hover_color = self.colors["btn_fn_hover"]
            fg_color = self.colors["text_primary"]
        else:  # Equals button 'eq'
            bg_color = self.colors["btn_eq"]
            hover_color = self.colors["btn_eq_hover"]
            fg_color = self.colors["text_eq"]

        # Use an underlying Frame to give buttons a nice, clean modern flat border look
        btn_frame = tk.Frame(parent, bg=self.colors["bg"], padx=4, pady=4)
        btn_frame.grid(row=row, column=col, sticky="nsew")

        btn = tk.Label(
            btn_frame,
            text=text,
            font=("Helvetica", 16, "bold" if btn_type in ["op", "eq"] else "normal"),
            bg=bg_color,
            fg=fg_color,
            anchor="center",
            cursor="hand2"
        )
        btn.pack(fill=tk.BOTH, expand=True)

        # Bind touch/mouse click interaction
        btn.bind("<Button-1>", lambda event, t=text: self.on_button_press(t))
        
        # Bind modern hover transition events
        btn.bind("<Enter>", lambda event, b=btn, h=hover_color: b.config(bg=h))
        btn.bind("<Leave>", lambda event, b=btn, orig=bg_color: b.config(bg=orig))

    def on_button_press(self, char):
        """Handles internal application logic for calculations and state management."""
        if char == "C":
            self.clear_all()
        elif char == "⌫":
            self.backspace()
        elif char == "%":
            self.percentage()
        elif char == "+/-":
            self.toggle_sign()
        elif char in ["+", "-", "*", "/"]:
            self.handle_operator(char)
        elif char == "=":
            self.calculate()
        else:  # Numbers and Decimal Point
            self.handle_number(char)

    def handle_number(self, char):
        """Handles number inputs, decimal checks, and display resets."""
        if self.new_input_start:
            self.current_input = char if char != "." else "0."
            self.new_input_start = False
        else:
            if char == "." and "." in self.current_input:
                return  # Prevent multiple decimals
            self.current_input += char

        self.update_display()

    def handle_operator(self, op):
        """Stacks expressions for consecutive operations."""
        if self.new_input_start and self.expression:
            # Change operator if pressed immediately after another operator
            self.expression = self.expression[:-1] + op
        else:
            # Remove trailing decimal points
            if self.current_input.endswith("."):
                self.current_input = self.current_input[:-1]
            self.expression += f" {self.current_input} {op}"
            
        self.new_input_start = True
        self.update_display(show_expression=True)

    def calculate(self):
        """Evaluates the mathematical expression and catches system/math errors safely."""
        if not self.expression and self.new_input_start:
            return  # Nothing to calculate

        # Polish current input state before final evaluation
        if self.current_input.endswith("."):
            self.current_input = self.current_input[:-1]

        full_expr = self.expression + f" {self.current_input}"
        
        try:
            # Safely evaluate using python's built-in interpreter scope (restricted globals)
            result = eval(full_expr, {"__builtins__": None}, {})
            
            # Format floating points nicely (avoid 0.30000000000000004 representation issues)
            if isinstance(result, float):
                if result.is_integer():
                    result = int(result)
                else:
                    result = round(result, 8)

            self.current_input = str(result)
            self.expression = ""
            self.new_input_start = True
            self.update_display(show_expression=False)
            self.formula_label.config(text=f"{full_expr} =")
        except ZeroDivisionError:
            self.show_error("Cannot divide by 0")
        except Exception:
            self.show_error("Math Error")

    def toggle_sign(self):
        """Toggles the current visual sign positive/negative."""
        if self.current_input != "0":
            if self.current_input.startswith("-"):
                self.current_input = self.current_input[1:]
            else:
                self.current_input = "-" + self.current_input
            self.update_display()

    def percentage(self):
        """Converts the active visual value to its percentage."""
        try:
            val = float(self.current_input) / 100
            self.current_input = str(int(val) if val.is_integer() else val)
            self.update_display()
        except ValueError:
            self.show_error("Error")

    def backspace(self):
        """Removes the last entered character."""
        if self.new_input_start:
            return
        self.current_input = self.current_input[:-1]
        if not self.current_input or self.current_input == "-":
            self.current_input = "0"
            self.new_input_start = True
        self.update_display()

    def clear_all(self):
        """Resets the state of the calculator completely."""
        self.expression = ""
        self.current_input = "0"
        self.new_input_start = True
        self.update_display(show_expression=True)

    def show_error(self, message):
        """Gracefully shows standard calculation errors."""
        self.current_input = message
        self.expression = ""
        self.new_input_start = True
        self.update_display()

    def update_display(self, show_expression=False):
        """Updates the physical Tkinter labels with live data formatting."""
        # Update main number screen
        formatted_val = self.current_input
        # Add cosmetic commas for integers to look professional
        if "Error" not in formatted_val and "divide" not in formatted_val:
            try:
                if "." not in formatted_val:
                    formatted_val = f"{int(formatted_val):,}"
                else:
                    parts = formatted_val.split(".")
                    formatted_val = f"{int(parts[0]):,}.{parts[1]}"
            except ValueError:
                pass # Fallback in case of weird formats

        # Reduce display text size if number starts spilling off the visual display window
        if len(formatted_val) > 12:
            self.display_label.config(font=("Helvetica", 22, "bold"))
        elif len(formatted_val) > 9:
            self.display_label.config(font=("Helvetica", 26, "bold"))
        else:
            self.display_label.config(font=("Helvetica", 32, "bold"))

        self.display_label.config(text=formatted_val)

        # Update top formulation screen
        if show_expression:
            self.formula_label.config(text=self.expression)

    def bind_keyboard(self):
        """Hooks system keyboard input to internal buttons."""
        self.root.bind("<Key>", self.on_key_press)
        self.root.bind("<BackSpace>", lambda event: self.on_button_press("⌫"))
        self.root.bind("<Return>", lambda event: self.on_button_press("="))
        self.root.bind("<Escape>", lambda event: self.on_button_press("C"))

    def on_key_press(self, event):
        """Routes character keystrokes to calculator logic."""
        char = event.char
        if char in "0123456789.":
            self.handle_number(char)
        elif char in "+-*/%":
            self.handle_operator(char)


if __name__ == "__main__":
    # Initialize main application thread
    root = tk.Tk()
    app = ModernCalculator(root)
    root.mainloop()