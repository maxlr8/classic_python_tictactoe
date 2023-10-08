import random

from IPython.display import clear_output

clear_output()
#Main Code

def decision(p1, p2):

    result = ''
    count = 0
    board = [' ']*9
    positions = [1,2,3,4,5,6,7,8,9]
    register = []*20
    t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13,t14 = 0,0,0,0,0,0,0,0,0,0,0,0,0,0

    #Positions on the board

    print("\n               Positions of the board\n") 
    print(' '+' | '+' '+' | '+' '+'            '+'1'+' | '+'2'+' | '+'3')
    print('--|---|--'+'            '+'--|---|--') 
    print(' '+' | '+' '+' | '+' '+'            '+'4'+' | '+'5'+' | '+'6')
    print('--|---|--'+'            '+'--|---|--')
    print(' '+' | '+' '+' | '+' '+'            '+'7'+' | '+'8'+' | '+'9\n')

    if p1 == 'X':
        while count < 9:
            if count % 2 == 0:
                try:
                    place = int(input("Player1 - Where do you want to mark 'X': "))
                except ValueError:
                    print("Please enter a valid position between positions 1 - 9\n")
                    t1 += 1
                    if t1 >= 3:
                        print("Max invalid inputs exceeded - 3 times! Rerun..")
                        result = ''
                        break
                    continue

                if int(place) not in positions:
                    print("Please enter a valid position")
                    t2 += 1
                    if t2 >= 3:
                        print("Max invalid positions exceeded - 3 times! Rerun..")
                        result = ''
                        break
                else:
                    if place in register:
                        print("Position already filled. Please enter a different position")
                        t3 += 1
                        if t3 >= 3:
                            print("Max invalid positions exceeded - 3 times! Rerun..")
                            result = ''
                            break
                    elif place not in register:
                        val, result = disp(place,'X','p1',board)
                        register.append(place)
                        count += 1
                        if result == True and val == 'X':
                            print("'X' - Player 1 wins!")
                            break
                        elif count == 8:
                            print("Match Draw!")
                            result = 'invalid'
                            break

            elif count % 2 != 0:
                try:
                    place = int(input("Player2 - Where do you want to mark 'O': "))
                except ValueError:    
                    print("Please enter a valid position between positions 1 - 9\n")
                    t4 += 1
                    if t4 >= 3:
                        print("Max invalid positions exceeded - 3 times! Rerun..")
                        result = ''
                        break
                    continue

                if int(place) not in positions:
                    print("Please enter a valid position")
                    t5 += 1
                    if t5 >= 3:
                        print("Max invalid positions exceeded - 3 times! Rerun..")
                        result = ''
                        break
                else:
                    if place in register:
                        print("Position already filled. Please enter a different position")
                        t6 += 1
                        if t6 >= 3:
                            print("Max invalid positions exceeded - 3 times! Rerun..")
                            result = ''
                            break

                    elif place not in register:
                        val, result = disp(place,'O','p2',board)
                        register.append(place)
                        count += 1
                        if result == True and val == 'O':
                            print("'O' - Player 2 wins!")
                            break            
                        elif count == 8:
                            print("Match Draw!")
                            result = 'invalid'
                            break

    if p1 == 'O':
        while count < 9:

            if count % 2 == 0:
                try:
                    place = int(input("Player1 - Where do you want to mark 'O': "))
                except ValueError:
                    print("Please enter a valid position between positions 1 - 9\n")
                    t7 += 1
                    if t7 >= 3:
                            print("Max invalid positions exceeded - 3 times! Rerun..")
                            result = ''
                            break
                    continue

                if int(place) not in positions:
                    print("Please enter a valid position")
                    t8 += 1
                    if t8 >= 3:
                            print("Max invalid positions exceeded - 3 times! Rerun..")
                            result = ''
                            break
                else:                                   
                    if place in register:
                        print("Position already filled. Please enter a different position")
                        t9 += 1
                        if t9 >= 3:
                            print("Max invalid positions exceeded - 3 times! Rerun..")
                            result = ''
                            break
                    
                    elif place not in register:
                        val, result = disp(place,'O','p1',board)
                        register.append(place)
                        count += 1
                        if result == True and val == 'O':
                            print("'O' - Player 1 wins!")
                            break
                        elif count == 8:
                            print("Match Draw!")
                            result = 'invalid'
                            break

            elif count % 2 != 0:
                try:
                    place = int(input("Player2 - Where do you want to mark 'X': "))
                except ValueError:    
                    print("Please enter a valid position between positions 1 - 9\n")
                    t10 += 1
                    if t10 >= 3:
                            print("Max invalid positions exceeded - 3 times! Rerun..")
                            result = ''
                            break
                    continue

                if int(place) not in positions:
                    print("Please enter a valid position")
                    t11 += 1
                    if t11 >= 3:
                            print("Max invalid positions exceeded - 3 times! Rerun..")
                            result = ''
                            break
                else:                                   
                    if place in register:
                        print("Position already filled. Please enter a different position")
                        t12 += 1
                        if t12 >= 3:
                            print("Max invalid positions exceeded - 3 times! Rerun..")
                            result = ''
                            break
                    
                    elif place not in register:
                        val, result = disp(place,'X','p2',board)
                        register.append(place)
                        count += 1
                        if result == True and val == 'X':
                            print("'X' - Player 2 wins!")
                            break
                        elif count == 8:
                            print("Match Draw!")
                            result = 'invalid'
                            break
                   
    while result == True or result == 'invalid' :
        
        try:    
            again = int(input("Do you want to play again? Press ['1' - for Yes] | ['2'- for No] : "));
            clear_output()
        except ValueError:
            print("Please enter '1' or '2' to proceed!")
            t13 += 1
            if t13 >= 3:
                print("Max invalid values exceeded - 3 times! Rerun..")
                break
            continue
        
        if int(again) not in [1,2]:
            print("Please enter '1' or '2' to proceed!")
            t14 += 1
            if t14 >= 3:
                print("Max invalid values exceeded - 3 times! Rerun..")
                break
        else:
            if int(again) == 1:
                print("Okay!\n")
                Player_Choice()
            elif int(again) == 2:
                print("\nThank you for playing!")
                break

