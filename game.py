import random
from tkinter import *
from tkinter import messagebox

def button(frame):
    b=Button(frame,text="   ",font=('arial',40,'bold'),relief="sunken",bd=2)
    return b
def change_player():
    global Player
    for i in ['O','X']:
        if not(i==Player):
            Player=i
            break
def reset():
    global Player
    for i in range(3):
        for j in range(3):
                b[i][j]["text"]="   "
                b[i][j]["state"]=NORMAL
    Player=random.choice(['O','X'])

def check():
    for i in range(3):
            if(b[i][0]["text"]==b[i][1]["text"]==b[i][2]["text"]==Player or b[0][i]["text"]==b[1][i]["text"]==b[2][i]["text"]==Player):
                    messagebox.showinfo("Congrats!!","'"+Player+"' has won")
                    reset()
    if(b[0][0]["text"]==b[1][1]["text"]==b[2][2]["text"]==Player or b[0][2]["text"]==b[1][1]["text"]==b[2][0]["text"]==Player):
        messagebox.showinfo("Congrats!!","'"+Player+"' has won")
        reset()
    elif(b[0][0]["state"]==b[0][1]["state"]==b[0][2]["state"]==b[1][0]["state"]==b[1][1]["state"]==b[1][2]["state"]==b[2][0]["state"]==b[2][1]["state"]==b[2][2]["state"]==DISABLED):
        messagebox.showinfo("Tied!!","The match ended in a draw")
        reset()

def click(row,col):
        b[row][col].config(text=Player,state=DISABLED,disabledforeground=colour[Player])
        check()
        change_player()
        label.config(text=Player+"'s Chance")

if __name__=="__main__":
    root=Tk()
    root.title("Tic-Tac-Toe")
    Player=random.choice(['O','X'])
    colour={'O':"blue",'X':"green"}
    b=[[],[],[]]
    for i in range(3):
            for j in range(3):
                    b[i].append(button(root))
                    b[i][j].config(command= lambda row=i,col=j:click(row,col))
                    b[i][j].grid(row=i,column=j)
    label=Label(text=Player+"'s Chance",font=('arial',15,'bold'))
    label.grid(row=3,column=0,columnspan=3)
    root.mainloop()