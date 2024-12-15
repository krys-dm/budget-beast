import tkinter as tk
from tkinter import messagebox, Toplevel


class BudgetTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Budget Beast - Budget Tracker")
        self.root.geometry("500x700")
        self.root.configure(bg="black")  # Set the background color to black

        # Variables
        self.income = tk.DoubleVar()
        self.expenses = {
            "Rent/Mortgage": tk.DoubleVar(),
            "Utilities": tk.DoubleVar(),
            "Bills": tk.DoubleVar(),
            "Groceries": tk.DoubleVar(),
            "Other Expenses": tk.DoubleVar(),
        }
        self.remaining_budget = tk.StringVar(value="0.00")
        self.savings_goal = tk.DoubleVar(value=500)  # Default savings goal

        # Remaining budget display
        self.remaining_label = tk.Label(
            root, text="REMAINING BUDGET:", font=("Arial", 20), fg="white", bg="black"
        )
        self.remaining_label.pack(pady=10)

        self.remaining_amount_label = tk.Label(
            root, textvariable=self.remaining_budget, font=("Arial", 40, "bold"), fg="green", bg="black"
        )
        self.remaining_amount_label.pack(pady=10)

        # Income input
        tk.Label(root, text="Enter Your Monthly Income:", font=("Arial", 14), fg="white", bg="black").pack(pady=5)
        self.income_entry = tk.Entry(root, textvariable=self.income, font=("Arial", 14), bg="#222222", fg="white")
        self.income_entry.pack(pady=5)

        # Expenses input
        tk.Label(root, text="Enter Your Monthly Expenses:", font=("Arial", 14), fg="white", bg="black").pack(pady=10)
        self.expense_entries = {}
        for category, var in self.expenses.items():
            frame = tk.Frame(root, bg="black")
            frame.pack(pady=5)
            tk.Label(frame, text=category, font=("Arial", 12), fg="white", bg="black").pack(side=tk.LEFT, padx=10)
            entry = tk.Entry(frame, textvariable=var, font=("Arial", 12), bg="#222222", fg="white")
            entry.pack(side=tk.LEFT)
            self.expense_entries[category] = entry

        # Buttons with high-contrast colors
        self.calculate_button = tk.Button(
            root,
            text="Calculate Remaining Budget",
            command=self.calculate_budget,
            bg="#FF4500",  # Bright orange-red
            fg="black",  # Black text for high contrast
            activebackground="#FF6347",  # Lighter orange-red for hover
            activeforeground="black",
            font=("Arial", 12, "bold"),
        )
        self.calculate_button.pack(pady=10)

        self.details_button = tk.Button(
            root,
            text="View Expense Details",
            command=self.open_details_window,
            bg="#00CED1",  # Bright teal
            fg="black",  # Black text for high contrast
            activebackground="#20B2AA",  # Lighter teal for hover
            activeforeground="black",
            font=("Arial", 12, "bold"),
        )
        self.details_button.pack(pady=10)

    def calculate_budget(self):
        """Calculate the remaining budget and update the progress bar."""
        try:
            total_income = self.income.get()
            total_expenses = sum(var.get() for var in self.expenses.values())
            remaining = total_income - total_expenses
            self.remaining_budget.set(f"${remaining:.2f}")


            # Update colors
            if remaining < 0:
                self.remaining_amount_label.config(fg="red")
            else:
                self.remaining_amount_label.config(fg="green")
        except tk.TclError:
            messagebox.showerror("Input Error", "Please enter valid numeric values for income and expenses.")

    def open_details_window(self):
        """Open a secondary window with detailed expense breakdown."""
        details_window = Toplevel(self.root)
        details_window.title("Expense Details")
        details_window.geometry("400x300")
        details_window.configure(bg="black")  # Black background for details window

        # Display total income and expenses
        tk.Label(details_window, text="Income & Expenses Breakdown", font=("Arial", 16), fg="white", bg="black").pack(pady=10)
        tk.Label(details_window, text=f"Total Income: ${self.income.get():.2f}", font=("Arial", 14), fg="white", bg="black").pack(pady=5)
        total_expenses = sum(var.get() for var in self.expenses.values())
        tk.Label(details_window, text=f"Total Expenses: ${total_expenses:.2f}", font=("Arial", 14), fg="white", bg="black").pack(pady=5)

        # Expense breakdown
        tk.Label(details_window, text="Expense Breakdown:", font=("Arial", 14), fg="white", bg="black").pack(pady=10)
        for category, var in self.expenses.items():
            tk.Label(details_window, text=f"{category}: ${var.get():.2f}", font=("Arial", 12), fg="white", bg="black").pack()

        # Close button
        tk.Button(
            details_window,
            text="Close",
            command=details_window.destroy,
            bg="#FF4500",  # Bright orange-red
            fg="black",  # Black text for high contrast
            activebackground="#FF6347",  # Lighter orange-red for hover
            activeforeground="black",
            font=("Arial", 12, "bold"),
        ).pack(pady=10)


# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = BudgetTracker(root)
    root.mainloop()
