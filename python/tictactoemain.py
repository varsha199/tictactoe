def ready_to_play():
    ready = input("Are you ready to play? Enter Yes or No: ")
    if ready == "Yes" or ready == "yes":
        return True
    elif ready == "No":
        return False
    else:
        print("Invalid input")
        ready_to_play()


first_player_name=""
first_player_symbol=''
second_player_name=""
second_player_symbol=''


def get_player_symbol():
    s= input("Enter your symbol as x or o (Enter e to exit) : ")
    if s=='o' or s=='O' or s=='x' or s=='X':
        return s
    elif s=='e':
        return
    else:
        print("Invalid value. Try again!")
        get_player_symbol()

def get_second_player_symbol(s1):
    if s1 == 'x':
        return 'o'
    elif s1 =='X':
        return 'O'
    elif s1=='O':
        return 'X'
    else:
        return 'x'
    
def get_player_details():
    global first_player_name
    first_player_name= input("Enter First Player Name: ")
    global first_player_symbol
    first_player_symbol= get_player_symbol()
    global second_player_name
    second_player_name= input("Enter Second Player Name: ")
    global second_player_symbol
    second_player_symbol= get_second_player_symbol(first_player_symbol)
    print(second_player_name+" your symbol is: "+second_player_symbol)
    

list_of_positions = [['','',''],
                     ['','',''],
                     ['','','']]

def get_position(playername, playersymbol):
    position = int(input(playername + " enter your position in range of 1-9: "))
    global list_of_positions
    if list_of_positions[position-1]=='':
        list_of_positions[position-1]=playersymbol
    else:
        print("This position is alrady taken. Please try again")
        get_position(playername,playersymbol)
    
def printcurrentpositions():
    global list_of_positions
    print(list_of_positions[0] +"   | "+ list_of_positions[1] +"   | "+list_of_positions[2])
    print("----------------")
    print(list_of_positions[3] +"   | "+ list_of_positions[4] +"   | "+list_of_positions[5])
    print("----------------")
    print(list_of_positions[6] +"   | "+ list_of_positions[7] +"   | "+list_of_positions[8])

def start_the_game():
    print("Starting the game ....")
    print("Lets play ....ready, steady go")
    for x in range(0,9):
        if x%2==0:
            get_position(first_player_name, first_player_symbol)
        else:
            get_position(second_player_name, second_player_symbol)
        printcurrentpositions()


def check_result():
    if list_of_positions[0]==list_of_positions[4] == list_of_positions[9]:
        return list_of_positions[0]
    if list_of_positions[2]==list_of_positions[4] == list_of_positions[6]:
        return list_of_positions[2]
    
 

if(ready_to_play()):
    get_player_details()
    start_the_game()
else:
    print("Exiting the game")
