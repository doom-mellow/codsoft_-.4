from tkinter import*
from PIL import Image,ImageTk
from random import randint
window=Tk()
window.title("Rock Paper Scissor")
window.configure(background="#ffb6c1")
window.iconbitmap(r'rps.ico')
window.geometry("900x320")

choices=["rock","paper","scissors"]

def updatechoice(x):

    cc=choices[randint(0,2)]
    if cc=="rock":
        c1.configure(image=rc)
    elif x=="paper":
        c1.configure(image=pc)
    else:
        c1.configure(image=sc)   

    checkwin(x,cc)

    if x=="rock":
        u1.configure(image=ru)
    elif x=="paper":
        u1.configure(image=pu)
    else:
        u1.configure(image=su)


def updatemsg(x):
    msg['text']=x

def updateps():
    score=int(ps["text"])
    score+=1
    ps["text"]=str(score)

def updatecs():
    score=int(cs["text"])
    score+=1
    cs["text"]=str(score)

def checkwin(p,c):
    if p==c:
        updatemsg("Its a Tie!!!")
    elif p=="rock":
        if c=="paper":
            updatemsg("You Loose :(")
            updatecs()
        else:
            updatemsg("You Win :)")
            updateps()
    elif p=="scissors":
        if c=="paper":
            updatemsg("You Win :)")
            updateps()
        else:
            updatemsg("You Loose :(")
            updatecs()
    elif p=="paper":
        if c=="rock":
            updatemsg("You Win :)")
            updateps()
        else:
            updatemsg("You Loose :(")
            updatecs()
    else:
        pass

            
ru=ImageTk.PhotoImage(Image.open("rockl.png"))
pu=ImageTk.PhotoImage(Image.open("paperl.png"))
su=ImageTk.PhotoImage(Image.open("scissorsl.png"))
rc=ImageTk.PhotoImage(Image.open("rockr.png"))
pc=ImageTk.PhotoImage(Image.open("paperr.png"))
sc=ImageTk.PhotoImage(Image.open("scissorsr.png"))


u1=Label(window,width=220,height=220,image=su,bg="#ffb6c1")
u1.grid(row=1,column=0)
c1=Label(window,width=220,height=220,image=sc,bg="#ffb6c1")
c1.grid(row=1,column=4)

l=Label(window,text="Player  Score",font=100,bg="#ffb6c1")
l.grid(row=0,column=1)
l=Label(window,text="Computer Score",font=100,bg="#ffb6c1")
l.grid(row=0,column=3)

ps=Label(window,text=0,font=100,bg="#ffb6c1")
ps.grid(row=1,column=1)
cs=Label(window,text=0,font=100,bg="#ffb6c1")
cs.grid(row=1,column=3)

msg=Label(window,text="",font=50,bg="#ffb6c1")
msg.grid(row=3,column=2)


b1=Button(window,width=20,height=2,text="ROCK",bg="#f6546a",command=lambda:updatechoice("rock"))
b1.grid(row=2,column=1)
b1=Button(window,width=20,height=2,text="PAPER",bg="#fff68f",command=lambda:updatechoice("paper"))
b1.grid(row=2,column=2)
b1=Button(window,width=20,height=2,text="SCISSORS",bg="#afeeee",command=lambda:updatechoice("scissors"))
b1.grid(row=2,column=3)



window.mainloop()
