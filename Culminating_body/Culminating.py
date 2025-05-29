import pywinstyles
from customtkinter import *
from PIL import Image
balance=0
app=CTk()
app.attributes("-fullscreen", True)
set_appearance_mode("system")
x=1

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

#Creating a start screen
class Start_Screen(CTkFrame):
    def __init__(self,master):
        super().__init__(master)
        self.pack(fill="both", expand=True)
        #images
        img=Image.open("Culminating Files/Background/StartScreenImage.png")
        self.img = CTkImage(img, size=(app.winfo_screenwidth(), app.winfo_screenheight()))
        startImg=Image.open("Culminating Files\Sprites\Button\StartButton.png")
        self.startImg=CTkImage(startImg, size=(400, 400))

        
        backLabel = CTkLabel(self,text="",image=self.img)
        backLabel.pack(fill="both", expand=True)
        
        #defining other widgets
        startLabel= CTkButton(self,text='',image=self.startImg, bg_color="#000001",corner_radius=50)
        startLabel.place(x=200,y=400)
        pywinstyles.set_opacity(startLabel, 0.7, color="#000001")


    


if x==1:
    start_screen = Start_Screen(app)
elif x==2:
    # Placeholder for another screen, e.g., a login screen
    pass

app.mainloop()