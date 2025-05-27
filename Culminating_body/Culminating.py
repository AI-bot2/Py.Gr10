from customtkinter import *
from PIL import Image
balance=0
app=CTk()
app.geometry("700x500")
set_appearance_mode("system")

#Currency classs & functions(•_•)
class Currency():
    def __init__(self,balance):
        self.balance = balance
    def start_balance(self):
        self.balance+=1000
        return self.balance
    
    def add(self, amount):
        self.balance += amount
        return self.balance
    def subtract(self, amount):
        if self.balance>= amount:
            self.balance -= amount
        else:
            self.balance = 50
        return self.balance
 

    




app.mainloop()