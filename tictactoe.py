#Import libraries
import tkinter as tk
from tkinter import messagebox

##### FUNCTIONS #####
def click(row,col): #Update button after click - calls checkWinner and changeTurn
    b[row][col].config(text=turn,state="disabled")
    checkWinner()
    changeTurn()
    
def checkWinner(): #Check if the last move resulted in a winner
    global turn
    for i in range(3):
        if((b[i][0]["text"]==b[i][1]["text"]==b[i][2]["text"]==turn) or (b[0][i]["text"]==b[1][i]["text"]==b[2][i]["text"]==turn)):
            tk.messagebox.showinfo("Winner",turn+" Wins")
            reset()
    if((b[0][0]["text"]==b[1][1]["text"]==b[2][2]["text"]==turn) or (b[0][2]["text"]==b[1][1]["text"]==b[2][0]["text"]==turn)):
        tk.messagebox.showinfo("Winner",turn+" Wins")
        reset()
    elif(b[0][0]["state"]==b[0][1]["state"]==b[0][2]["state"]==b[1][0]["state"]==b[1][1]["state"]==b[1][2]["state"]==b[2][0]["state"]==b[2][1]["state"]==b[2][2]["state"]=="disabled"):
        tk.messagebox.showinfo("Tie","Tie Game")
        reset()

def changeTurn(): #Change to the next player's turn
    global turn
    if(turn=="X"):
        turn="O"
        ##Add Logic here if play against bot is selected##
    else:
        turn="X"
    label.config(text=turn+"'s Turn")

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
b = [[0,0,0],[0,0,0],[0,0,0]]
for x in range(3):
    for y in range(3):
        b[x][y] = tk.Button(frame, text=" ", width=10, command=lambda x=x,y=y:click(x,y))
        b[x][y].grid(column=x, row=y)

#Create label to publish turn order
label = tk.Label(text=turn+"'s Turn")
label.grid(row=3,column=0,columnspan=3)

root.mainloop()
