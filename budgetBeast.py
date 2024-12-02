"""

Budget Beast, Budget Tracker

This program tracks finances and budgets.

- User inputs income and expenses.
- Categories include Rent/Mortgage, Utilities, Bills, Groceries, and Other Expenses.
- Displays the remaining budget dynamically.


"""


import tkinter as tk
from http.cookiejar import uppercase_escaped_char
from tkinter import messagebox

class BudgetTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Budget Beast - Budget Tracker")

        # Initialize variables
        self.income = tk.DoubleVar()
        self.expenses = {
            "Rent/Mortgage": tk.DoubleVar(),
            "Utilities": tk.DoubleVar(),
            "Bills": tk.DoubleVar(),
            "Groceries": tk.DoubleVar(),
            "Other Expenses": tk.DoubleVar(),
        }
        self.remaining_budget = tk.StringVar(value="0.00")

        # Remaining budget display
        self.remaining_label = tk.Label(
            root, text="REMAINING BUDGET\nfor this month:", font=("Arial", 30, ), fg="pink"
        )
        self.remaining_label.pack(pady=10)

        self.remaining_amount_label = tk.Label(
            root, textvariable=self.remaining_budget, font=("Arial", 46), fg="pink"
        )
        self.remaining_amount_label.pack(pady=10)

        # Income input
        tk.Label(root, text="Enter Your Monthly Income:", font=("Arial", 14)).pack(pady=5)
        self.income_entry = tk.Entry(root, textvariable=self.income, font=("Arial", 14))
        self.income_entry.pack(pady=5)

        # Expenses input
        tk.Label(root, text="Enter Your Monthly Expenses:", font=("Arial", 14)).pack(pady=10)
        self.expense_entries = {}
        for category, var in self.expenses.items():
            frame = tk.Frame(root)
            frame.pack(pady=5)
            tk.Label(frame, text=category, font=("Arial", 12)).pack(side=tk.LEFT, padx=10)
            entry = tk.Entry(frame, textvariable=var, font=("Arial", 12))
            entry.pack(side=tk.LEFT)
            self.expense_entries[category] = entry

        # Buttons
        self.calculate_button = tk.Button(
            root, text="Calculate Remaining Budget", command=self.calculate_budget, font=("Arial", 14)
        )
        self.calculate_button.pack(pady=20)

    def calculate_budget(self):
        """Calculates the remaining budget."""
        try:
            total_income = self.income.get()
            total_expenses = sum(var.get() for var in self.expenses.values())
            remaining = total_income - total_expenses

            self.remaining_budget.set(f"${remaining:.2f}")

            # Update the color based on remaining budget
            if remaining < 0:
                self.remaining_amount_label.config(fg="red")
            else:
                self.remaining_amount_label.config(fg="green")
        except tk.TclError:
            messagebox.showerror("Input Error", "Please enter valid numeric values for income and expenses.")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = BudgetTracker(root)
    root.mainloop()
