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

def main():
    i = 1
    while i > 0:
        #beginning of round
        print(f"Hand #{i}:")


        #end of round
        userChoice = str(input('Type "PLAY" to continue playing, or "STOP" to stop playing: '))
        if userChoice.lower() == "play":
            i += 1
        elif userChoice.lower() == "stop":
            break
    print("Thank you for playing!")

if __name__ == "__main__":
    main()
