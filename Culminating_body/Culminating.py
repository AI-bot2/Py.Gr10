import pywinstyles
from customtkinter import *
from PIL import Image
app=CTk()
app.attributes("-fullscreen", True)
set_appearance_mode("system")
y=1

def clear_screen():
    for widget in app.winfo_children():
        widget.destroy()
#Currency classs & functions(•_•)
class Currency():
    def __init__(self,balance=0):
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
        startImg=Image.open("Culminating Files/Sprites/Button/StartButton.png")
        self.startImg=CTkImage(startImg, size=(600, 600))
        shopImg=Image.open("Culminating Files/Sprites/Button/ShopButton.png")
        self.shopImg=CTkImage(shopImg, size=(600, 600))

        
        backLabel = CTkLabel(self,text="",image=self.img)
        backLabel.pack(fill="both", expand=True)
        def to_bet_screen():
            clear_screen()
            Bet_Screen(app)
        #defining other widgets
        startLabel= CTkButton(self,text='',image=self.startImg, bg_color="#000001",fg_color="#000001",hover=False,corner_radius=50,command=to_bet_screen)
        startLabel.place(x=100,y=250)
        pywinstyles.set_opacity(startLabel, 0.7, color="#000001")

        Currency_Label = CTkLabel(self, text=f"Current Balance: ${Current_Currency.balance}",font=('PixelfySans', 40), text_color="white",bg_color="#000001",fg_color="#8BCF5E",width=600, height=200, corner_radius=80)
        Currency_Label.place(x=1, y=1)
        pywinstyles.set_opacity(Currency_Label, color="#000001")

        shopLabel=CTkButton(self,text='',image=self.shopImg, bg_color="#000001",fg_color="#000001",corner_radius=50,hover=False)
        shopLabel.place(x=100,y=500)
        pywinstyles.set_opacity(shopLabel, 0.7, color="#000001")
#play screen 

def image_animation(image_idle, image_press, button):
    button.configure(image=image_press)
    button.after(100, lambda: button.configure(image=image_idle))

