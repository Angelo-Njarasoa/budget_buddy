from backend.database import create_user
import customtkinter


class RegisterScreen:
    def __init__(self, root, switch_to_login):
        self.root = root
        self.switch_to_login = switch_to_login

        self.frame = customtkinter.CTkScrollableFrame(master=root, orientation="vertical")
        self.frame.pack(pady=20, padx=60, fill="both", expand=True)

        self.label = customtkinter.CTkLabel(master=self.frame, text="Inscription", font=("Roboto", 24))
        self.label.pack(pady=12, padx=10)

        self.first_name_entry = customtkinter.CTkEntry(master=self.frame, placeholder_text="Prénom")
        self.first_name_entry.pack(pady=12, padx=10)

        self.last_name_entry = customtkinter.CTkEntry(master=self.frame, placeholder_text="Nom")
        self.last_name_entry.pack(pady=12, padx=10)
        
        self.email_entry = customtkinter.CTkEntry(master=self.frame, placeholder_text="Email")
        self.email_entry.pack(pady=12, padx=10)

        self.password_entry = customtkinter.CTkEntry(master=self.frame, placeholder_text="Mot de passe", show="*")
        self.password_entry.pack(pady=1, padx=10)

        self.message = customtkinter.CTkLabel(master=self.frame, text="")
        self.message.pack(pady=1)

        self.register_button = customtkinter.CTkButton(master=self.frame, text="S'inscrire", command=self.register)
        self.register_button.pack(pady=12, padx=10)

        self.back_button = customtkinter.CTkButton(master=self.frame, text="Retour", command=self.go_to_login)
        self.back_button.pack(pady=12, padx=10)


    def register(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()

        if not email or not password or not first_name or not last_name:
            self.message.configure(text="Veuillez remplir tous les champs", text_color="red")
            return

        success = create_user(last_name, first_name, email, password)

        if success:
            self.message.configure(text="Compte créé avec succès", text_color="green")
        else:
            self.message.configure(text="Email déjà utilisé ou erreur", text_color="red")

    def go_to_login(self):
        self.switch_to_login()
