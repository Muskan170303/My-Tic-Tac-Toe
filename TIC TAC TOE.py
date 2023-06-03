import turtle as t
import random
def grid_prep():
    t.screensize(500,500)
    t.showturtle()
    t.pensize(5)
    t.penup()
    t.goto(0,200)
    t.color("Maroon")
    t.write("TIC-TAC-TOE GAME",align='center',font=('Algerian',40,'bold'))
    t.goto(0,150)
    t.color("Purple")
    t.write("Using Python",align='center',font=('Comic sans MS',20,'bold'))
    t.penup()
    t.color("Black")
    t.goto(-150,0)
    t.pendown()
    t.forward(300)
    t.penup()
    t.goto(-150,-100)
    t.pendown()
    t.forward(300)
    t.penup()
    t.right(90)
    t.goto(-50,100)
    t.pendown()
    t.forward(300)
    t.penup()
    t.goto(50,100)
    t.pendown()
    t.forward(300)
    t.hideturtle()
    t.penup()
    t.color("Cyan")
    t.goto(-135,70)
    t.write("1",align='center',font=('Comic sans MS',15,'bold'))
    t.goto(-35,70)
    t.write("2",align='center',font=('Comic sans MS',15,'bold'))
    t.goto(65,70)
    t.write("3",align='center',font=('Comic sans MS',15,'bold'))
    t.goto(-135,-30)
    t.write("4",align='center',font=('Comic sans MS',15,'bold'))
    t.goto(-35,-30)
    t.write("5",align='center',font=('Comic sans MS',15,'bold'))
    t.goto(65,-30)
    t.write("6",align='center',font=('Comic sans MS',15,'bold'))
    t.goto(-135,-130)
    t.write("7",align='center',font=('Comic sans MS',15,'bold'))
    t.goto(-35,-130)
    t.write("8",align='center',font=('Comic sans MS',15,'bold'))
    t.goto(65,-130)
    t.write("9",align='center',font=('Comic sans MS',15,'bold'))
    t.color("Black")

def player_name1():
    global p1
    global p2
    global d
    global keys
    d={input("Your name:"):0,"COMPUTER":0}
    keys=list(d)
    p1=keys[0]
    p2=keys[1]

def player_name2():
    global p1
    global p2
    global d
    global keys
    d={input("Player 1st name : "):0,input("Player 2nd name : "):0}
    keys=list(d)
    p1=keys[0]
    p2=keys[1]
    
def character():
    print(p1,", Which character would you like X or O : ")
    global cp1,cp2
    cp1=input()
    if(cp1=="X" or cp1=="x"):
        cp1="X"
        cp2="O"
    elif(cp1=="O" or cp1=="o"):
        cp1="O"
        cp2="X"
    else:
        print("Invalid Selection!! - Try Again")
        character()
    print("--------------------------------------------")
    print("%s : %c | %s : %c"%(p1,cp1,p2,cp2))
    print("--------------------------------------------\n")
    
def score():
    print("***************SCORE BOARD*******************")
    print("--------------------------------------------")
    print("%s\t\t%d"%(keys[0],d[keys[0]]))
    print("%s\t%d"%(keys[1],d[keys[1]]))
    print("--------------------------------------------\n")
    
