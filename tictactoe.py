#Import libraries
import tkinter as tk
from tkinter import messagebox
import random
##### FUNCTIONS #####
def click(row,col): #Update button after click - calls checkWinner and changeTurn
    b[row][col].config(text=turn,state="disabled")
    checkWinner()
    changeTurn()
    
def checkWinner(): #Check if the last move resulted in a winner
    global turn
    global scoreX
    global scoreY
    for i in range(3):
        if((b[i][0]["text"]==b[i][1]["text"]==b[i][2]["text"]==turn) or (b[0][i]["text"]==b[1][i]["text"]==b[2][i]["text"]==turn)):
            if(turn == "X"):
                scoreX += 1
            else:
                scoreY += 1
            tk.messagebox.showinfo(turn+" Wins","Score:\n X-"+str(scoreX)+"\n O-"+str(scoreY))
            reset()
    if((b[0][0]["text"]==b[1][1]["text"]==b[2][2]["text"]==turn) or (b[0][2]["text"]==b[1][1]["text"]==b[2][0]["text"]==turn)):
        if(turn == "X"):
            scoreX += 1
        else:
            scoreY += 1
        tk.messagebox.showinfo(turn+"Wins","Score:\n X-"+str(scoreX)+"\n O-"+str(scoreY))
        reset()
    elif(b[0][0]["state"]==b[0][1]["state"]==b[0][2]["state"]==b[1][0]["state"]==b[1][1]["state"]==b[1][2]["state"]==b[2][0]["state"]==b[2][1]["state"]==b[2][2]["state"]=="disabled"):
        tk.messagebox.showinfo("Tie","Score:\n X-"+str(scoreX)+"\n O-"+str(scoreY))
        reset()

def changeTurn(): #Change to the next player's turn
    global turn
    if(turn=="X"):
        turn="O"
        compTurn()
    else:
        turn="X"
    label.config(text=turn+"'s Turn")

def compTurn(): #Computer's Turn
    clicked = 0
    if(b[1][1]["state"]=="normal"): #always take the middle
        clicked = 1
        click(1,1)        
    else: 
        for i in range(3): #check for victory
            if((b[i][0]["text"]==b[i][1]["text"]==turn) and b[i][2]["state"]=="normal"): #horizontal win (i,2)
                clicked = 1
                click(i,2)
                break
            elif ((b[i][1]["text"]==b[i][2]["text"]==turn) and b[i][0]["state"]=="normal"): #horizontal win (i,0)
                clicked = 1
                click(i,0)
                break
            elif ((b[i][2]["text"]==b[i][0]["text"]==turn) and b[i][1]["state"]=="normal"): #horizontal win (i,1)
                clicked = 1
                click(i,1)
                break
            elif ((b[0][i]["text"]==b[1][i]["text"]==turn) and b[2][i]["state"]=="normal"): #vertical win (2,i)
                clicked = 1
                click(2,i)
                break
            elif ((b[1][i]["text"]==b[2][i]["text"]==turn) and b[0][i]["state"]=="normal"): #vertical win (0,i)
                clicked = 1
                click(0,i)
                break
            elif ((b[0][i]["text"]==b[2][i]["text"]==turn) and b[1][i]["state"]=="normal"): #vertical win (1,i)
                clicked = 1
                click(1,i)
                break
        while clicked==0: #random click
            i = random.randint(0,2)
            j = random.randint(0,2)
            if(b[i][j]["state"]=="normal"):
                clicked = 1
                click(i,j)
        

def reset(): #Resets the game
    global turn
    for x in range(3):
        for y in range(3):
                b[x][y]["text"]=" "
                b[x][y]["state"]="normal"
    turn = "O"
                
##### MAIN PROGRAM #####
#Initialize frame
root = tk.Tk()
root.title("Tic Tac Toe")
frame = tk.Frame(root)
frame.grid(row=0,column=0)

#Add message here to determine if 2 player game or 1 player vs computer

#Create 9 buttons and assign funciton click to them
numTurns = 0
turn = "X"
scoreX = 0
scoreY = 0
b = [[0,0,0],[0,0,0],[0,0,0]]
for x in range(3):
    for y in range(3):
        b[x][y] = tk.Button(frame, text=" ", width=10, command=lambda x=x,y=y:click(x,y))
        b[x][y].grid(column=x, row=y)

#Create label to publish turn order
label = tk.Label(text=turn+"'s Turn")
label.grid(row=3,column=0,columnspan=3)

root.mainloop()
