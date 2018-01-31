from graphics import*

#Setting up the Window
win = GraphWin("Connect Four", 700, 700)
win.setBackground("Blue")
start = Text(Point(350, 325), "PRESS ANY KEY TO START THE GAME!")
instruction = Text(Point(350, 350), "Use the numberpad on your keyboard to place your chip in the desired column.")
instruction2 = Text(Point(350, 370), "To quit the game, please press q.")
start.draw(win)
instruction.draw(win)
instruction2.draw(win)                   
instruction.setSize(15)
instruction2.setSize(15)
instruction.setTextColor("white")
instruction2.setTextColor("white")
start.setSize(25)
start.setTextColor("white")
start.setStyle("bold")
K = win.getKey()
start.undraw()
instruction.undraw()
instruction2.undraw()

Heading = Text(Point(350, 30), "LET'S PLAY CONNECT FOUR!")
Heading.setSize(30)
Heading.setTextColor("white")
Heading.setStyle("bold")
Heading.draw(win)

#To tell whether it is Player 1's turn or Player's 2 turn
Player1 = Text(Point(350, 55), "Player 1, make your move!")
Player1.setSize(15)
Player1.setTextColor("white")
Player1.setStyle("bold")
Player2 = Text(Point(350, 55), "Player 2, make your move!")
Player2.setSize(15)
Player2.setTextColor("white")
Player2.setStyle("bold")
Player1.draw(win)

#Variables
boardstate = {}
pieces = {}
player = "yellow"
winner = "none"
x = 0

def main():
    DrawBoard()
    win = False
    while win == False or win == "none":
        Move()
        win = Winner()
        
def MakeRow(y, rows, i):
    while rows > i:
        for col in range(7):
            cp = Point(50 + 100*col, y)  
            circle = Circle(cp, 45)
            pieces[col + 1,  i + 1] = circle
            boardstate[col + 1,  i + 1] = "white"
            circle.setFill("white")
            circle.draw(win)

        i += 1
        y += 100
        MakeRow(y, rows, i)

def DrawBoard():
    MakeRow(125, 6, 0)

def DrawPiece(column, row, color):
    global player
    global x
    
    pieces[column, row].setFill(player)
    boardstate[column, row] = player
    if player == "yellow":
        x += 1
        Player1.undraw()
        Player2.draw(win)
        player = "red"
    else:
        player = "yellow"
        x += 1
        Player2.undraw()
        Player1.draw(win)

def MakeMove(column):
   for row in range(6, 0, -1):
        if boardstate[column, row] == "white":
            DrawPiece(column, row, player)
            break

#It takes a while for the first move to draw. Other than that, everything is fine.
def Move():
    if winner == "none":
        key = win.checkKey()
        if key in ("1", "2", "3", "4", "5", "6", "7"):
            MakeMove(int(key))
        elif key == "q":
            win.close()

def WinCheck(A, B, C, D):
    if (A == B) and (A == C) and (A == D) and A != "white":
        if A == "yellow":
            A = "Player 1"
        elif A == "red":
            A = "Player 2"
        return A
    else:
        return False
    
def Winner():
    global winner
    if winner == "none":
        for column in range(7, 0, -1):
            for row in range(3, 0, -1):
                c1 = boardstate[column, row]
                c2 = boardstate[column, row + 1]
                c3 = boardstate[column, row + 2]
                c4 = boardstate[column, row + 3]
                win = WinCheck(c1, c2, c3, c4)
                if win != False:
                    winwindow = GraphWin("WINNER", 400, 200)
                    Won = Text(Point(200, 100), win + " wins!")
                    Won.setSize(30)
                    Won.setStyle("bold")
                    Won.draw(winwindow)
                    return win
                    
        for row in range(6, 1, -1):
            for column in range(1, 4, 1):
                c1 = boardstate[column, row]
                c2 = boardstate[column + 1, row]
                c3 = boardstate[column + 2, row]
                c4 = boardstate[column + 3, row]
                win = WinCheck(c1, c2, c3, c4)
                if win != False:
                    winwindow = GraphWin("WINNER", 400, 200)
                    Won = Text(Point(200, 100), win + " wins!")
                    Won.setSize(30)
                    Won.setStyle("bold")
                    Won.draw(winwindow)
                    return win
                
        for row in range(6, 1, -1):
            for column in range(3, 1, -1):
                c1 = boardstate[column, row]
                c2 = boardstate[column + 1, row]
                c3 = boardstate[column + 2, row]
                c4 = boardstate[column + 3, row]
                win = WinCheck(c1, c2, c3, c4)
                if win != False:
                    winwindow = GraphWin("WINNER", 400, 200)
                    Won = Text(Point(200, 100), win + " wins!")
                    Won.setSize(30)
                    Won.setStyle("bold")
                    Won.draw(winwindow)
                    return win
                
        for row in range(3, 1, -1):
            for column in [1, 2, 3, 4]:
                c1 = boardstate[column, row]
                c2 = boardstate[column + 1, row + 1]
                c3 = boardstate[column + 2, row + 2]
                c4 = boardstate[column + 3, row + 3]
                win = WinCheck(c1, c2, c3, c4)
                if win != False:
                    winwindow = GraphWin("WINNER", 400, 200)
                    Won = Text(Point(200, 100), win + " wins!")
                    Won.setSize(30)
                    Won.setStyle("bold")
                    Won.draw(winwindow)
                    return win

        for row in range(3, 1, -1):
            for column in [7, 6, 5, 4]:
                c1 = boardstate[column, row]
                c2 = boardstate[column - 1, row + 1]
                c3 = boardstate[column - 2, row + 2]
                c4 = boardstate[column - 3, row + 3]
                win = WinCheck(c1, c2, c3, c4)
                if win != False:
                    winwindow = GraphWin("WINNER", 400, 200)
                    Won = Text(Point(200, 100), win + " wins!")
                    Won.setSize(30)
                    Won.setStyle("bold")
                    Won.draw(winwindow)
                    return win

    if x == 42:
        tiedwindow = GraphWin("TIED", 400, 200)
        Tied = Text(Point(200, 100), "YOU ARE TIED!")
        Tied.setSize(30)
        Tied.setStyle("bold")
        Tied.draw(tiedwindow)
        return win
    
    return False

main()
