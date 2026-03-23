import customtkinter
from backend.transaction import add_transaction, make_transfer
from datetime import datetime
from backend.database import get_user_by_email


class TransactionScreen:
    def __init__(self, root, user, transaction_type, go_back):
        self.user = user
        self.transaction_type = transaction_type.lower()
        self.go_back = go_back

        self.frame = customtkinter.CTkFrame(root)
        self.frame.pack(fill="both", expand=True, padx=20, pady=20)

        customtkinter.CTkLabel(self.frame, text=transaction_type.capitalize(), font=("Roboto", 24)).pack(pady=10)

        self.amount = customtkinter.CTkEntry(self.frame, placeholder_text="Amount")
        self.amount.pack(pady=10)

        self.description = customtkinter.CTkEntry(self.frame, placeholder_text="Description")
        self.description.pack(pady=5)

        # Category field for deposit and withdrawal
        if self.transaction_type in ["depot", "retrait"]:
            self.category = customtkinter.CTkEntry(self.frame, placeholder_text="Category")
            self.category.pack(pady=5)

        # Recipient email field for transfer
        if self.transaction_type == "transfert":
            self.recipient_email = customtkinter.CTkEntry(self.frame, placeholder_text="Recipient Email")
            self.recipient_email.pack(pady=5)

        self.message = customtkinter.CTkLabel(self.frame, text="")
        self.message.pack(pady=5)

        customtkinter.CTkButton(self.frame, text="Submit", command=self.submit).pack(pady=10)
        customtkinter.CTkButton(self.frame, text="Back", command=self.go_back).pack()

    def submit(self):
        try:
            amount = float(self.amount.get())
            description = self.description.get().strip() or "No description"

            if self.transaction_type == "transfert":
                email = self.recipient_email.get().strip()
                if not email:
                    self.message.configure(text="Recipient email required", text_color="red")
                    return

                dest_user = get_user_by_email(email)
                if not dest_user:
                    self.message.configure(text="Recipient not found", text_color="red")
                    return

                make_transfer(
                    sender_id=self.user["id"],
                    recipient_id=dest_user["id"],
                    amount=amount,
                    description=description
                )
                self.message.configure(text="Transfer successful! (both accounts updated)", text_color="green")

            else:
                # Deposit or Withdrawal
                category = getattr(self, 'category', None)
                cat_value = category.get().strip() if category else "salaire"

                add_transaction(
                    user_id=self.user["id"],
                    amount=amount,
                    transaction_type=self.transaction_type,
                    description=description,
                    date=datetime.now(),
                    category=cat_value
                )
                self.message.configure(text="Transaction successful!", text_color="green")

        except ValueError:
            self.message.configure(text="Invalid amount", text_color="red")
        except Exception as e:
            self.message.configure(text=f"Error: {str(e)}", text_color="red")