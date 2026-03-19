from frontend.RegisterScreen import RegisterScreen
from frontend.LoginScreen import LoginScreen
from frontend.DashboardScreen import DashboardScreen

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

    def display_dashboard(self):
        self.clear()
        DashboardScreen(self.root, switch_to_login=self.display_login)