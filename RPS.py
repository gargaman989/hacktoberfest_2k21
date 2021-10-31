import random
def validate(hand):
    if ((hand<0)or(hand>2)):
        return False
    else:
        return True

def print_hand(hand, name):
    hands = ['Rock', 'Paper', 'Scissors']
    print(name + ' picked: ' + hands[hand])

def judge(player,computer):
    if player==computer:
        return "Draw"
    elif ((player==0 and computer==1)or(player==1 and computer==2)or(player==2 and computer==0)):
        return 'Lose'
    else:
        return 'Win'
    

print('Starting the Rock Paper Scissors game!')
x=0
while(x!=1):
    player_name = input('\nPlease enter your name: ')
    print('Pick a hand: (0: Rock, 1: Paper, 2: Scissors)')
    try:
        player_hand = int(input('Please enter a number (0-2): '))
    except:
        print("Invalid Invalid Invalid use only 0 ,1 0r 2")
        y=0
        while(y!=1):
             choice=input("Would you like to continue (y:n):")
             if choice=='n':
                 x=1
                 y=1
             elif choice=='y':
                 y=1
             else:
                 print('Enter Valid Choice')
        continue

    if validate(player_hand) is True:
        computer_hand = random.randint(0,2)
        print_hand(player_hand, player_name)
        print_hand(computer_hand, 'Computer')
        result=judge(player_hand,computer_hand)
        print(result)
    else:
        print("Please enter a valid number")

    y=0
    while(y!=1):
        choice=input("Would you like to continue (y:n):")
        if choice=='n':
            x=1
            y=1
        elif choice=='y':
            y=1
        else:
            print('Enter Valid Choice')
