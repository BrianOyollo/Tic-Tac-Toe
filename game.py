import tkinter as tk
from tkinter import Label, ttk
from tkinter import Menu
from tkinter import messagebox as mbox
win = tk.Tk()
win.title('Tic Tac Toe')

def checkWinner():
    """
    Checks if there's a winner
    B1,B2,B3,
    B4,B5,B6,
    B7,B8,B9
    """
    winner = False
    # if x wins
    if B1['text'] == 'X' and B2['text'] == 'X' and B3['text'] == 'X':
        B1.config(bg='green')
        B2.config(bg='green')
        B3.config(bg='green')
        winner = True
        mbox.showinfo('Tic Tac Toe', 'Congratulations!\nX wins')
    elif B4['text'] == 'X' and B5['text'] == 'X' and B6['text'] == 'X':
        B4.config(bg='green')
        B5.config(bg='green')
        B6.config(bg='green')
        winner = True
        mbox.showinfo('Tic Tac Toe', 'Congratulations!\nX wins')
    elif B7['text'] == 'X' and B8['text'] == 'X' and B9['text'] == 'X':
        B7.config(bg='green')
        B8.config(bg='green')
        B9.config(bg='green')
        winner = True
        mbox.showinfo('Tic Tac Toe', 'Congratulations!\nX wins')
    elif B1['text'] == 'X' and B4['text'] == 'X' and B7['text'] == 'X':
        B1.config(bg='green')
        B4.config(bg='green')
        B7.config(bg='green')
        winner = True
        mbox.showinfo('Tic Tac Toe', 'Congratulations!\nX wins')
    elif B2['text'] == 'X' and B5['text'] == 'X' and B8['text'] == 'X':
        B2.config(bg='green')
        B5.config(bg='green')
        B8.config(bg='green')
        winner = True
        mbox.showinfo('Tic Tac Toe', 'Congratulations!\nX wins')
    elif B3['text'] == 'X' and B6['text'] == 'X' and B9['text'] == 'X':
        B3.config(bg='green')
        B6.config(bg='green')
        B9.config(bg='green')
        winner = True
        mbox.showinfo('Tic Tac Toe', 'Congratulations!\nX wins')
    elif B3['text'] == 'X' and B5['text'] == 'X' and B7['text'] == 'X':
        B3.config(bg='green')
        B5.config(bg='green')
        B7.config(bg='green')
        winner = True
        mbox.showinfo('Tic Tac Toe', 'Congratulations!\nX wins')
    elif B3['text'] == 'X' and B5['text'] == 'X' and B7['text'] == 'X':
        B3.config(bg='green')
        B5.config(bg='green')
        B7.config(bg='green')
        winner = True
        mbox.showinfo('Tic Tac Toe', 'Congratulations!\nX wins')
    elif B1['text'] == 'X' and B5['text'] == 'X' and B9['text'] == 'X':
        B1.config(bg='green')
        B5.config(bg='green')
        B9.config(bg='green')
        winner = True
        mbox.showinfo('Tic Tac Toe', 'Congratulations!\nX wins')
    # if Y wins
    elif B1['text'] == 'O' and B2['text'] == 'O' and B3['text'] == 'O':
        B1.config(bg='green')
        B2.config(bg='green')
        B3.config(bg='green')
        winner = True
        mbox.showinfo('Tic Tac Toe', 'Congratulations!\nO wins')
    elif B4['text'] == 'O' and B5['text'] == 'O' and B6['text'] == 'O':
        B4.config(bg='green')
        B5.config(bg='green')
        B6.config(bg='green')
        winner = True
        mbox.showinfo('Tic Tac Toe', 'Congratulations!\nO wins')
    elif B7['text'] == 'O' and B8['text'] == 'O' and B9['text'] == 'O':
        B7.config(bg='green')
        B8.config(bg='green')
        B9.config(bg='green')
        winner = True
        mbox.showinfo('Tic Tac Toe', 'Congratulations!\nO wins')
    elif B1['text'] == 'O' and B4['text'] == 'O' and B7['text'] == 'O':
        B1.config(bg='green')
        B4.config(bg='green')
        B7.config(bg='green')
        winner = True
        mbox.showinfo('Tic Tac Toe', 'Congratulations!\nO wins')
    elif B2['text'] == 'O' and B5['text'] == 'O' and B8['text'] == 'O':
        B2.config(bg='green')
        B5.config(bg='green')
        B8.config(bg='green')
        winner = True
        mbox.showinfo('Tic Tac Toe', 'Congratulations!\nO wins')
    elif B3['text'] == 'O' and B6['text'] == 'O' and B9['text'] == 'O':
        B3.config(bg='green')
        B6.config(bg='green')
        B9.config(bg='green')
        winner = True
        mbox.showinfo('Tic Tac Toe', 'Congratulations!\nO wins')
    elif B3['text'] == 'O' and B5['text'] == 'O' and B7['text'] == 'O':
        B3.config(bg='green')
        B5.config(bg='green')
        B7.config(bg='green')
        winner = True
        mbox.showinfo('Tic Tac Toe', 'Congratulations!\nO wins')
    elif B3['text'] == 'O' and B5['text'] == 'O' and B7['text'] == 'O':
        B3.config(bg='green')
        B5.config(bg='green')
        B7.config(bg='green')
        winner = True
        mbox.showinfo('Tic Tac Toe', 'Congratulations!\nO wins')
    elif B1['text'] == 'O' and B5['text'] == 'O' and B9['text'] == 'O':
        B1.config(bg='green')
        B5.config(bg='green')
        B9.config(bg='green')
        winner = True
        mbox.showinfo('Tic Tac Toe', 'Congratulations!\nO wins')
    # if tie
    if count ==9 and winner == False:
        mbox.showinfo('Tic Tac Toe', "It's a tie !")   
        new_game


        