def winner_select():
    if(i>=4):
        if(l[1]==l[5]==l[9]!=""):
            print("**************CONGRATULATIONS***************")
            t.penup()
            t.pensize(8)
            t.color("Black")
            t.goto(-150,100)
            t.pendown()
            t.goto(150,-200)
            t.penup()
            if(l[1]==cp1):
                print(p1," WON!!")
                print("--------------------------------------------\n")
                d[p1]=d[p1]+1
                return(True)
            else:
                print(p2," WON!!")
                print("--------------------------------------------\n")
                d[p2]=d[p2]+1
                return(True)
        elif(l[3]==l[5]==l[7]!=""):
            print("**************CONGRATULATIONS***************")
            t.penup()
            t.pensize(8)
            t.color("Black")
            t.goto(-150,-200)
            t.pendown()
            t.goto(150,100)
            t.penup()
            if(l[3]==cp1):
                print(p1," WON!!")
                print("--------------------------------------------\n")
                d[p1]=d[p1]+1
                return(True)
            else:
                print(p2," WON!!")
                print("--------------------------------------------\n")
                d[p2]=d[p2]+1
                return(True)
        elif(l[1]==l[2]==l[3]!=""):
            print("**************CONGRATULATIONS***************")
            t.penup()
            t.pensize(8)
            t.color("Black")
            t.goto(-150,50)
            t.pendown()
            t.goto(150,50)
            t.penup()
            if(l[1]==cp1):
                print(p1," WON!!")
                print("--------------------------------------------\n")
                d[p1]=d[p1]+1
                return(True)
            else:
                print(p2," WON!!")
                print("--------------------------------------------\n")
                d[p2]=d[p2]+1
                return(True)
        elif(l[4]==l[5]==l[6]!=""):
            print("**************CONGRATULATIONS***************")
            t.penup()
            t.pensize(8)
            t.color("Black")
            t.goto(-150,-50)
            t.pendown()
            t.goto(150,-50)
            t.penup()
            if(l[4]==cp1):
                print(p1," WON!!")
                print("--------------------------------------------\n")
                d[p1]=d[p1]+1
                return(True)
            else:
                print(p2," WON!!")
                print("--------------------------------------------\n")
                d[p2]=d[p2]+1
                return(True)
        elif(l[7]==l[8]==l[9]!=""):
            print("**************CONGRATULATIONS***************")
            t.penup()
            t.pensize(8)
            t.color("Black")
            t.goto(-150,-150)
            t.pendown()
            t.goto(150,-150)
            t.penup()
            if(l[7]==cp1):
                print(p1," WON!!")
                print("--------------------------------------------\n")
                d[p1]=d[p1]+1
                return(True)
            else:
                print(p2," WON!!")
                print("--------------------------------------------\n")
                d[p2]=d[p2]+1
                return(True)
        elif(l[1]==l[4]==l[7]!=""):
            print("**************CONGRATULATIONS***************")
            t.penup()
            t.pensize(8)
            t.color("Black")
            t.goto(-100,100)
            t.pendown()
            t.goto(-100,-200)
            t.penup()
            if(l[1]==cp1):
                print(p1," WON!!")
                print("--------------------------------------------\n")
                d[p1]=d[p1]+1
                return(True)
            else:
                print(p2," WON!!")
                print("--------------------------------------------\n")
                d[p2]=d[p2]+1
                return(True)
        elif(l[2]==l[5]==l[8]!=""):
            print("**************CONGRATULATIONS***************")
            t.penup()
            t.pensize(8)
            t.color("Black")
            t.goto(0,100)
            t.pendown()
            t.goto(0,-200)
            t.penup()
            if(l[2]==cp1):
                print(p1," WON!!")
                print("--------------------------------------------\n")
                d[p1]=d[p1]+1
                return(True)
            else:
                print(p2," WON!!")
                print("--------------------------------------------\n")
                d[p2]=d[p2]+1
                return(True)
        elif(l[3]==l[6]==l[9]!=""):
            print("**************CONGRATULATIONS***************")
            t.penup()
            t.pensize(8)
            t.color("Black")
            t.goto(100,100)
            t.pendown()
            t.goto(100,-200)
            t.penup()
            if(l[3]==cp1):
                print(p1," WON!!")
                print("--------------------------------------------\n")
                d[p1]=d[p1]+1
                return(True)
            else:
                print(p2," WON!!")
                print("--------------------------------------------\n")
                d[p2]=d[p2]+1
                return(True)
        elif(i==8):
            print("It's a Tie")
            print("--------------------------------------------\n")
            return(True)
        else:
            return(False)

def entering1():
    a=True
    while(a):
        r=random.randint(1,9)
        if(l[r]==""):
            print("Computer Chooses :",r)
            l.update({r:ch})
            a=False
            print("--------------------------------------------")
    return(r)

def entering2():
    a=True
    while(a):
        r=int(input("Enter the position you want to enter(1 to 9) :"))
        if(r>=1 and r<=9):
            if(l[r]==""):
                l.update({r:ch})
                a=False
                print("--------------------------------------------")
            else:
                print("Already Occupied!! - Try Again..")
        else:
            print("Invalid Choice!! - Try Again")
    return(r)

