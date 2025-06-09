import pywinstyles
from customtkinter import *
from PIL import Image
import random

app = CTk()
app.attributes("-fullscreen", True)
set_appearance_mode("system")

def clear_screen():
    for widget in app.winfo_children():
        widget.destroy()

# Currency class
class Currency():
    def __init__(self, balance=0):
        self.balance = balance

    def start_balance(self):
        self.balance += 1000
        return self.balance

    def add(self, amount):
        self.balance += amount
        return self.balance

    def subtract(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            self.balance = 50
        return self.balance

# Start Screen
class Start_Screen(CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(fill="both", expand=True)

        # Images
        img = Image.open("Culminating Files/Background/StartScreenImage.png")
        self.img = CTkImage(img, size=(app.winfo_screenwidth(), app.winfo_screenheight()))
        startImg = Image.open("Culminating Files/Sprites/Button/StartButton.png")
        self.startImg = CTkImage(startImg, size=(600, 600))
        shopImg = Image.open("Culminating Files/Sprites/Button/ShopButton.png")
        self.shopImg = CTkImage(shopImg, size=(600, 600))

        backLabel = CTkLabel(self, text="", image=self.img)
        backLabel.pack(fill="both", expand=True)

        def to_bet_screen():
            clear_screen()
            Bet_Screen(app)

        startLabel = CTkButton(self, text='', image=self.startImg, bg_color="#000001", fg_color="#000001", hover=False, corner_radius=50, command=to_bet_screen)
        startLabel.place(x=100, y=250)
        pywinstyles.set_opacity(startLabel, 0.7, color="#000001")

        Currency_Label = CTkLabel(self, text=f"Current Balance: ${Current_Currency.balance}", font=('PixelfySans', 40), text_color="white", bg_color="#000001", fg_color="#8BCF5E", width=600, height=200, corner_radius=80)
        Currency_Label.place(x=1, y=1)
        pywinstyles.set_opacity(Currency_Label, color="#000001")

        shopLabel = CTkButton(self, text='', image=self.shopImg, bg_color="#000001", fg_color="#000001", corner_radius=50, hover=False)
        shopLabel.place(x=100, y=500)
        pywinstyles.set_opacity(shopLabel, 0.7, color="#000001")

# Bet Screen
class Bet_Screen(CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(fill="both", expand=True)
        self.betAmount = 0

        # Background
        img = Image.open("Culminating Files/Background/betBackground.png")
        self.img = CTkImage(img, size=(app.winfo_screenwidth(), app.winfo_screenheight()))
        backLabel = CTkLabel(self, text="", image=self.img)
        backLabel.pack(fill="both", expand=True)

        # Currency label
        self.currency_label = CTkLabel(self, text=f"Current Balance: ${Current_Currency.balance}", font=('PixelfySans', 40), text_color="white", bg_color="#000000", fg_color="#8BCF5E", width=600, height=200, corner_radius=80)
        self.currency_label.place(x=1, y=1)
        pywinstyles.set_opacity(self.currency_label, color="#000000")

        # Button Images
        spritecontainer = Image.open("Culminating Files/Sprites/Button/spriteContainer.png")
        self.spritecontainer = CTkImage(spritecontainer, size=(1100, 1100))
        self.subbetImg = CTkImage(Image.open("Culminating Files/Sprites/Button/-Button.png"), size=(300, 300))
        self.subbetImg2 = CTkImage(Image.open("Culminating Files/Sprites/Button/-ButtonPress.png"), size=(300, 300))
        self.addbetImg = CTkImage(Image.open("Culminating Files/Sprites/Button/+Button.png"), size=(300, 300))
        self.addbetImg2 = CTkImage(Image.open("Culminating Files/Sprites/Button/+ButtonPush.png"), size=(300, 300))
        self.button5 = CTkImage(Image.open("Culminating Files/Sprites/Button/$5Button.png"), size=(300, 300))
        self.button52 = CTkImage(Image.open("Culminating Files/Sprites/Button/$5ButtonPush.png"), size=(300, 300))
        self.button10 = CTkImage(Image.open("Culminating Files/Sprites/Button/$10Button.png"), size=(300, 300))
        self.button102 = CTkImage(Image.open("Culminating Files/Sprites/Button/$10ButtonPush.png"), size=(300, 300))
        self.button100 = CTkImage(Image.open("Culminating Files/Sprites/Button/$100Button.png"), size=(300, 300))
        self.button1002 = CTkImage(Image.open("Culminating Files/Sprites/Button/$100ButtonPush.png"), size=(300, 300))
        self.acceptImg = CTkImage(Image.open("Culminating Files/Sprites/Button/Idleframe.png"), size=(400, 400))
        self.acceptImg2 = CTkImage(Image.open("Culminating Files/Sprites/Button/Pressframe.png"), size=(400, 400))

        # Button Functions
        def image_animation(image_idle, image_press, button):
            button.configure(image=image_press)
            button.after(100, lambda: button.configure(image=image_idle))
            if button == self.subtractbet:
                Current_Currency.add(self.betAmount)
                self.betAmount = 0
            elif button == self.bet5:
                if Current_Currency.balance >= 5:
                    self.betAmount += 5
                    Current_Currency.subtract(5)
            elif button == self.bet10:
                if Current_Currency.balance >= 10:
                    self.betAmount += 10
                    Current_Currency.subtract(10)
            elif button == self.bet100:
                if Current_Currency.balance >= 100:
                    self.betAmount += 100
                    Current_Currency.subtract(100)
            elif button == self.accept:
                if self.betAmount > 0:
                    clear_screen()
                    Play_Screen(app, self.betAmount)

            self.betLabel.configure(text=f"You are currently betting: ${self.betAmount}")
            self.currency_label.configure(text=f"Current Balance: ${Current_Currency.balance}")

        # Buttons
        self.subtractbet = CTkButton(self, text='', image=self.subbetImg, bg_color="#000001", fg_color="#000001", corner_radius=50, hover=False, command=lambda: image_animation(self.subbetImg, self.subbetImg2, self.subtractbet))
        self.subtractbet.place(x=200, y=650)
        pywinstyles.set_opacity(self.subtractbet, 0.8, color="#000001")

        containerLabel = CTkLabel(self, text='', image=self.spritecontainer, bg_color='#000001', corner_radius=50)
        containerLabel.place(x=400, y=250)
        pywinstyles.set_opacity(containerLabel, 0.8, color="#000001")

        self.bet5 = CTkButton(self, text='', image=self.button5, bg_color="#000001", fg_color="#000001", corner_radius=50, hover=False, command=lambda: image_animation(self.button5, self.button52, self.bet5))
        self.bet5.place(x=650, y=750)
        pywinstyles.set_opacity(self.bet5, 0.8, color="#000001")

        self.bet10 = CTkButton(self, text='', image=self.button10, bg_color="#000001", fg_color="#000001", corner_radius=50, hover=False, command=lambda: image_animation(self.button10, self.button102, self.bet10))
        self.bet10.place(x=800, y=750)
        pywinstyles.set_opacity(self.bet10, 0.8, color="#000001")

        self.bet100 = CTkButton(self, text='', image=self.button100, bg_color="#000001", fg_color="#000001", corner_radius=50, hover=False, command=lambda: image_animation(self.button100, self.button1002, self.bet100))
        self.bet100.place(x=950, y=750)
        pywinstyles.set_opacity(self.bet100, 0.8, color="#000001")

        self.accept = CTkButton(self, text='', image=self.acceptImg, bg_color="#000001", fg_color="#000001", corner_radius=50, hover=False, command=lambda: image_animation(self.acceptImg, self.acceptImg2, self.accept))
        self.accept.place(x=750, y=550)
        pywinstyles.set_opacity(self.accept, 0.8, color="#000001")

        self.betLabel = CTkLabel(self, text=f'You are currently betting: ${self.betAmount}', font=('Sans', 50), text_color="white", bg_color="#000001", fg_color="#000001", width=600, height=200, corner_radius=80)
        self.betLabel.place(x=650, y=400)
        pywinstyles.set_opacity(self.betLabel, color="#000001")

class Play_Screen(CTkFrame):
    def __init__(self, master, betAmount):
        super().__init__(master)
        self.pack(fill="both", expand=True)
        self.betAmount = betAmount
        self.posx = 600  # Track card placement

        # Card Deck
        self.cardDeck = []

        # Images
        img = Image.open("Culminating Files/Background/betBackground.png")
        self.img = CTkImage(img, size=(app.winfo_screenwidth(), app.winfo_screenheight())) 
        backGround = CTkLabel(self, text="", image=self.img)
        backGround.pack(fill="both", expand=True)

        # Load all card images into self.cardDeck
        self.cardDeck = [
            CTkImage(Image.open(f"Culminating Files/Sprites/Card/{name}.png"), size=(800, 800))
            for name in ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
        ]

        # Buttons
        self.hitImg = self.cardDeck[0]  # Placeholder to load real button image
        self.hitImg2 = self.cardDeck[1]
        self.standImg = self.cardDeck[2]
        self.standImg2 = self.cardDeck[3]

        hitImg = Image.open("Culminating Files/Sprites/Button/HitButton.png")
        self.hitImg = CTkImage(hitImg, size=(600, 600))
        hitImg2 = Image.open("Culminating Files/Sprites/Button/HitButtonPush.png")
        self.hitImg2 = CTkImage(hitImg2, size=(600, 600))
        standImg = Image.open("Culminating Files/Sprites/Button/Stand.png")
        self.standImg = CTkImage(standImg, size=(600, 600))
        standImg2 = Image.open("Culminating Files/Sprites/Button/StandPress.png")
        self.standImg2 = CTkImage(standImg2, size=(600, 600))

        # Currency Label
        Currency_Label = CTkLabel(self, text=f"Current Balance: ${Current_Currency.balance}",font=('PixelfySans', 40), text_color="white",bg_color="#000000",fg_color="#8BCF5E",width=600, height=200, corner_radius=80)
        Currency_Label.place(x=1, y=1)
        pywinstyles.set_opacity(Currency_Label, color="#000000")

        # Buttons
        hitButton = CTkButton(self, text='', image=self.hitImg, bg_color="#000001", fg_color="#000001", corner_radius=50, hover=False,
                              command=lambda: image_animation(self.hitImg, self.hitImg2, hitButton))
        hitButton.place(x=100, y=325)
        pywinstyles.set_opacity(hitButton, 0.8, color="#000001")

        standButton = CTkButton(self, text='', image=self.standImg, bg_color="#000001", fg_color="#000001", corner_radius=50, hover=False,
                                command=lambda: image_animation(self.standImg, self.standImg2, standButton))
        standButton.place(x=1150, y=325)
        pywinstyles.set_opacity(standButton, 0.8, color="#000001")

        # Initial player cards
        playerCard1 = CTkLabel(self, text='', image=random.choice(self.cardDeck), bg_color="#000001", fg_color="#000001", corner_radius=50)
        playerCard1.place(x=200, y=550)
        pywinstyles.set_opacity(playerCard1, 0.8, color="#000001")
        playerCard2 = CTkLabel(self, text='', image=random.choice(self.cardDeck), bg_color="#000001", fg_color="#000001", corner_radius=50)
        playerCard2.place(x=400, y=550)
        pywinstyles.set_opacity(playerCard2, 0.8, color="#000001")

        # Animation function
        def image_animation(image_idle, image_press, button):
            button.configure(image=image_press)
            button.after(100, lambda: button.configure(image=image_idle))
            if button == hitButton:
                newCard = CTkLabel(self, text='', image=random.choice(self.cardDeck), bg_color="#000001", fg_color="#000001", corner_radius=50)
                newCard.place(x=self.posx, y=550)
                pywinstyles.set_opacity(newCard, 0.8, color="#000001")
                self.posx += 200

# Rest of Play_Screen (no need to change local `posx` unless making a full class state)

# Initialize game
if __name__ == "__main__":
    y = 1
    if y == 1:
        Current_Currency = Currency()
        Current_Currency.start_balance()
        startScreen = Start_Screen(app)
        y += 1
    app.mainloop()
