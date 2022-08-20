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
        values = list(set(values))
        count = 0
        for i in range(len(values) - 4):
            if values[i + 4] - values[i] == 4:
                high = values[i + 4]
                count += 1
        if count > 0:
            return True, high
        else:
            high = 0
            return False, high

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
        cardsInSuit = []
        for card in cards:
            if card.suit == self.name:
                value = card.cardVals()
                cardsInSuit.append(value)
        if len(cardsInSuit) >= 5:
            high = max(cardsInSuit)
            return True, high
        else:
            high = 0
            return False, high
    
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
    
    def checkSFlush(self, card1, card2, card3, card4, card5, card6, card7):
        cards = [card1, card2, card3, card4, card5, card6, card7]
        cardsInSuit = []
        for card in cards:
            if(card.suit == self.name):
                cardsInSuit.append(card)
        if len(cardsInSuit) >= 5:
            values = []
            for card in cardsInSuit:
                if card.value == "Ace":
                    values.append(1)
                value = card.cardVals()
                values.append(value)
            values.sort()
            count = 0
            for i in range(len(values) - 4):
                if values[i + 4] - values[i] == 4:
                    high = values[i + 4]
                    count += 1
            if count > 0:
                return True, high
            else:
                high = 0
                return False, high
        else: 
            high = 0
            return False, high
    
class Player():
    def __init__(self, name, rFlush, sFlush, fourKind, fullHouse, flush, straight, threeKind, twoPair, pair):
        self.name = name
        self.rFlush = rFlush
        self.sFlush = sFlush
        self.fourKind = fourKind
        self.fullHouse = fullHouse
        self.flush = flush
        self.straight = straight
        self.threeKind = threeKind
        self.twoPair = twoPair
        self.pair = pair

    def countPairs(self, card1, card2, card3, card4, card5, card6, card7):
        cards = [card1, card2, card3, card4, card5, card6, card7]
        values = []
        for card in cards:
            value = card.cardVals()
            values.append(value)
        numApp = []
        val1 = 0
        val2 = 0
        for i in range(2, 15):
            ct = values.count(i)
            if ct == 3:
                val1 = i
            elif ct == 2:
                val2 = i
            numApp.append(ct)
        
        count2 = 0
        count3 = 0
        count4 = 0
        for n in range(len(numApp)):
            if numApp[n] == 2:
                count2 += 1
            elif numApp[n] == 3:
                count3 += 1
            elif numApp[n] == 4:
                count4 += 1
        
        if count4 >= 1:
            self.fourKind = True
        if (count3 >= 1) & (count2 >= 1):
            self.fullHouse = True
        if count3 >= 1:
            self.threeKind = True
        if count2 >= 2: 
            self.twoPair = True
        if count2 == 1:
            self.pair = True
        
        return val1, val2

    def result(self):
        if self.rFlush == True:
            result = 9
        elif self.sFlush == True:
            result = 8
        elif self.fourKind == True:
            result = 7
        elif self.fullHouse == True:
            result = 6
        elif self.flush == True:
            result = 5
        elif self.straight == True:
            result = 4
        elif self.threeKind == True:
            result = 3
        elif self.twoPair == True:
            result = 2
        elif self.pair == True:
            result = 1
        else:
            result = 0
        return result

