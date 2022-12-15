import tkinter

import random 
screen = tkinter.Tk()

screen.title("Game")
screen.geometry("600x600")

game = ["ROCK","PAPER","SCISSOR"]
var_user_choice = tkinter.StringVar()
var_result = tkinter.StringVar()
var_result.set("RESULT")
def myfun(user_choice):
    var_user_choice.set(user_choice)
    com_choice = random.choice(game)
    print("---> com choice = ",com_choice)
    print("====> button clicked",user_choice)

    if user_choice == com_choice:
        var_result.set("TIE")

    

title = tkinter.Label(screen,text = "ROCK PAPER SCISSOR",font = ('arial',20,'bold'))
title.place(x = 150,y = 10)

btn = tkinter.Button(screen,text = "ROCK",bg = "blue",fg = "white",font = ('arial',15,'bold'),activebackground = "red",activeforeground = "white",command=lambda :myfun("ROCK"))
btn.place(x = 10,y = 100)

btn = tkinter.Button(screen,text = "PAPER",bg = "blue",fg = "white",font = ('arial',15,'bold'),activebackground = "red",activeforeground = "white",command=lambda :myfun("PAPER"))
btn.place(x = 250,y = 100)

btn = tkinter.Button(screen,text = "SCISSOR",bg = "blue",fg = "white",font = ('arial',15,'bold'),activebackground = "red",activeforeground = "white",command=lambda :myfun("SCISSOR"))
btn.place(x = 450,y = 100)

title = tkinter.Label(screen,text = "USER",font = ('arial',15,'bold'))
title.place(x = 10,y = 175)

title = tkinter.Label(screen,textvariable=var_user_choice,font = ('arial',15,'bold'))
title.place(x = 250,y = 175)

title = tkinter.Label(screen,text = "0",font = ('arial',15,'bold'))
title.place(x = 450,y = 175)

title = tkinter.Label(screen,text = "COMPUTER",font = ('arial',15,'bold'))
title.place(x = 10 ,y = 225 )

title = tkinter.Label(screen,text = "PAPER",font = ('arial',15,'bold'))
title.place(x =250,y = 225)

title = tkinter.Label(screen,text = "0",font = ('arial',15,'bold'))
title.place(x =450,y = 225)

btn = tkinter.Button(screen,textvariable=var_result,bg = "blue",fg = "white",font = ('arial',25,'bold'),activebackground = "red",activeforeground = "white")
btn.place(x = 250,y = 300)

screen.mainloop()