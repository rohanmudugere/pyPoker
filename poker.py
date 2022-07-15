def deal(deck):
    import random as r

    #generate 12 cards
    cards = []
    for i in range(0, 12):
        num = r.choice(list(deck))
        cards.append(deck.pop(num))
    return cards
    
def dispHand(first, second):
    print(f"\n  Your cards are: {first}, {second}")

def dispRiver(first, second, third):
    print(f"\n  The first three cards in the river are: {first}, {second}, {third}")

def dispNext(next):
    print(f"\n  The next card in the river is: {next}")

def option1(smBlind, balance):
    print(f"\n  You are the small blind.\n  Pot total: {smBlind * 3}")
    userChoice = input("  Would you like to CALL, RAISE, or FOLD: ")
    while (userChoice.lower() != "call") & (userChoice.lower() != "raise") & (userChoice.lower() != "fold"):
        userChoice = str(input('  Invalid input. Please type "CALL", "RAISE", or "FOLD": '))
    if userChoice.lower() == "call":
        potTot = smBlind * 4
        print(f"  Updated pot total: {potTot}")
        loss = 0
    elif userChoice.lower() == "raise":
        raiseAmt = int(input("  How much would you like to raise: "))
        while (raiseAmt % smBlind != 0) | (raiseAmt <= smBlind) | (raiseAmt > balance - smBlind):
            if (raiseAmt % smBlind != 0) | (raiseAmt <= smBlind):
                raiseAmt = int(input("\n  Error. Your raise must be greater than and divisible by the small blind. \n  Please re-enter raise amount: "))
            elif (raiseAmt > balance - smBlind):
                raiseAmt = int(input("\n  Error. Your raise cannot exceed your balance. \n  Please re-enter raise amount: "))  
        potTot = smBlind * 2 + raiseAmt * 2
        print(f"  Updated pot total: {potTot}")
        loss = 0
    else:
        potTot = smBlind * 3
        loss = smBlind
        print(f"\n  You lost {loss} chips.")
    return userChoice.lower(), potTot, loss

def option2(smBlind, potTot, balance):
    userChoice = input("  Would you like to CHECK, RAISE, or FOLD: ")
    while (userChoice.lower() != "check") & (userChoice.lower() != "raise") & (userChoice.lower() != "fold"):
        userChoice = str(input('  Invalid input. Please type "CHECK", "RAISE", or "FOLD": '))
    if userChoice.lower() == "raise":
        if (balance - potTot / 2 == 0):
            print(f"  You have no chips left to bet.")
            newPotTot = potTot
        else:
            raiseAmt = int(input("  How much would you like to raise: "))
            while (raiseAmt % smBlind != 0) | (raiseAmt <= smBlind) | (raiseAmt > balance - potTot / 2):
                if (raiseAmt % smBlind != 0) | (raiseAmt <= smBlind):
                    raiseAmt = int(input("\n  Error. Your raise must be greater than and divisible by the small blind. \n  Please re-enter raise amount: "))
                elif (raiseAmt > balance - potTot / 2):
                    raiseAmt = int(input("\n  Error. Your raise cannot exceed your balance. \n  Please re-enter raise amount: "))  
            newPotTot = potTot + raiseAmt * 2
            print(f"  Updated pot total: {newPotTot}")
        loss = 0
    elif (userChoice.lower() == "check") | (userChoice.lower() == "fold"):
        newPotTot = potTot
        if userChoice.lower() == "check":
            loss = 0
        elif userChoice.lower() == "fold":
            loss = int(newPotTot / 2)
            print(f"\n  You lost {loss} chips.")
    return userChoice.lower(), newPotTot, loss

def setBlind():
    smBlind = int(input("\nEnter small blind amount: "))
    return smBlind

def setBuyIn(smBlind):
    buyIn = int(input("Enter buy-in amount: "))
    while (buyIn % smBlind != 0) | (buyIn <= smBlind):
        buyIn = int(input(f"Error! Buy-in must be greater than and divisible by {smBlind}. \nPlease re-enter buy-in amouunt: "))
    return buyIn
    