def turn(i):
    global ch
    if(i%2==0):
        ch=cp1
        print("--------------------------------------------")
        print(p1,"'s Turn : ")
        return(entering2())
    else:
        ch=cp2
        print("--------------------------------------------")
        print(p2,"'s Turn : ")
        if(z==2):
            return(entering2())
        else:
            return(entering1())
    
def game():
    print("--------------------------------------------")
    print("                GAME STARTS                 ")
    print("--------------------------------------------\n")
    global i
    for i in range(9):
        x=turn(i)
        if(x==1):
            t.goto(-100,-10)
            if(ch=="X"):
                t.color("Red")
            else:
                t.color("Blue")
            t.write(ch,align='center',font=('Comic sans MS',70,'bold'))
            val=winner_select()
            if(val==True):
                break
        elif(x==2):
            t.goto(0,-10)
            if(ch=="X"):
                t.color("Red")
            else:
                t.color("Blue")
            t.write(ch,align='center',font=('Comic sans MS',70,'bold'))
            val=winner_select()
            if(val==True):
                break
        elif(x==3):
            t.goto(100,-10)
            if(ch=="X"):
                t.color("Red")
            else:
                t.color("Blue")
            t.write(ch,align='center',font=('Comic sans MS',70,'bold'))
            val=winner_select()
            if(val==True):
                break
        elif(x==4):
            t.goto(-100,-115)
            if(ch=="X"):
                t.color("Red")
            else:
                t.color("Blue")
            t.write(ch,align='center',font=('Comic sans MS',70,'bold'))
            val=winner_select()
            if(val==True):
                break
        elif(x==5):
            t.goto(0,-115)
            if(ch=="X"):
                t.color("Red")
            else:
                t.color("Blue")
            t.write(ch,align='center',font=('Comic sans MS',70,'bold'))
            val=winner_select()
            if(val==True):
                break
        elif(x==6):
            t.goto(100,-115)
            if(ch=="X"):
                t.color("Red")
            else:
                t.color("Blue")
            t.write(ch,align='center',font=('Comic sans MS',70,'bold'))
            val=winner_select()
            if(val==True):
                break
        elif(x==7):
            t.goto(-100,-215)
            if(ch=="X"):
                t.color("Red")
            else:
                t.color("Blue")
            t.write(ch,align='center',font=('Comic sans MS',70,'bold'))
            val=winner_select()
            if(val==True):
                break
        elif(x==8):
            t.goto(0,-215)
            if(ch=="X"):
                t.color("Red")
            else:
                t.color("Blue")
            t.write(ch,align='center',font=('Comic sans MS',70,'bold'))
            val=winner_select()
            if(val==True):
                break
        elif(x==9):
            t.goto(100,-215)
            if(ch=="X"):
                t.color("Red")
            else:
                t.color("Blue")
            t.write(ch,align='center',font=('Comic sans MS',70,'bold'))
            val=winner_select()
            if(val==True):
                break
    score()
    if(z==1):
        exit1()
    else:
        exit2()

def exit1():
    yorn=input("Do you want to play again or not(Y or N): ")
    if(yorn=="Y" or yorn=="y"):
        t.reset()
        t.color("Black")
        grid_prep()
        global p1
        global p2
        for i in range(1,10):
            l.update({i:""})
        game()
    elif(yorn=="N" or yorn=="n"):
        print("Thanks for playing..")
    else:
        print("Invalid Choice!! - Try Again..")
        exit()     
    
def exit2():
    yorn=input("Do you want to play again or not(Y or N): ")
    if(yorn=="Y" or yorn=="y"):
        print("\n")
        t.reset()
        t.color("Black")
        grid_prep()
        global p1
        global p2
        for i in range(1,10):
            l.update({i:""})
        p1,p2=p2,p1
        character()
        game()
    elif(yorn=="N" or yorn=="n"):
        print("Thanks For Playing..")
    else:
        print("Invalid Choice!! - Try Again..")
        exit()

def choice():
    choice=input()
    return(choice)
    
l={1:"",2:"",3:"",4:"",5:"",6:"",7:"",8:"",9:""}
grid_prep()
print("Do You want to play single player or double player (S OR D):")
global z
c=choice()
if(c=="S" or c=="s"):
    z=1
    player_name1()
elif(c=="D" or c=="d"):
    z=2
    player_name2()
else:
    print("Invalid Choice!! - Try again..")
    choice()
character()
game()




        
