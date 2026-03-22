import customtkinter
from backend.transaction import get_transactions_by_user
from backend.filters import (
    filter_by_type,
    filter_by_category,
    filter_by_date,
    filter_by_period,
    sort_by_amount
)

class HistoryScreen:
    def __init__(self, root, user, go_back):
        self.user = user
        self.go_back = go_back

        self.frame = customtkinter.CTkFrame(root)
        self.frame.pack(fill="both", expand=True, padx=20, pady=20)

        customtkinter.CTkLabel(self.frame, text="History", font=("Roboto", 24)).pack(pady=10)

        self.type = customtkinter.CTkEntry(self.frame, placeholder_text="Type")
        self.type.pack(pady=5)

        self.category = customtkinter.CTkEntry(self.frame, placeholder_text="Category")
        self.category.pack(pady=5)

        self.date = customtkinter.CTkEntry(self.frame, placeholder_text="Date YYYY-MM-DD")
        self.date.pack(pady=5)

        self.sort = customtkinter.CTkOptionMenu(self.frame, values=["asc", "desc"])
        self.sort.pack(pady=5)

        customtkinter.CTkButton(self.frame, text="Search", command=self.search).pack(pady=10)

        self.results = customtkinter.CTkTextbox(self.frame, height=250)
        self.results.pack(fill="both", expand=True)

        customtkinter.CTkButton(self.frame, text="Back", command=self.go_back).pack(pady=10)

    def search(self):
        transactions = get_transactions_by_user(self.user["id"])

        if self.type.get():
            transactions = filter_by_type(transactions, self.type.get())

        if self.category.get():
            transactions = filter_by_category(transactions, self.category.get())

        if self.date.get():
            transactions = filter_by_date(transactions, self.date.get())

        transactions = sort_by_amount(transactions, self.sort.get())

        self.results.delete("1.0", "end")

        for t in transactions:
            line = f"{t['date']} | {t['type']} | {t['montant']}€ | {t['categorie']}\n"
            self.results.insert("end", line)