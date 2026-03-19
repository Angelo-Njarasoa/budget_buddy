import customtkinter

class LoginScreen:
    def __init__(self, root, switch_to_dashboard, switch_to_register):
        self.root = root
        self.switch_to_dashboard = switch_to_dashboard
        self.switch_to_register = switch_to_register

        self.frame = customtkinter.CTkScrollableFrame(master=root, orientation="vertical")
        self.frame.pack(pady=20, padx=60, fill="both", expand=True)

        self.label = customtkinter.CTkLabel(master=self.frame, text="Se connecter", font=("Roboto", 24))
        self.label.pack(pady=12, padx=10)

        self.email_entry = customtkinter.CTkEntry(master=self.frame, placeholder_text="Email")
        self.email_entry.pack(pady=12, padx=10)

        self.password_entry = customtkinter.CTkEntry(master=self.frame, placeholder_text="Mot de passe", show="*")
        self.password_entry.pack(pady=12, padx=10)

        self.message = customtkinter.CTkLabel(master=self.frame, text="")
        self.message.pack(pady=5)

        self.login_button =customtkinter.CTkButton(master=self.frame, text="Connexion", command=self.login)
        self.login_button.pack(pady=12, padx=10)

        self.register_button = customtkinter.CTkButton(master=self.frame, text="S'inscrire", command=self.go_to_register)
        self.register_button.pack(pady=12, padx=10)

    def login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        if email and password:
            self.switch_to_dashboard()
        else:
            self.message.configure(text="Veuillez remplir tous les champs", text_color="red")

    def go_to_register(self):
        self.switch_to_register()

        
