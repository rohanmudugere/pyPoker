import csv

class Cards():
    all = []
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

        Cards.all.append(self)

    @classmethod
    def addCards(cls):
        with open("EBEC/deck.csv", "r") as file:
            cardDict = csv.DictReader(file)
            cardList = list(cardDict)

        for card in cardList:
            Cards(
                value=card.get("value"),
                suit=card.get("suit"),
            )

    @staticmethod
    def checkStraight(card1, card2, card3, card4, card5, card6, card7):
        cards = [card1, card2, card3, card4, card5, card6, card7]
        values = []
        for card in cards:
            if card.value == "Ace":
                values.append(1)
            value = card.cardVals()
            values.append(value)
        values.sort()
        count = 0
        for i in range(len(values) - 1):
            if values[i+1] == values[i] + 1:
                count += 1
        if (count >= 4) & ((values[len(values) - 1] - values[len(values) - 5] == 4) | (values[4] - values[0] == 4)):
            return True
        else:
            return False

    @staticmethod
    def countPairs(card1, card2, card3, card4, card5, card6, card7):
        cards = [card1, card2, card3, card4, card5, card6, card7]
        count = 0
        for card in cards:
            for c in cards:
                if card.value == c.value:
                    count += 1
        return count 

    def cardVals(self):
        if self.value == "Ace":
            return 14
        elif self.value == "King":
            return 13
        elif self.value == "Queen":
            return 12
        elif self.value == "Jack":
            return 11
        elif self.value == "10":
            return 10
        elif self.value == "9":
            return 9
        elif self.value == "8":
            return 8
        elif self.value == "7":
            return 7
        elif self.value == "6":
            return 6
        elif self.value == "5":
            return 5
        elif self.value == "4":
            return 4
        elif self.value == "3":
            return 3
        elif self.value == "2":
            return 2
        
    def __repr__(self):
        return f"The {self.value} of {self.suit}"

class Suit():
    def __init__(self, name):
        self.name = name

    def checkFlush(self, card1, card2, card3, card4, card5, card6, card7):
        cards = [card1, card2, card3, card4, card5, card6, card7]
        count = 0
        for card in cards:
            if card.suit == self.name:
                count += 1
        if count >= 5:
            return True
        else:
            return False
    
    def checkRFlush(self, card1, card2, card3, card4, card5, card6, card7):
        cards = [card1, card2, card3, card4, card5, card6, card7]
        count = 0
        for card in cards:
            if (card.suit == self.name) & ((card.value == "Ace") | (card.value == "King") | (card.value == "Queen") | (card.value == "Jack") | (card.value == "10")):
                count += 1
        if count == 5:
            return True
        else:
            return False
    
class Player():
    def __init__(self, name, rFlush, sFlush, flush, straight):
        self.name = name
        self.rFlush = rFlush
        self.sFlush = sFlush
        self.flush = flush
        self.straight = straight

    def result(self):
        if self.rFlush == True:
            return 4
        elif self.sFlush == True:
            return 3
        elif self.flush == True:
            return 2
        elif self.straight == True:
            return 1
        else:
            return 0

def createDict(cards):
    keys = []
    for i in range (1, 53):
        keys.append(i)
    return (dict(zip(keys, cards)))

def deal(deck):
    import random as r
    #generate 12 cards
    cards = []
    for i in range(0, 12):
        num = r.choice(list(deck))
        cards.append(deck.pop(num))
    return cards

def dispCards(card1, card2, card3, card4, card5, card6, card7, card8, card9):
    print(f"\n  You have: {card1} & {card2}")
    print(f"\n  The computer has: {card3} & {card4}")
    print(f"\n  In the river: {card5}, {card6}, {card7}, {card8}, & {card9}")

