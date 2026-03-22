from frontend.LoginScreen import LoginScreen
from frontend.RegisterScreen import RegisterScreen
from frontend.DashboardScreen import DashboardScreen
from frontend.TransactionScreen import TransactionScreen
from frontend.HistoryScreen import HistoryScreen

class ScreenHandler:
    def __init__(self, root):
        self.root = root

    def clear(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def display_login(self):
        self.clear()
        LoginScreen(self.root, self.display_dashboard, self.display_register)

    def display_register(self):
        self.clear()
        RegisterScreen(self.root, self.display_login)

    def display_dashboard(self, user):
        self.clear()
        DashboardScreen(
            self.root,
            user,
            self.display_login,
            self.display_transaction,
            self.display_history
        )

    def display_transaction(self, user, transaction_type):
        self.clear()
        TransactionScreen(
            self.root,
            user,
            transaction_type,
            lambda: self.display_dashboard(user)
        )

    def display_history(self, user):
        self.clear()
        HistoryScreen(
            self.root,
            user,
            lambda: self.display_dashboard(user)
        )