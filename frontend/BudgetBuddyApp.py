import customtkinter
from frontend.ScreenHandler import ScreenHandler

class BudgetBuddyApp:
    def __init__(self):
        self.root = customtkinter.CTk()
        self.root.title("Budget Buddy")
        self.root.geometry("500x350")

        customtkinter.set_appearance_mode("system")
        customtkinter.set_default_color_theme("dark-blue")

        self.handler = ScreenHandler(self.root)

    def run(self):
        self.handler.display_login()
        self.root.mainloop()