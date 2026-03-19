import customtkinter

class DashboardScreen:
    def __init__(self, root, switch_to_login):
        self.root = root
        self.switch_to_login = switch_to_login

        self.frame = customtkinter.CTkFrame(master=root)
        self.frame.pack(pady=20, padx=60, fill="both", expand=True)

        self.label = customtkinter.CTkLabel(master=self.frame, text="Dashboard", font=("Roboto", 24))
        self.label.pack(pady=12, padx=10)

        self.message = customtkinter.CTkLabel(master=self.frame, text="ARGENT$")
        self.message.pack(pady=12, padx=10)

        self.back_button = customtkinter.CTkButton(master=self.frame, text="Se déconnecter", command=self.go_to_login)
        self.back_button.pack(pady=12, padx=10)

    def go_to_login(self):
        self.switch_to_login()