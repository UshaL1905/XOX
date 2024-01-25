def block():
        print("-------------------------------------------------")
        print("|[0]             |[1]            |[2]           |")
        print("         ",b[0],"    |       ",b[1],"    |       ",b[2],"   |")
        print("|                |               |              |")
        print("-------------------------------------------------")
        print("|[3]             |[4]            |[5]           |")
        print("|        ",b[3],"    |       ",b[4],"    |       ",b[5],"   |")
        print("|                |               |              |")
        print("-------------------------------------------------")
        print("|[6]             |[7]            |[8]           |")
        print("|        ",b[6],"    |       ",b[7],"   |       ",b[8],"   |")
        print("|                |               |              |")
        print("-------------------------------------------------")
        
print(" HELLOOOOOOO WELCOME TO XOX....!!! ")
print(''' LET'S PLAY "XOX" ''')
u = input(" PLAYER_1 NAME : ")
v = input(" PLAYER_2 NAME : ")
print("             LET'S START          ")
print(u," IS GIVEN AS 'X'")
print(v," IS GIVEN AS 'O'")
b = [ '','','','','','','','','' ]
for i  in b :
        block()
        print(u," YOU CAN SELECT THE POSTION " )
        
        C = eval(input())
        if b[C] == 'X ':
            print(" THE BLOCK IS FILLED ")
            print(u," YOU CAN SELECT THE NEW POSTION " )
        if b[C] == 'O ' :
            print(v," HAS ALREADY ENTERED THAT POSITION")
            print(u," PLEASE ENTER NEW POSITION")
            C = eval(input())
            
        b[C] = 'X '


        
        if b[0] == b[1] == b[2]== 'X ':
                block()
                print(u,"IS WINNER....!!!!")
                print("CONGRATS", u)
                print("WINNER WINNER CHICKEN DINNER.....")
                print("___GAME OVER___")
                exit()
        elif b[1] == b[4] == b[7]== 'X ':
                block()
                print(u,"IS WINNER....!!!!")
                print("CONGRATS", u)
                print("WINNER WINNER CHICKEN DINNER.....")
                print("___GAME OVER___")
                exit()
        elif b[2] == b[5] == b[8]== 'X ':
                block()
                print(u,"IS WINNER....!!!!")
                print("CONGRATS", u)
                print("WINNER WINNER CHICKEN DINNER.....")
                print("___GAME OVER___")
                exit()
        elif b[0] == b[4] == b[8]== 'X ':
                block()
                print(u,"IS WINNER....!!!!")
                print("CONGRATS", u)
                print("WINNER WINNER CHICKEN DINNER.....")
                print("___GAME OVER___")
                exit()
        elif b[2] == b[4] == b[6]== 'X ':
                block()
                print(u,"IS WINNER....!!!!")
                print("CONGRATS", u)
                print("WINNER WINNER CHICKEN DINNER.....")
                print("___GAME OVER___")
                exit()
        elif b[3] == b[4] == b[5]== 'X ':
                block()
                print(u,"IS WINNER....!!!!")
                print("CONGRATS", u)
                print("WINNER WINNER CHICKEN DINNER.....")
                print("___GAME OVER___")
                exit()
        elif b[6] == b[7] == b[8]== 'X ':
                block()
                print(u,"IS WINNER....!!!!")
                print("CONGRATS", u)
                print("WINNER WINNER CHICKEN DINNER.....")
                print("___GAME OVER___")
                exit()
        elif b[0] == b[3] == b[6]== 'X ':
                block()
                print(u,"IS WINNER....!!!!")
                print("CONGRATS", u)
                print("WINNER WINNER CHICKEN DINNER.....")
                print("___GAME OVER___")
                exit()
        elif b[0] != '' and b[1] != '' and b[2] != '' and b[3] != '' and b[4] != '' and b[5] != '' and b[6] != '' and b[7] != '' and b[8] != '':
            print("MATCH DRAW!!!")
            print("PLEASE TRY AGAIN")
            block()
            exit()
        else:
                print("~~~~~~~~~~~~~~")
                                

          


        block()
        
        print(v," YOU CAN SELECT THE POSTION " )
        D = eval(input())
        if b[D] == 'O ':
            print(" THE BLOCK IS FILLED ")
            print(v," PLEASE ENTER THE NEW POSTION ") 
            D = eval(input())
        if b[D] == 'X ' :
            print(" THE BLOCK IS FILLED ")
            print(u," HAS ALREADY ENTERD THE POSTION" )
            print(v," PLEASE ENTER THE NEW POSTION")
            D = eval(input())
            b[D] = 'O '
                
        b[D] = 'O '


            
        
        if b[0] == b[1] == b[2]== 'O ':
            block()
            print(v," IS WINNER....!!!!!")
            print("CONGRATS", v)
            print("WINNER WINNER CHICKEN DINNER.....")
            print("___GAME OVER___")
            exit()
        
        elif b[1] == b[4] == b[7]== 'O ':
            block()
            print(v," IS WINNER....!!!!!")
            print("CONGRATS", v)
            print("WINNER WINNER CHICKEN DINNER.....")
            print("___GAME OVER___")
            exit()
        
        elif b[2] == b[5] == b[8]== 'O ':
            block()
            print(v," IS WINNER....!!!!!")
            print("CONGRATS", v)
            print("WINNER WINNER CHICKEN DINNER.....")
            print("___GAME OVER___")
            exit()
        
        elif b[0] == b[4] == b[8]== 'O ':
            block()
            print(v," IS WINNER....!!!!!")
            print("CONGRATS", v)
            print("WINNER WINNER CHICKEN DINNER.....")
            print("___GAME OVER___")
            exit()
        
        elif b[2] == b[4] == b[6]== 'O ':
            block()
            print(v," IS WINNER....!!!!!")
            print("CONGRATS", v)
            print("WINNER WINNER CHICKEN DINNER.....")
            print("___GAME OVER___")
            exit()
        
        elif b[3] == b[4] == b[5]== 'O ':
            block()
            print(v," IS WINNER....!!!!!")
            print("CONGRATS", v)
            print("WINNER WINNER CHICKEN DINNER.....")
            print("___GAME OVER___")
            exit()
        
        elif b[6] == b[7] == b[8]== 'O ':
            block()
            print(v," IS WINNER....!!!!!")
            print("CONGRATS", v)
            print("WINNER WINNER CHICKEN DINNER.....")
            print("___GAME OVER___")
            exit()
        
        elif b[0] == b[3] == b[6]== 'O ':
            block()
            print(v," IS WINNER....!!!!!")
            print("CONGRATS", v)
            print("WINNER WINNER CHICKEN DINNER.....")
            print("___GAME OVER___")
            exit()
        elif b[0] != '' and b[1] != '' and b[2] != '' and b[3] != '' and b[4] != '' and b[5] != '' and b[6] != '' and b[7] != '' and b[8] != '':
            print(" MATCH DRAW!!!")
            print("PLEASE TRY AGAIN")
            block()
            exit()
        
        else:
                print("~~~~~~~~~~~~~~")
