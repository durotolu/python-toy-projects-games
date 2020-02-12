import random

#file i/o for historical results
def load_results():
    text_file = open("src/history.txt", "r")
    history = text_file.read().split(",")
    text_file.close()
    return history

def save_results( w, t, l ):
    text_file = open("src/history.txt", "w")
    text_file.write( str(w) + "," + str(t) + "," + str(l) )

#welcome message
results = load_results()
wins = int(results[0])
ties = int(results[1])
losses = int(results[2])
print("Welcome to the Rock, Paper, Scissors game!")
print(F"Wins: {wins}, Ties: {ties}, Losses: {losses}")
print("Choose to continue...")

#getting computer and user choices
computer = random.randint(1, 3)
user = int(input("[1] Rock  [2] Paper  [3] Scissors  [0] Quit\n"))

#gameplay loop
while not user == 0:
    #user chooses rock
    if user == 1:
        if computer == 1:
            print("Computer chose rock... tie!")
            ties += 1
        elif computer == 2:
            print("Computer chose paper... computer wins :(")
            losses += 1
        else:
            print("Computer chose scissors... you win :)")
            wins += 1
    #user chooses paper
    elif user == 2:
        if computer == 1:
            print("Computer chose rock... you win :)")
            wins += 1
        elif computer == 2:
            print("Computer chose paper... tie!")
            ties += 1
        else:
            print("Computer chose scissors... computer wins :(")
            losses += 1
    #user chooses scissors
    elif user == 3:
        if computer == 1:
            print("Computer chose rock... computer wins :(")
            losses += 1
        elif computer == 2:
            print("Computer chose paper... you win :)")
            wins += 1
        else:
            print("Computer chose scissors... tie!")
            ties += 1
    #user inputs some undefined selection
    else:
        print("invalid selection, try again from the options provided")

    print(F"Wins: {wins}, Ties: {ties}, Losses: {losses}")

    print("Choose to continue...")
    computer = random.randint(1, 3)
    user = int((input("[1] Rock  [2] Paper  [3] Scissors  [0] Quit\n")))

save_results(wins, ties, losses)
print("You decided to quit game ;-(\nresults at end of game:")
print(F"Wins: {wins}, Ties: {ties}, Losses: {losses}")