def createDeck(cards):
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
    user = Player("User", "rFlush", "sFlush", "fourKind", "fullHouse", "flush", "straight", "threeKind", "twoPair", "pair")
    comp = Player("Comp", "rFlush", "sFlush", "fourKind", "fullHouse", "flush", "straight", "threeKind", "twoPair", "pair") 

    #create class for each suit
    spades = Suit("Spades")
    clubs = Suit("Clubs")
    hearts = Suit("Hearts")
    diamonds = Suit("Diamonds")

    #create and deal deck 
    Cards.addCards()
    deck = createDeck(Cards.all)
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
    user.flush, uFHigh = Suit.checkFlush(spades, userCard1, userCard2, river1, river2, river3, river4, river5)
    if user.flush == False:
        user.flush, uFHigh = Suit.checkFlush(clubs, userCard1, userCard2, river1, river2, river3, river4, river5)
        if user.flush == False:
            user.flush, uFHigh = Suit.checkFlush(hearts, userCard1, userCard2, river1, river2, river3, river4, river5)
            if user.flush == False:
                user.flush, uFHigh = Suit.checkFlush(diamonds, userCard1, userCard2, river1, river2, river3, river4, river5)
    #check for comp flush
    comp.flush, cFHigh = Suit.checkFlush(spades, compCard1, compCard2, river1, river2, river3, river4, river5)
    if comp.flush == False:
        comp.flush, cFHigh = Suit.checkFlush(clubs, compCard1, compCard2, river1, river2, river3, river4, river5)
        if comp.flush == False:
            comp.flush, cFHigh = Suit.checkFlush(hearts, compCard1, compCard2, river1, river2, river3, river4, river5)
            if comp.flush == False:
                comp.flush, cFHigh = Suit.checkFlush(diamonds, compCard1, compCard2, river1, river2, river3, river4, river5)
    
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
    
    #check for user straight Flush
    user.sFlush, uSFHigh = Suit.checkSFlush(spades, userCard1, userCard2, river1, river2, river3, river4, river5)
    if user.sFlush == False:
        user.sFlush, uSFHigh = Suit.checkSFlush(clubs, userCard1, userCard2, river1, river2, river3, river4, river5)
        if user.sFlush == False:
            user.sFlush, uSFHigh = Suit.checkSFlush(hearts, userCard1, userCard2, river1, river2, river3, river4, river5)
            if user.sFlush == False:
                user.sFlush, uSFHigh = Suit.checkSFlush(diamonds, userCard1, userCard2, river1, river2, river3, river4, river5)
    #check for comp straight flush
    comp.sFlush, cSFHigh = Suit.checkSFlush(spades, compCard1, compCard2, river1, river2, river3, river4, river5)
    if comp.sFlush == False:
        comp.sFlush, cSFHigh = Suit.checkSFlush(clubs, compCard1, compCard2, river1, river2, river3, river4, river5)
        if comp.sFlush == False:
            comp.sFlush, cSFHigh = Suit.checkSFlush(hearts, compCard1, compCard2, river1, river2, river3, river4, river5)
            if comp.sFlush == False:
                comp.sFlush, cSFHigh = Suit.checkSFlush(diamonds, compCard1, compCard2, river1, river2, river3, river4, river5)

    #check for user and comp straight
    user.straight, uSHigh = Cards.checkStraight(userCard1, userCard2, river1, river2, river3, river4, river5)
    comp.straight, cSHigh = Cards.checkStraight(compCard1, compCard2, river1, river2, river3, river4, river5)

    #check user and comp pairs
    u3Val, uPairVal = Player.countPairs(user, userCard1, userCard2, river1, river2, river3, river4, river5)
    c3Val, cPairVal = Player.countPairs(comp, compCard1, compCard2, river1, river2, river3, river4, river5)
    
    uResult = user.result()
    cResult = comp.result()

    #get high card values 
    value1 = Cards.cardVals(userCard1)
    value2 = Cards.cardVals(userCard2)
    value3 = Cards.cardVals(compCard1)
    value4 = Cards.cardVals(compCard2)
    if value2 > value1:
        value1, value2 = value2, value1
    if value4 > value3:
        value3, value4 = value4, value3

    #determine winner
    if uResult > cResult:
        result = "won"
    elif uResult < cResult:
        result = "lost"
    elif (uResult == 1) | (uResult == 2) | (uResult == 3) | (uResult == 6):
        if u3Val > c3Val:
            result = "won"
        elif u3Val < c3Val:
            result = "lost"
        elif uPairVal > cPairVal:
            result = "won"
        elif uPairVal < cPairVal:
            result = "lost"
        elif value1 > value3:
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
    elif uResult == 4:
        if uSHigh > cSHigh:
            result = "won"
        elif uSHigh == cSHigh:
            result = "tied"
        else:
            result = "lost"
    elif uResult == 5:
        if uFHigh > cFHigh:
            result = "won"
        elif uFHigh == cFHigh:
            result = "tied"
        else:
            result = "lost"
    elif uResult == 8:
        if uSFHigh > cSFHigh:
            result = "won"
        elif uSFHigh == cSFHigh:
            result = "tie"
        else:
            result = "lost"     
    else:   
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
