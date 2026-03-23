import customtkinter
from backend.database import create_user
from backend.user import validate_registration

class RegisterScreen:
    def __init__(self, root, go_to_login):
        self.root = root
        self.go_to_login = go_to_login

        self.frame = customtkinter.CTkFrame(root)
        self.frame.pack(fill="both", expand=True, padx=20, pady=20)

        customtkinter.CTkLabel(self.frame, text="Register", font=("Roboto", 24)).pack(pady=10)

        self.last_name = customtkinter.CTkEntry(self.frame, placeholder_text="Last Name")
        self.last_name.pack(pady=5)

        self.first_name = customtkinter.CTkEntry(self.frame, placeholder_text="First Name")
        self.first_name.pack(pady=5)

        self.email = customtkinter.CTkEntry(self.frame, placeholder_text="Email")
        self.email.pack(pady=5)

        self.password = customtkinter.CTkEntry(self.frame, show="*", placeholder_text="Password")
        self.password.pack(pady=5)

        self.message = customtkinter.CTkLabel(self.frame, text="")
        self.message.pack()

        customtkinter.CTkButton(self.frame, text="Register", command=self.register).pack(pady=10)
        customtkinter.CTkButton(self.frame, text="Back", command=self.go_to_login).pack()

    def register(self):
        # Validation complète (password + email + doublon)
        valid, msg = validate_registration(
            self.last_name.get().strip(),
            self.first_name.get().strip(),
            self.email.get().strip(),
            self.password.get()
        )

        if not valid:
            self.message.configure(text=msg, text_color="red")
            return

        # Si tout est bon → on crée l'utilisateur
        success = create_user(
            self.last_name.get().strip(),
            self.first_name.get().strip(),
            self.email.get().strip(),
            self.password.get()
        )

        if success:
            self.message.configure(text="✅ Compte créé avec succès !", text_color="green")
            # Optionnel : rediriger vers login après 1 seconde
            self.root.after(1500, self.go_to_login)
        else:
            self.message.configure(text="❌ Erreur lors de la création", text_color="red")