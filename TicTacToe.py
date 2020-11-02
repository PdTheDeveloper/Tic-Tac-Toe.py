# Milestone: Tic Tac Toe
#from IPython.display import clear_output
import random

marksList = ["", "", "", "", "", "", "", "", ""]
currentMark = ""
position = 0


def drawTable():
    #clear_output()
    print(
        "     |     |     \n     |     |     \n{6:^5}|{7:^5}|{8:^5}\n     |     |     \n     |     |     \n------------------\n     |     |     \n     |     |     \n{3:^5}|{4:^5}|{5:^5}\n     |     |     \n     |     |     \n------------------\n     |     |     \n     |     |     \n{0:^5}|{1:^5}|{2:^5}\n     |     |     \n     |     |     ".format(
            marksList[0], marksList[1], marksList[2], marksList[3], marksList[4], marksList[5], marksList[6],
            marksList[7], marksList[8]))


def setMark(position):
    marksList[position - 1] = currentMark
    drawTable()
    fullCheck()


def nextPlayer():
    global currentMark
    if currentMark == "X":
        currentMark = "O"
    else:
        currentMark = "X"
    position = int(input("Please enter the position:"))
    setMark(position)


def isFull():
    for x in range(0, 9):
        if marksList[x] == "":
            return False
    return True


def playOrNot():
    choice = ''
    while choice != "Y" and choice != "N":
        choice = input("Do you want to play again? Enter Y for yes and N for no:")
    if choice == "Y":
        init()
    else:
        exit()


def fullCheck():
    if ((marksList[0] != "" and marksList[0] == marksList[1] == marksList[2]) or (
            marksList[3] != "" and marksList[3] == marksList[4] == marksList[5]) or (
            marksList[6] != "" and marksList[6] == marksList[7] == marksList[8]) or (
            marksList[0] != "" and marksList[0] == marksList[3] == marksList[6]) or (
            marksList[1] != "" and marksList[1] == marksList[4] == marksList[7]) or (
            marksList[2] != "" and marksList[2] == marksList[5] == marksList[8]) or (
            marksList[0] != "" and marksList[0] == marksList[8] == marksList[4]) or (
            marksList[2] != "" and marksList[6] == marksList[4] == marksList[2])):
        print("You win!")
        playOrNot()
    elif isFull():
        print("Tie!")
        playOrNot()
    else:
        nextPlayer()


def init():
    global marksList, currentMark
    marksList = ["", "", "", "", "", "", "", "", ""]
    currentMark = ""
    print(100*"\n")
    input("What do you want to be? X or O?")
    drawTable()
    rnd = random.randint(1, 2)
    if rnd == 2:
        currentMark = "X"
        print("Player 2 is playing first: O")
    else:
        currentMark = "O"
        print("Player 1 is playing first: X")
    nextPlayer()


init()



