import customtkinter
from LoginScreen import LoginScreen
from RegisterScreen import RegisterScreen
from DashboardScreen import DashboardScreen

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.title("Budget Buddy")
root.geometry("600x450")

def dashboard():
    DashboardScreen(root, switch_to_login=login)

def register():
    RegisterScreen(root, switch_to_login=login)

def login():
    LoginScreen(root, switch_to_dashboard=dashboard, switch_to_register=register)

login()
root.mainloop()