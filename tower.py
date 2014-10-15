# basicTower.py
# Towers of Hanoi game with a shoddy GUI. You can pick 
# the amount of levels up to nine.
# By: Ryan Miller


def movePt1(a,b,game,level):
    zero = 0
    mover = 0
    if game[a][level-1] == 1:
        zero = level-1
        mover = 1
    else:
        for i in range(level):
            if game[a][i] == 0:
                if i == 0:
                    print("There's nothing to move...")
                mover = game[a][i-1]
                zero = i-1
                break
    for j in range(level):
        if game[b][j] == 0:
            if game[b][j-1] > mover:
                game[b][j] = mover
                game[a][zero] = 0
                break
            elif j == 0:
                game[b][j] = mover
                game[a][zero] = 0
                break
            else:
                print("Invalid move.")
                break
    return game

def solvedYet(game,level):
    if game[2][level-1] == 1:
        return True
    else:
        return False

def letsSee(game,level):
    print("           ")
    print("1------2------3")
    print("           ")
    for i in range(level):
        s = [0,0,0]
        if game[0][level-i-1] == 0:
            s[0] = " "
        else:
            s[0] = game[0][level-i-1]
        if game[1][level-i-1] == 0:
            s[1] = " "
        else:
            s[1] = game[1][level-i-1]
        if game[2][level-i-1] == 0:
            s[2] = " "
        else:
            s[2] = game[2][level-i-1]
        print(s[0],"    ",s[1],"    ",s[2])
        # Alternate method below shows zeros instead of blank spaces and is compact
        # print((game[0][level-i-1],"    ",game[1][level-i-1],"    ",game[2][level-i-1])) 


def main():
    q = False
    while q == False:
        level = eval(input("How many levels do you think you can handle? (2-9): "))
        if level > 1 and level < 11:
            q = True
        else:
            print("Come on... that's ridiculous.")
    solved = False
    pile1 = [0] * level
    for k in range(level):
        pile1[k] = level - k
    pile2 = [0] * level
    pile3 = [0] * level
    game = [pile1,pile2,pile3]
    letsSee(game,level)
    y = 0
    while solved == False:
        y += 1
        butt = False
        while butt == False:
            try:
                a,b = eval(input("Move: "))-1,eval(input("To: "))-1
                butt = True
            except Exception:
                print("Put in some legit numbers")
                letsSee(game,level)
            
        if (a < 4 and a > -1 and b < 4 and b > -1):
            game = movePt1(a, b, game, level)
            solved = solvedYet(game,level)
            letsSee(game, level)
        else:
            print("Please enter valid numbers.")
    print("Nice one, you did it!")
    if y > ((2 * level) - 1):
        print("It only took", y, "moves! You could've done it in", ((2 ** level) - 1), ", though.")
    else:
        print("Woah! You did it in the fewest moves possible, ", y, "!")
    again = input("Do you want to try another? ")
    if again == "yes":
        main()

main()
