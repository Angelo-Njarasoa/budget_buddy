import customtkinter
from backend.transaction import get_transactions_by_user
from backend.budgetmanagement import generate_summary

class DashboardScreen:
    def __init__(self, root, user, logout, go_to_transaction, go_to_history):
        self.root = root
        self.user = user

        self.frame = customtkinter.CTkFrame(root)
        self.frame.pack(fill="both", expand=True, padx=20, pady=20)

        customtkinter.CTkLabel(self.frame, text="Dashboard", font=("Roboto", 24)).pack(pady=10)

        transactions = get_transactions_by_user(user["id"])
        summary = generate_summary(transactions)

        customtkinter.CTkLabel(
            self.frame,
            text=f"Balance: {summary['balance']} €"
        ).pack(pady=5)

        customtkinter.CTkLabel(
            self.frame,
            text=f"Deposits: {summary['total_deposits']} €"
        ).pack()

        customtkinter.CTkLabel(
            self.frame,
            text=f"Withdrawals: {summary['total_withdrawals']} €"
        ).pack()

        if summary["overdrawn"]:
            customtkinter.CTkLabel(
                self.frame,
                text="⚠ Overdrawn!",
                text_color="red"
            ).pack(pady=5)

        customtkinter.CTkButton(
            self.frame, text="Deposit",
            command=lambda: go_to_transaction(user, "depot")
        ).pack(pady=5)

        customtkinter.CTkButton(
            self.frame, text="Withdraw",
            command=lambda: go_to_transaction(user, "retrait")
        ).pack(pady=5)

        customtkinter.CTkButton(
            self.frame, text="Transfer",
            command=lambda: go_to_transaction(user, "transfert")
        ).pack(pady=5)

        customtkinter.CTkButton(
            self.frame, text="History",
            command=lambda: go_to_history(user)
        ).pack(pady=5)

        customtkinter.CTkButton(
            self.frame, text="Logout",
            command=logout
        ).pack(pady=10)