def main():
    print("\nWelcome to Poker!")

    #create class for each player
    user = Player("User", "rFlush", "sFlush", "flush", "straight")
    comp = Player("Comp", "rFlush", "sFlush", "flush", "straight") 

    #create class for each suit
    spades = Suit("Spades")
    clubs = Suit("Clubs")
    hearts = Suit("Hearts")
    diamonds = Suit("Diamonds")

    #create and deal deck 
    Cards.addCards()
    deck = createDict(Cards.all)
    cards = deal(deck)

    #assign and display cards
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
    dispCards(userCard1, userCard2, compCard1, compCard2, river1, river2, river3, river4, river5)

    #check for user flush
    user.flush = Suit.checkFlush(spades, userCard1, userCard2, river1, river2, river3, river4, river5)
    if user.flush == False:
        user.flush = Suit.checkFlush(clubs, userCard1, userCard2, river1, river2, river3, river4, river5)
    if user.flush == False:
        user.flush = Suit.checkFlush(hearts, userCard1, userCard2, river1, river2, river3, river4, river5)
    if user.flush == False:
        user.flush = Suit.checkFlush(diamonds, userCard1, userCard2, river1, river2, river3, river4, river5)
    #check for comp flush
    comp.flush = Suit.checkFlush(spades, compCard1, compCard2, river1, river2, river3, river4, river5)
    if comp.flush == False:
        comp.flush = Suit.checkFlush(clubs, compCard1, compCard2, river1, river2, river3, river4, river5)
    if comp.flush == False:
        comp.flush = Suit.checkFlush(hearts, compCard1, compCard2, river1, river2, river3, river4, river5)
    if comp.flush == False:
        comp.flush = Suit.checkFlush(diamonds, compCard1, compCard2, river1, river2, river3, river4, river5)
    
    #check for user royal Flush
    user.rFlush = Suit.checkRFlush(spades, userCard1, userCard2, river1, river2, river3, river4, river5)
    if user.rFlush == False:
        user.rFlush = Suit.checkRFlush(clubs, userCard1, userCard2, river1, river2, river3, river4, river5)
    if user.rFlush == False:
        user.rFlush = Suit.checkRFlush(hearts, userCard1, userCard2, river1, river2, river3, river4, river5)
    if user.rFlush == False:
        user.rFlush = Suit.checkRFlush(diamonds, userCard1, userCard2, river1, river2, river3, river4, river5)
    #check for comp royal flush
    comp.rFlush = Suit.checkRFlush(spades, compCard1, compCard2, river1, river2, river3, river4, river5)
    if comp.rFlush == False:
        comp.rFlush = Suit.checkRFlush(clubs, compCard1, compCard2, river1, river2, river3, river4, river5)
    if comp.rFlush == False:
        comp.rFlush = Suit.checkRFlush(hearts, compCard1, compCard2, river1, river2, river3, river4, river5)
    if comp.rFlush == False:
        comp.rFlush = Suit.checkRFlush(diamonds, compCard1, compCard2, river1, river2, river3, river4, river5)
    
    #check for user and comp straight
    user.straight = Cards.checkStraight(userCard1, userCard2, river1, river2, river3, river4, river5)
    comp.straight = Cards.checkStraight(compCard1, compCard2, river1, river2, river3, river4, river5)

    userCount = Cards.countPairs(userCard1, userCard2, river1, river2, river3, river4, river5)
    compCount = Cards.countPairs(compCard1, compCard2, river1, river2, river3, river4, river5)
    
    uResult = user.result()
    cResult = comp.result()

    #determine winner
    if (uResult > cResult):
        result = "won"
    elif (uResult < cResult):
        result = "lost"
    elif (userCount > compCount):
        result = "won"
    elif (userCount < compCount):
        result = "lost"
    else:
        value1 = Cards.cardVals(userCard1)
        value2 = Cards.cardVals(userCard2)
        value3 = Cards.cardVals(compCard1)
        value4 = Cards.cardVals(compCard2)

        if value2 > value1:
            value1, value2 = value2, value1
        if value4 > value3:
            value3, value4 = value4, value3
        
        if value1 > value3:
            result = "won"
        elif value1 == value3:
            if value2 > value4:
                result = "won"
            elif value2 == value4:
                result = "tied"
            else:
                result = "lost"
        else:
            result = "lost"
    
    print(f"\nYou {result}!\n")

if __name__ == "__main__":
    main()
