import customtkinter
from backend.database import login

class LoginScreen:
    def __init__(self, root, go_to_dashboard, go_to_register):
        self.root = root
        self.go_to_dashboard = go_to_dashboard
        self.go_to_register = go_to_register

        self.frame = customtkinter.CTkFrame(root)
        self.frame.pack(fill="both", expand=True, padx=20, pady=20)

        customtkinter.CTkLabel(self.frame, text="Login", font=("Roboto", 24)).pack(pady=10)

        self.email = customtkinter.CTkEntry(self.frame, placeholder_text="Email")
        self.email.pack(pady=10)

        self.password = customtkinter.CTkEntry(self.frame, show="*", placeholder_text="Password")
        self.password.pack(pady=10)

        self.message = customtkinter.CTkLabel(self.frame, text="")
        self.message.pack()

        customtkinter.CTkButton(self.frame, text="Login", command=self.login).pack(pady=10)
        customtkinter.CTkButton(self.frame, text="Register", command=self.go_to_register).pack()

    def login(self):
        user = login(self.email.get(), self.password.get())

        if user:
            self.go_to_dashboard(user)
        else:
            self.message.configure(text="Invalid credentials", text_color="red")