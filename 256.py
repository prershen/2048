# code to implement 256

# all imports
import random
import sqlite3
import datetime
import tkinter

# to record player scores
score = 0
highest_tile = 0
player_name = ""
flag_new = [0] * 3  # this is for adding tiles only when the move has resulted in some change

# to initialize
GAME=[0]*9
GAME=reshape(GAME,(3,3),'C')
random_numbers = [2, 4]
random_index = [0, 1, 2]
index1 = [random.choice(random_index), random.choice(random_index)]
GAME[index1[0], index1[1]] = random.choice(random_numbers)
index2 = [random.choice(random_index), random.choice(random_index)]
while index2 == index1:
    index2 = [random.choice(random_index), random.choice(random_index)]
GAME[index2[0], index2[1]] = random.choice(random_numbers)


# to display the grid
def display():
    for xx in range(3):
        for yy in range(3):
            print (GAME[xx][yy]),
        print("\n")


# this part is for GUI using Tkinter

root = tkinter.Tk()  # to create object(makes a blank window)


def display_game():
    global root

    BACKGROUND_DICT = {0: "#92877d", 2: "#eee4da", 4: "#ede0c8", 8: "#f2b179", 16: "#f59563", \
                       32: "#f67c5f", 64: "#f65e3b", 128: "#edcf72", 256: "#edcc61"}
    CELL_COLOR_DICT = {0: "#9e948a", 2: "#776e65", 4: "#776e65", 8: "#f9f6f2", 16: "#f9f6f2", \
                       32: "#f9f6f2", 64: "#f9f6f2", 128: "#f9f6f2", 256: "#f9f6f2"}

    # to display the tiles
    for r in range(3):
        for c in range(3):
            tkinter.Label(root, text=GAME[r][c], borderwidth=1, bg=BACKGROUND_DICT[GAME[r][c]],
                          fg=CELL_COLOR_DICT[GAME[r][c]], height=5, width=5).grid(row=r, column=c, padx=2, pady=2)

    # to display score tile
    tkinter.Label(root, text='SCORE: %s' % score, bg='#00cdcd').grid(row=3, columnspan=3)

    # for control buttons and exit
    tkinter.Button(root, text="up", bg="#00bfff", fg="#ff0000", command=up).grid(row=4, columnspan=3)
    tkinter.Button(root, text="left", bg="#00bfff", fg="#ff0000", command=left).grid(row=5, column=0)
    tkinter.Button(root, text="down", bg="#00bfff", fg="#ff0000", command=down).grid(row=5, column=1)
    tkinter.Button(root, text="right", bg="#00bfff", fg="#ff0000", command=right).grid(row=5, column=2)
    tkinter.Button(root, text="EXIT", bg="red", fg="#ffffff", command=out).grid(row=6, columnspan=3)

    # to display continuously
    root.mainloop()


# to close GUI
def out():
    root.destroy()


# for game controls
def down():
    global flag, score, GAME
    flag = [0] * 3
    for i in range(0, 3):
        for j in range(0, 2):
            if GAME[j + 1][i] == 0 and GAME[j][i] != 0:
                GAME[j + 1][i], GAME[j][i] = GAME[j][i], GAME[j + 1][i]
                flag[i] = 1
            elif GAME[j + 1][i] == GAME[j][i] and GAME[j][i] != 0 and flag[i] != 2:
                flag[i] = 2
                if j == 0 and GAME[j + 2][i] == GAME[j + 1][i]:
                    GAME[j + 2][i] *= 2
                    GAME[j + 1][i] = 0
                    GAME[j + 1][i], GAME[j][i] = GAME[j][i], GAME[j + 1][i]
                    score += GAME[j + 2][i]
                else:
                    GAME[j][i] = 0
                    GAME[j + 1][i] *= 2
                    score += GAME[j + 1][i]
    for i in range(0, 3):
        for j in range(0, 2):
            if GAME[j + 1][i] == 0 and GAME[j][i] != 0:
                GAME[j + 1][i], GAME[j][i] = GAME[j][i], GAME[j + 1][i]
                flag[i] = 1
    add_num()
    display()


