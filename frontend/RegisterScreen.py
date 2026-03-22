import customtkinter
from backend.database import create_user
from backend.user import validate_password

class RegisterScreen:
    def __init__(self, root, go_to_login):
        self.root = root
        self.go_to_login = go_to_login

        self.frame = customtkinter.CTkFrame(root)
        self.frame.pack(fill="both", expand=True, padx=20, pady=20)

        customtkinter.CTkLabel(self.frame, text="Register", font=("Roboto", 24)).pack(pady=10)

        self.nom = customtkinter.CTkEntry(self.frame, placeholder_text="Last Name")
        self.nom.pack(pady=5)

        self.prenom = customtkinter.CTkEntry(self.frame, placeholder_text="First Name")
        self.prenom.pack(pady=5)

        self.email = customtkinter.CTkEntry(self.frame, placeholder_text="Email")
        self.email.pack(pady=5)

        self.password = customtkinter.CTkEntry(self.frame, show="*", placeholder_text="Password")
        self.password.pack(pady=5)

        self.message = customtkinter.CTkLabel(self.frame, text="")
        self.message.pack()

        customtkinter.CTkButton(self.frame, text="Register", command=self.register).pack(pady=10)
        customtkinter.CTkButton(self.frame, text="Back", command=self.go_to_login).pack()

    def register(self):
        valid, msg = validate_password(self.password.get())

        if not valid:
            self.message.configure(text=msg, text_color="red")
            return

        success = create_user(
            self.nom.get(),
            self.prenom.get(),
            self.email.get(),
            self.password.get()
        )

        if success:
            self.message.configure(text="Account created", text_color="green")
        else:
            self.message.configure(text="Error", text_color="red")