# Display

def disp(place, value, player, board):

    if player == 'p1':
        clear_output()
        board[int(place)-1] = value 
        print("\n               Positions of the board")
        print(board[0]+' | '+board[1]+' | '+board[2]+'            '+'1'+' | '+'2'+' | '+'3')
        print('--|---|--'+'            '+'--|---|--')
        print(board[3]+' | '+board[4]+' | '+board[5]+'            '+'4'+' | '+'5'+' | '+'6')
        print('--|---|--'+'            '+'--|---|--')
        print(board[6]+' | '+board[7]+' | '+board[8]+'            '+'7'+' | '+'8'+' | '+'9')
        print('\n')
    
    if player == 'p2':
        clear_output()
        board[int(place)-1] = value 
        print("\n               Positions of the board")
        print(board[0]+' | '+board[1]+' | '+board[2]+'            '+'1'+' | '+'2'+' | '+'3')
        print('--|---|--'+'            '+'--|---|--')
        print(board[3]+' | '+board[4]+' | '+board[5]+'            '+'4'+' | '+'5'+' | '+'6')
        print('--|---|--'+'            '+'--|---|--')
        print(board[6]+' | '+board[7]+' | '+board[8]+'            '+'7'+' | '+'8'+' | '+'9')
        print('\n')
    
    if(board[0]==board[1]==board[2]=='X' or board[3]==board[4]==board[5]=='X' or
       board[6]==board[7]==board[8]=='X' or board[0]==board[3]==board[6]=='X' or
       board[1]==board[4]==board[7]=='X' or board[2]==board[5]==board[8]=='X' or
       board[0]==board[4]==board[8]=='X' or board[2]==board[4]==board[6]=='X'):
        return 'X',True
    elif(board[0]==board[1]==board[2]=='O' or board[3]==board[4]==board[5]=='O' or
       board[6]==board[7]==board[8]=='O' or board[0]==board[3]==board[6]=='O' or
       board[1]==board[4]==board[7]=='O' or board[2]==board[5]==board[8]=='O' or
       board[0]==board[4]==board[8]=='O' or board[2]==board[4]==board[6]=='O'):
        return 'O',True
    else:
        return '',''


# Player Choice

def Player_Choice():

    # Initials
    m1 = 0
    choice = ''

    print("Welcome to TIC-TAC-TOE!\n")
    while choice not in ['1','2']:

        choice = input("Do you want to choose b/w (1) X and O |or| (2) want it randomly assigned? Please choose between 1 or 2 \n")

        if choice not in ['1','2']:
            clear_output()
            print("Please choose between 1 or 2! Try again..")
            m1 += 1
            if (m1 > 3):
                clear_output()
                print("Max invalid inputs exceeded - 3 times! Rerun..")
                choice = ''
                break

        elif choice in ['1','2']:
            if choice == '1':

                chosen = '1'
                m2 = 1
                while chosen not in ['X','O','x','o']:

                    chosen = input("X or O \n")
                    X = 'X'
                    O = 'O'

                    if chosen.casefold() == X.casefold():
                        p1 = 'X'
                        p2 = 'O'
                        clear_output()
                        print("Player 1 - '{}'".format(p1))
                        print("Player 2 - '{}'".format(p2))
                        decision(p1,p2)

                    elif chosen.casefold() == O.casefold():
                        p1 = 'O'
                        p2 = 'X'
                        clear_output()
                        print("Player 1 - '{}'".format(p1))
                        print("Player 2 - '{}'".format(p2))
                        decision(p1,p2)

                    else:
                        clear_output()
                        print("Incorrect! Please choose only between X or O! Try again..")
                        chosen = '1'
                        m2 += 1
                        if (m2 > 3):
                            clear_output()
                            print("Max invalid inputs exceeded - 3 times! Rerun..")
                            break

            elif choice == '2':

                X_or_O = ['X','O']
                p1 = random.choice(X_or_O)
                p2 = ''

                if p1 == 'X':
                    p2 = 'O'

                elif p1 == 'O':
                    p2 = 'X'

                clear_output()
                print("Player 1 - '{}'".format(p1))
                print("Player 2 - '{}'".format(p2))
                decision(p1,p2)

Player_Choice()