def up():
    global score, GAME
    flag = [0] * 3
    for i in range(0, 3):
        for j in reversed(range(1, 3)):
            if GAME[j - 1][i] == 0 and GAME[j][i] != 0:
                GAME[j - 1][i], GAME[j][i] = GAME[j][i], GAME[j - 1][i]
                flag[i] = 1
            elif GAME[j - 1][i] == GAME[j][i] and GAME[j][i] != 0 and flag[i] != 2:
                flag[i] = 2
                if GAME[j - 2][i] == GAME[j - 1][i]:
                    GAME[j - 2][i] *= 2
                    GAME[j - 1][i] = 0
                    GAME[j - 1][i], GAME[j][i] = GAME[j][i], GAME[j - 1][i]
                    score += GAME[j - 2][i]
                else:
                    GAME[j][i] = 0
                    GAME[j - 1][i] *= 2
                    score += GAME[j - 1][i]
    for i in range(0, 3):
        for j in reversed(range(1, 3)):
            if GAME[j - 1][i] == 0 and GAME[j][i] != 0:
                GAME[j - 1][i], GAME[j][i] = GAME[j][i], GAME[j - 1][i]
                flag[i] = 1
    add_num()
    display()


def left():
    global  score, GAME
    flag = [0] * 3
    for i in range(0, 3):
        for j in reversed(range(1, 3)):
            if GAME[i][j - 1] == 0 and GAME[i][j] != 0:
                GAME[i][j - 1], GAME[i][j] = GAME[i][j], GAME[i][j - 1]
                flag[i] = 1
            elif GAME[i][j - 1] == GAME[i][j] and GAME[i][j] != 0 and flag[i] != 2:
                flag[i] = 2
                if GAME[i][j - 2] == GAME[i][j - 1]:
                    GAME[i][j - 2] *= 2
                    GAME[i][j - 1] = 0
                    GAME[i][j - 1], GAME[i][j] = GAME[i][j], GAME[i][j - 1]
                    score += GAME[i][j - 2]
                else:
                    GAME[i][j] = 0
                    GAME[i][j - 1] *= 2
                    score += GAME[i][j - 1]
    for i in range(0, 3):
        for j in reversed(range(1, 3)):
            if GAME[i][j - 1] == 0 and GAME[i][j] != 0:
                GAME[i][j - 1], GAME[i][j] = GAME[i][j], GAME[i][j - 1]
                flag[i] = 1
    add_num()
    display()


def right():
    global  score, GAME
    flag = [0] * 3
    for i in range(0, 3):
        for j in range(0, 2):
            if GAME[i][j + 1] == 0 and GAME[i][j] != 0:
                GAME[i][j + 1], GAME[i][j] = GAME[i][j], GAME[i][j + 1]
                flag[i] = 1
            elif GAME[i][j + 1] == GAME[i][j] and GAME[i][j] != 0 and flag[i] != 2:
                flag[i] = 2
                if j == 0 and GAME[i][j + 2] == GAME[i][j + 1]:
                    GAME[i][j + 2] *= 2
                    GAME[i][j + 1] = 0
                    GAME[i][j + 1], GAME[i][j] = GAME[i][j], GAME[i][j + 1]
                    score += GAME[i][j + 2]
                else:
                    GAME[i][j] = 0
                    GAME[i][j + 1] *= 2
                    score += GAME[i][j + 1]
    for i in range(0, 3):
        for j in range(0, 2):
            if GAME[i][j + 1] == 0 and GAME[i][j] != 0:
                GAME[i][j + 1], GAME[i][j] = GAME[i][j], GAME[i][j + 1]
                flag[i] = 1
    add_num()
    display()


# end of controls


def rules():
    print( '''******************************************************************************************************************
                                              RULES OF THE GAME 256
    OBJECTIVE:-The game's objective is to slide numbered tiles on a grid to combine them to create a tile with 
             the number 256
    CONTROLS:-'w' for 'up'
              's' for 'down' 
              'a' for 'left' 
              'd' for 'right' 
              'q' for 'quit'  
    DESCRIPTION:- 256 is a game played on a 3X3 grid with numbered tiles that slide when a player moves them 
     using the four control keys. Every turn, a new tile will randomly appear in an empty spot on the board with
     a value of either 2 or 4. Tiles slide as far as possible in the chosen direction until they are stopped by 
     either another tile or the edge of the grid. If two tiles of the same number collide while moving, they 
     will merge into a tile with the total value of the two tiles that collided. The resulting tile cannot merge
     with another tile again in the same move.The user's score starts at zero, and is incremented whenever two 
     tiles combine,by the value of the new tile.The game is won when a tile with a value of 256 appears on the 
     board, hence the name of the game.When the player has no legal moves (there are no empty spaces and no 
     adjacent tiles with the same value), the game ends.

******************************************************************************************************************
     ''')


