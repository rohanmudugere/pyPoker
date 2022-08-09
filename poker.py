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
            if (card.suit == self.name) & ((card.value == "Ace") | (card.value == "King") | (card.value == "Queen") | (card.value == "Jack")| (card.value == "10")):
                count += 1
        if count == 5:
            return True
        else:
            return False

    @staticmethod
    def checkAmt(card1, card2, card3, card4, card5, card6, card7):
        cards = [card1, card2, card3, card4, card5, card6, card7]
        count = [0, 0, 0, 0, 0, 0, 0]
        fourOfKind = False
        fullHouse = False
        threeOfKind = False
        twoPair = False
        pair = False
        
        i = 0
        for card1 in cards:
            for card2 in cards:
                if card1.value == card2.value:
                    count[i] += 1
            i += 1
        
        for i in range(len(count)):
            if count[i] == 4:
                fourOfKind == True
            elif count[i] == 3:
                threeOfKind == True
            elif count[i] == 2:
                pair == True
        
        return fourOfKind, threeOfKind, pair

class Player():
    def __init__(self, name, rFlush, sFlush, fourOfKind, fullHouse, flush, straight, threeOfKind, twoPair, pair):
        self.name = name
        self.rFlush = rFlush
        self.sFlush = sFlush
        self.fourOfKind = fourOfKind
        self.fullHouse = fullHouse
        self.flush = flush
        self.straight = straight
        self.threeOfKind = threeOfKind
        self.twoPair = twoPair
        self.pair = pair

    def result(self):
        if self.rFlush == True:
            return 9
        elif self.sFlush == True:
            return 8
        elif self.fourOfKind == True:
            return 7
        elif self.fullHouse == True:
            return 6
        elif self.flush == True:
            return 5
        elif self.straight == True:
            return 4
        elif self.threeOfKind == True:
            return 3
        elif self.twoPair == True:
            return 2
        elif self.pair == True:
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
    print(f"\n  You have {card1} & {card2}")
    print(f"\n  The computer has {card3} & {card4}")
    print(f"\n  In the river: {card5}, {card6}, {card7}, {card8}, & {card9}")

def main():
    print("\nWelcome to Poker!")

    #create class for each player
    user = Player("User", "rFlush", "sFlush", "fourOfKind", "fullHouse", "flush", "straight", "threeOfKind", "twoPair", "pair")
    comp = Player("Comp", "rFlush", "sFlush", "fourOfKind", "fullHouse", "flush", "straight", "threeOfKind", "twoPair", "pair") 

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

    user.fourOfKind, user.threeOfKind, user.pair = Suit.checkAmt(userCard1, userCard2, river1, river2, river3, river4, river5)
    comp.fourOfKind, comp.threeOfKind, comp.pair = Suit.checkAmt(compCard1, compCard2, river1, river2, river3, river4, river5)

    #determine winner
    if user.result() > comp.result():
        result = "won"
    elif user.result() < comp.result():
        result = "lost"
    else:
        result = "tie"
    print(f"\nYou {result}!")

if __name__ == "__main__":
    main()
