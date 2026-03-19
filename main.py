import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from frontend.BudgetBuddyApp import BudgetBuddyApp 

if __name__ == "__main__":
    app = BudgetBuddyApp()
    app.run()