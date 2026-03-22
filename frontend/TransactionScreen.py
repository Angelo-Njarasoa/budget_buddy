import customtkinter
from backend.transaction import add_transaction
from datetime import datetime

class TransactionScreen:
    def __init__(self, root, user, transaction_type, go_back):
        self.user = user
        self.transaction_type = transaction_type
        self.go_back = go_back

        self.frame = customtkinter.CTkFrame(root)
        self.frame.pack(fill="both", expand=True, padx=20, pady=20)

        customtkinter.CTkLabel(self.frame, text=transaction_type, font=("Roboto", 24)).pack(pady=10)

        self.amount = customtkinter.CTkEntry(self.frame, placeholder_text="Amount")
        self.amount.pack(pady=10)

        self.description = customtkinter.CTkEntry(self.frame, placeholder_text="Description")
        self.description.pack(pady=5)

        self.category = customtkinter.CTkEntry(self.frame, placeholder_text="Category")
        self.category.pack(pady=5)

        self.message = customtkinter.CTkLabel(self.frame, text="")
        self.message.pack()

        customtkinter.CTkButton(self.frame, text="Submit", command=self.submit).pack(pady=10)
        customtkinter.CTkButton(self.frame, text="Back", command=self.go_back).pack()

    def submit(self):
        try:
            amount = float(self.amount.get())

            add_transaction(
                user_id=self.user["id"],
                reference="UI",
                amount=amount,
                transaction_type=self.transaction_type,
                description=self.description.get(),
                category=self.category.get(),
                date=datetime.now()
            )

            self.message.configure(text="Success", text_color="green")

        except:
            self.message.configure(text="Error", text_color="red")