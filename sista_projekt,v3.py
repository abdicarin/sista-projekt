from tkinter import *
import random

# Skapa av Isac och Abdikariim
windows = Tk()
windows.geometry("400x500")
windows.title("Tkinter")
windows.maxsize(700, 700)
windows.minsize(300, 300)
windows.configure(bg="light green")

#skapat av isac och abdikariim
player_scores = [0, 0]
current_round_score = 0
current_player = 0  # 0 = Spelare 1, 1 = Spelare 2


# Funktion av Isac
def kasta_tarning():
    global current_round_score, current_player

    kast = random.randint(1, 6)
    dice_label.config(text=f"Tärning: {kast}")

    if kast == 1:
        current_round_score = 0
        round_score_label.config(text="Rundpoäng: 0")
        byt_spelare()
    else:
        current_round_score += kast
        round_score_label.config(text=f"Rundpoäng: {current_round_score}")
#funktion av abdikariim


def behall_poang():
    global player_scores, current_round_score, current_player


def byt_spelare(): #funktion av abdikariim
    global current_player, current_round_score
    current_player = 1 - current_player
    current_round_score = 0
    info_label.config(text=f"Spelare {current_player + 1}'s tur")


def nytt_spel():
    global player_scores, current_round_score, current_player
#skapad av abdikariim
def nytt_spel():
    global player_scores, current_round_score, current_player

    player_scores = [0, 0]
    current_round_score = 0
    current_player = 0
    score_label.config(text="Spelare 1: 0  Spelare 2: 0")
    round_score_label.config(text="Rundpoäng: 0")
    dice_label.config(text="Tärning: -")
    info_label.config(text="Spelare 1's tur")
    roll_button.config(state=NORMAL)
    hold_button.config(state=NORMAL)


#creating labels and buttons #skapat av abdikariim, tillägg av kommando av Isac
score_label= Label(windows,text="Spelare 1: 0  Spelare 2: 0", font=("Arial",14), bg="#768F70",fg="white")
score_label.pack(pady=10)

round_score_label =Label(windows,text="Rundpoäng: 0",font=("Arial",14), bg="#768F70",fg="white")
round_score_label.pack(pady=10)

dice_label =Label(windows, text="Tärning: -", font=("Arial",14), bg="#768F70",fg="white")
dice_label.pack(pady=10)

info_label =Label(windows, text="Spelare 1's tur", font=("Arial",14), bg="#768F70",fg="white")
info_label.pack(pady=10)

roll_button = Button(windows, text="Kasta Tärning", font=("Arial", 12), command=kasta_tarning)
roll_button.pack(pady=10)

hold_button =Button(windows,text="Behåll Poängen",font=("Arial",12), command=behall_poang)
hold_button.pack(pady=10)

# Av Isac
nytt_spel_button = Button(windows, text="Nytt Spel", font=("Arial", 12), command=nytt_spel)
nytt_spel_button.pack(pady=10)

windows.mainloop()