# code for checking exit conditions

def exit_conditions(GAME):
    # quit if q key is pressed
    if user_input == "q":
        print ("exit from game.....")
        display_score()
        out()
        exit()

    # quit if 256 tile occurs
    for p in range(3):
        for q in range(3):
            if GAME[p][q] == 256:
                print ("you win!!!!!!")
                display_score()
                out()
                exit()

    # quit if all tiles filled
    flag = 0
    for p in range(3):
        for q in range(3):
            if GAME[p][q] != 0:
                flag = flag + 1
    if flag == 9:
        print ("no more moves \n you lose .....")
        display_score()
        out()
        exit()


# for adding new tile
def add_num(GAME):
    global flag_new
    if flag_new[0] >= 1 or flag_new[1] >= 1 or flag_new[2] >= 1:
        index_0 = random.choice(random_index)
        index_1 = random.choice(random_index)
        while GAME[index_0][index_1] != 0:
            index_0 = random.choice(random_index)
            index_1 = random.choice(random_index)
        GAME[index_0][index_1] = random.choice(random_numbers)


def display_score():
    # to get highest tile
    global highest_tile
    for xx in range(3):
        for y in range(3):
            if GAME[xx][y] > highest_tile:
                highest_tile = GAME[xx][y]
    print ("highest tile in the game \t" + str(highest_tile))
    print ("your score" + str(score))
    global player_name
    player_name = input("\n ENTER THE NAME..")
    points()


# we will be using sql here by importing sqlite3 module
def points():
    # to connect to database
    connection = sqlite3.connect("points.db")

    # cursor
    crsr = connection.cursor()

    # SQL command to insert data
    now = datetime.datetime.now()
    date = now.strftime("%Y-%m-%d %H:%M")
    sql_cmd = "INSERT INTO score VALUES ('" + player_name + "', '" + str(score) + "' , '" + str(
        highest_tile) + "' , '" + date + "')"
    crsr.execute(sql_cmd)

    # to save changes in the file
    connection.commit()

    # to close connection
    connection.close()


# to display all points from table

def display_points():
    # to connect to database
    connection = sqlite3.connect("points.db")

    # cursor
    crsr1 = connection.cursor()

    # SQL command to insert data
    sql_cmd = "SELECT * FROM score"
    crsr1.execute(sql_cmd)

    # store all the fetched data in the ans variable
    ans = crsr1.fetchall()

    widths = []
    columns = []
    tavnit = '|'
    separator = '+'

    for cd in crsr1.description:
        widths.append(max(cd[2], len(cd[0])))
        columns.append(cd[0])

    for w in widths:
        tavnit += " %-" + "%ss |" % (w,)
        separator += '-' * w + '--+'

    print(separator)
    print(tavnit % tuple(columns))
    print(separator)
    for row in ans:
        print(tavnit % row)
    print(separator)

    # to close connection
    connection.close()


def delete():
    # to connect to database
    connection = sqlite3.connect("points.db")

    # cursor
    crsr = connection.cursor()

    # SQL command to clear table
    sql_cmd = "DROP TABLE score "
    crsr.execute(sql_cmd)

    # to save changes in the file
    connection.commit()

    # to close connection
    connection.close()

    # to recreate table
    database()


def database():
    # to connect to database use only to modify structure of table
    connection = sqlite3.connect("points.db")

    # cursor
    crsr2 = connection.cursor()

    # SQL command to create table
    sql_cmd = "CREATE TABLE score (player_name VARCHAR(30),score INTEGER, highest_tile INTEGER , date_and_time____ VARCHAR(20))"
    crsr2.execute(sql_cmd)

    # to save changes in the file
    connection.commit()

    # to close connection
    connection.close()


# end of sql


# this is the main code for running the game

# database()  # call this if you are using this first time
print(
    "******************************************< WELCOME TO 256>******************************************************\n")
input_play = input(" \n'b' to 'begin \n'r' for 'rules' \n'p' for 'points table' \n'q' for 'quit' \n ")
if input_play == 'b':
    # automatic initilization
    display_game()
elif input_play == 'q':
    print("quitting")
    exit()
elif input_play == "r":
    rules()
elif input_play == 'p':
    print( "POINTS TABLE")
    display_points()
    chara = raw_input("\n want to delete all scores??? \n press 'd' to 'delete' and any other key to exit")
    if chara == 'd':
        delete()
        print("all scores are reset")
    else:
        exit()

else:
    print(" invalid choice ")