class Bet_Screen(CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(fill="both", expand=True)
        #images
        img = Image.open("Culminating Files/Background/betBackground.png")
        self.img = CTkImage(img, size=(app.winfo_screenwidth(), app.winfo_screenheight())) 
        backLabel = CTkLabel(self, text="", image=self.img)
        backLabel.pack(fill="both", expand=True)
        #Currency widget
        Currency_Label = CTkLabel(self, text=f"Current Balance: ${Current_Currency.balance}",font=('PixelfySans', 40), text_color="white",bg_color="#000000",fg_color="#8BCF5E",width=600, height=200, corner_radius=80)
        Currency_Label.place(x=1, y=1)
        pywinstyles.set_opacity(Currency_Label, color="#000000")
        #load buttons
        spritecontainer = Image.open("Culminating Files/Sprites/Button/spriteContainer.png")
        self.spritecontainer = CTkImage(spritecontainer, size=(1100,1100))
        subbetImg = Image.open("Culminating Files/Sprites/Button/-Button.png")
        self.subbetImg = CTkImage(subbetImg, size=(300, 300))
        subbetImg2= Image.open("Culminating Files/Sprites/Button/-ButtonPress.png")
        self.subbetImg2 = CTkImage(subbetImg2, size=(300, 300))
        addbet= Image.open("Culminating Files/Sprites/Button/+Button.png")
        self.addbetImg = CTkImage(addbet, size=(300, 300))
        addbetImg2= Image.open("Culminating Files\Sprites\Button\+ButtonPush.png")
        self.addbetImg2 = CTkImage(addbetImg2, size=(300, 300))
        button5=Image.open("Culminating Files\Sprites\Button\$5Button.png")
        self.button5=CTkImage(button5, size=(300, 300))
        button52=Image.open("Culminating Files\Sprites\Button\$5ButtonPush.png")
        self.button52=CTkImage(button52, size=(300, 300))
        button10=Image.open("Culminating Files\Sprites\Button\$10Button.png")
        self.button10=CTkImage(button10, size=(300, 300))
        button102=Image.open("Culminating Files\Sprites\Button\$10ButtonPush.png")
        self.button102=CTkImage(button102, size=(300, 300))
        button100=Image.open("Culminating Files\Sprites\Button\$100Button.png")
        self.button100=CTkImage(button100, size=(300, 300))
        button1002=Image.open("Culminating Files\Sprites\Button\$100ButtonPush.png")
        self.button1002=CTkImage(button1002, size=(300, 300))
        acceptImg=Image.open("Culminating Files/Sprites/Button/Idleframe.png")
        self.acceptImg = CTkImage(acceptImg, size=(400, 400))
        acceptImg2=Image.open("Culminating Files/Sprites/Button/Pressframe.png")
        self.acceptImg2 = CTkImage(acceptImg2, size=(400, 400))


        #Test button transformation
        subtractbet= CTkButton(self, text='', image=self.subbetImg, bg_color="#000001",fg_color="#000001", corner_radius=50,hover=False, command=lambda:image_animation(self.subbetImg,self.subbetImg2,subtractbet))
        subtractbet.place(x=200, y=650)
        pywinstyles.set_opacity(subtractbet, 0.8, color="#000001")
        containerLabel = CTkLabel(self, text='',image=self.spritecontainer, bg_color='#000001', corner_radius=50)
        containerLabel.place(x=400, y=250)
        pywinstyles.set_opacity(containerLabel, 0.8, color="#000001")
        addbet=CTkButton(self,text='',image=self.addbetImg, bg_color="#000001",fg_color="#000001", corner_radius=50,hover=False, command=lambda:image_animation(self.addbetImg,self.addbetImg2,addbet))
        addbet.place(x=1400, y=650)
        pywinstyles.set_opacity(addbet, 0.8, color="#000001")
        bet5=CTkButton(self,text='',image=self.button5, bg_color="#000001",fg_color="#000001", corner_radius=50,hover=False, command=lambda:image_animation(self.button5,self.button52,bet5))
        bet5.place(x=650, y=750)
        pywinstyles.set_opacity(bet5, 0.8, color="#000001")
        bet10=CTkButton(self,text='',image=self.button10, bg_color="#000001",fg_color="#000001", corner_radius=50,hover=False, command=lambda:image_animation(self.button10,self.button102,bet10))
        bet10.place(x=800, y=750)
        pywinstyles.set_opacity(bet10, 0.8, color="#000001")
        bet100=CTkButton(self,text='',image=self.button100, bg_color="#000001",fg_color="#000001", corner_radius=50,hover=False, command=lambda:image_animation(self.button100,self.button1002,bet100))
        bet100.place(x=950, y=750)
        pywinstyles.set_opacity(bet100, 0.8, color="#000001")
        accept=CTkButton(self,text='',image=self.acceptImg, bg_color="#000001",fg_color="#000001", corner_radius=50,hover=False, command=lambda:image_animation(self.acceptImg,self.acceptImg2,accept))
        accept.place(x=750, y=550)
        pywinstyles.set_opacity(accept, 0.8, color="#000001")
        currentAddLabel=CTkLabel(self,text='', font=('PixelfySans', 40), text_color="white",bg_color="#000001",fg_color="#000001",width=600, height=200, corner_radius=80)
        currentAddLabel.place(x=750, y=400)
        pywinstyles.set_opacity(currentAddLabel, color="#000001")
        #Amount bet label
        betLabel=CTkLabel(self, text='', font=('Sans', 50), text_color="white", bg_color="#000001", fg_color="#000001", width=600, height=200, corner_radius=80)
        betLabel.place(x=650, y=400)
        pywinstyles.set_opacity(betLabel, color="#000001")

        
        

if y==1:                            #Currency starting balance
    Current_Currency=Currency()
    Current_Currency.start_balance()
    startScreen=Start_Screen(app)
    y+=1        



app.mainloop()