# player x's turn to play
player_x = True
count = 0

def button_click(btn):
    """ Checks if a button has been clicked. An already clicked button raises an error. """
    global player_x, count
    if btn['text'] == '' and player_x == True:
        btn['text'] = 'X'
        player_x = False
        count += 1
        checkWinner()
    elif btn['text'] == '' and player_x == False:
        btn['text'] = 'O'
        player_x= True
        count += 1
        checkWinner()
    else:
        mbox.showerror('Ti Tac Toe!', 'Invalid move!')



# buttons
def new_game():
    global B1, B2, B3, B4, B5, B6, B7, B8, B9
    global count
    B1 = tk.Button(win, width=8, height=4, text='', command=lambda: button_click(B1))
    B1.grid(column=0,row=0)
    B2 = tk.Button(win, width=8, height=4, text='',command=lambda: button_click(B2))
    B2.grid(column=1,row=0)
    B3 = tk.Button(win, width=8, height=4, text='',command=lambda: button_click(B3))
    B3.grid(column=2,row=0)
    B4 = tk.Button(win, width=8, height=4, text='',command=lambda: button_click(B4))
    B4.grid(column=0,row=1)
    B5 = tk.Button(win, width=8, height=4, text='',command=lambda:button_click(B5))
    B5.grid(column=1,row=1)
    B6 = tk.Button(win, width=8, height=4, text='',command=lambda:button_click(B6))
    B6.grid(column=2,row=1)
    B7 = tk.Button(win, width=8, height=4, text='',command=lambda:button_click(B7))
    B7.grid(column=0,row=2)
    B8 = tk.Button(win, width=8, height=4, text='',command=lambda:button_click(B8))
    B8.grid(column=1,row=2)
    B9 = tk.Button(win, width=8, height=4, text='',command=lambda:button_click(B9))
    B9.grid(column=2,row=2)


menu_bar = Menu(win)
win.config(menu=menu_bar)
gameMenu = Menu(menu_bar, tearoff=0)
gameMenu.add_command(label='New Game', command=new_game)
menu_bar.add_cascade(label = 'Options', menu = gameMenu)

new_game()
win.mainloop()