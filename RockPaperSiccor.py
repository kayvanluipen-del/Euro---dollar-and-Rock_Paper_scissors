from tkinter import *
import tkinter.font as font
import random 


Game_Window = Tk()
Game_Window.title("Rock Paper Scissors")
#Game_Window.config(Background= "white")
Game_Window.geometry("800x600")

app_font = font.Font(size=12)

game_title= Label(text="Rock Paper Scissors",font=font.Font(size=20),fg="grey")
game_title.pack()

winner_label= Label(text= "Lets start the game.",font=font.Font(size=15),fg="green",pady=8,padx=2)
winner_label.pack()


input_frame = Frame(Game_Window)
input_frame.pack()

player_options= Label(input_frame,text= "Your options    :",font=app_font,fg="grey")
player_options.grid(row=0,column=0,pady=8)

Rock_btn = Button(input_frame,text= "Rock",width=15,bg="pink",pady=5)
Rock_btn.grid(row=1,column=1,padx=8,pady=5)
Paper_btn = Button(input_frame,text= "Paper",width=15,bg="light blue",pady=5)
Paper_btn.grid(row=1,column=2,padx=8,pady=5)
Scissors_btn = Button(input_frame,text= "Scissors",width=15,bg="light green",pady=5)
Scissors_btn.grid(row=1,column=3,padx=8,pady=5)

Score_label= Label(input_frame,text= "Score   :",font=app_font,fg="grey")
Score_label.grid(row=2,column=0,pady=8)

Player_choice_label = Label(input_frame,text= "Your Selected  : ----", font= app_font)
Player_choice_label.grid(row=3,column=1,pady=5)

Player_score_label = Label(input_frame,text= "     Your Score : ----   ", font= app_font)
Player_score_label.grid(row=3,column=2,pady=5)

Computer_choice_label = Label(input_frame,text= "Computer Selected  : ----", font= app_font)
Computer_choice_label.grid(row=4,column=1,pady=5)

Computer_score_label = Label(input_frame,text= "     Copmuter Score : ----   ", font= app_font)
Computer_score_label.grid(row=4,column=2,pady=5)

Game_Window.mainloop()