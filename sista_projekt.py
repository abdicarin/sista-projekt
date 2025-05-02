from tkinter import *
import random

# Skapa av Isac
windows = Tk()
windows.geometry("400x500")
windows.title("Tkinter")
windows.maxsize(700, 700)
windows.minsize(300, 300)
windows.configure(bg="light green")

#skapat av isac
player_scores = [0, 0]
current_round_score = 0
current_player = 0  # 0 = Spelare 1, 1 = Spelare 2


#creating labels and buttons #skapat av abdikariim
score_label= Label(windows,text="Spelare 1: 0  Spelare 2: 0", font=("Arial",14), bg="#768F70",fg="white")
score_label.pack(pady=10)

round_score_label =Label(windows,text="Rundpoäng: 0",font=("Arial",14), bg="#768F70",fg="white")
round_score_label.pack(pady=10)

dice_label =Label(windows, text="Tärning: -", font=("Arial",14), bg="#768F70",fg="white")
dice_label.pack(pady=10)

info_label =Label(windows, text="Spelare 1's tur", font=("Arial",14), bg="#768F70",fg="white")
info_label.pack(pady=10)

roll_button=Button(windows,text="Kasta Tärning", font= ("Arial", 12),)
roll_button.pack(pady=10)

hold_button =Button(windows,text="Behåll Poängen",font=("Arial",12),)
hold_button.pack(pady=10)

windows.mainloop()