def main():
    smBlind = setBlind()
    balance = setBuyIn(smBlind)

    i = 1
    while i > 0:
        #initiailze deck
        deck = {
        "1": "Ace of Spades",
        "2": "Two of Spades",
        "3": "Three of Spades",
        "4": "Four of Spades", 
        "5": "Five of Spades",
        "6": "Six of Spades",
        "7": "Seven of Spades",
        "8": "Eight of Spades",
        "9": "Nine of Spades",
        "10": "Ten of Spades",
        "11": "Jack of Spades",
        "12": "Queen of Spades",
        "13": "King of Spades",
        "14": "Ace of Hearts",
        "15": "Two of Hearts",
        "16": "Three of Hearts",
        "17": "Four of Hearts", 
        "18": "Five of Hearts",
        "19": "Six of Hearts",
        "20": "Seven of Hearts",
        "21": "Eight of Hearts",
        "22": "Nine of Hearts",
        "23": "Ten of Hearts",
        "24": "Jack of Hearts",
        "25": "Queen of Hearts",
        "26": "King of Hearts",
        "27": "Ace of Clubs",
        "28": "Two of Clubs",
        "29": "Three of Clubs",
        "30": "Four of Clubs", 
        "31": "Five of Clubs",
        "32": "Six of Clubs",
        "33": "Seven of Clubs",
        "34": "Eight of Clubs",
        "35": "Nine of Clubs",
        "36": "Ten of Clubs",
        "37": "Jack of Clubs",
        "38": "Queen of Clubs",
        "39": "King of Clubs",
        "40": "Ace of Diamonds",
        "41": "Two of Diamonds",
        "42": "Three of Diamonds",
        "43": "Four of Diamonds", 
        "44": "Five of Diamonds",
        "45": "Six of Diamonds",
        "46": "Seven of Diamonds",
        "47": "Eight of Diamonds",
        "48": "Nine of Diamonds",
        "49": "Ten of Diamonds",
        "50": "Jack of Diamonds",
        "51": "Queen of Diamonds",
        "52": "King of Diamonds",
    }
        #begin round
        print(f"\nHand #{i}:")
        cards = deal(deck)

        #assign cards
        userCard1 = cards[0]
        compCard1 = cards[1]
        userCard2 = cards[2]
        compCard2 = cards[3]
        burned1 = cards[4]
        river1 = cards[5]
        river2 = cards[6]
        river3 = cards[7]
        burned2 = cards[8]
        river4 = cards[9]
        burned3 = cards[10]
        river5 = cards[11]

        dispHand(userCard1, userCard2) #reveal user hand
        userChoice, potTot1, loss = option1(smBlind, balance)
        if userChoice != "fold":
            dispRiver(river1, river2, river3) #start flop
            userChoice, potTot2, loss = option2(smBlind, potTot1, balance)
            if userChoice != "fold":
        #finish flop
                dispNext(river4)
                userChoice, potTot3, loss = option2(smBlind, potTot2, balance)
                if userChoice != "fold":
                    dispNext(river5)
                    userChoice, potTot4, loss = option2(smBlind, potTot3, balance)
        if userChoice == "fold":
            result = "lose"

        if result == "lose":
            if userChoice != "fold":
                loss = potTot4 / 2
                print(f" You lost {loss} chips.")
            balance -= loss
        elif result == "win":
            gain = potTot4 / 2
            print(f"  You won {gain} chips.")
            balance += gain
        
        print(f"  Updated balance: {balance} chips")
        if balance == 0:
            print(f"\nYou have run out of chips. ")
            balance = setBuyIn(smBlind)

        #end round
        userChoice = str(input('\nType "PLAY" to continue playing, or "STOP" to stop playing: '))
        while (userChoice.lower() != "play") & (userChoice.lower() != "stop"):
            userChoice = str(input('Invalid input. Please type "PLAY" or "STOP": '))
        if userChoice.lower() == "play":
            i += 1
        elif userChoice.lower() == "stop":
            break

    print("\nThank you for playing!\n")

if __name__ == "__main__":
    main()
