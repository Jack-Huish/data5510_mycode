from DeckOfCards import *

playAgain = 'y'
deck = DeckOfCards()
while playAgain == 'y':
    deck.print_deck()
    deck.shuffle_deck()
    print()
    deck.print_deck()

    # welccome message
    print("Welcome to BlackJack!")

    # keep track of aces
    aceCount = 0
    dealerAceCount = 0

    # deal two cards to the user
    card = deck.get_card()
    card2 = deck.get_card()
    if card.face == "Ace":
        aceCount += 1
    if card2.face == "Ace":
        aceCount += 1
    # just in case of double aces
    score = 0
    score += card.val
    score += card2.val
    while score > 21 and aceCount > 0:
                score -= 10
                aceCount -= 1

    # deal two cards to the dealer
    dealerCard1 = deck.get_card()
    dealerCard2 = deck.get_card()
    if dealerCard1.face == "Ace":
        dealerAceCount += 1
    if dealerCard2.face == "Ace":
        dealerAceCount += 1
    # just in case they get double aces
    dealerScore = dealerCard1.val + dealerCard2.val
    while dealerScore > 21 and dealerAceCount > 0:
                dealerScore -= 10
                dealerAceCount -= 1
    
    # calculate the user's hand score
    print(card)
    print(card2)
    print("Your score is: ", score)

    # set up var to track if busted
    busted = False

    # ask user if they would like a "hit"
    hit = 'y'
    while hit != 'n':
        hit = input("would you like a hit? y/n ")

        if hit == 'y':
            card3 = deck.get_card()
            if card3.face == "Ace":
                aceCount += 1
            score += card3.val
            print(f"User hits, user draws a {card3}")
            print("new score: ", score)
            while score > 21 and aceCount > 0:
                score -= 10
                aceCount -= 1
            if score > 21 and aceCount == 0:
                print("You busted! You lose!")
                busted = True
                break

    # dealer's turn        
    if busted == False:    
        print(f"The dealer's card 1 is: {dealerCard1}")
        print(f"The dealer's card 2 is {dealerCard2}")
        print(f"Dealer's score: {dealerScore}")

        # if dealer is less than 17
        while dealerScore < 17:
            dealerNextCard = deck.get_card()
            if dealerNextCard.face == "Ace":
                dealerAceCount += 1
            dealerScore += dealerNextCard.val
            print(f"Dealer hits, he draws a {dealerNextCard}")
            print("Dealer new score: ", dealerScore)
            while dealerScore > 21 and dealerAceCount > 0:
                dealerScore -= 10
                dealerAceCount -= 1
            if dealerScore > 21 and dealerAceCount == 0:
                break
        
        # determine who the winner is    
        if dealerScore > 21:
            print("Dealer busted! You win!")    
        elif dealerScore > score:
            print("You lose! Dealer had a higher score.")
        elif dealerScore < score:
            print("You win! You had a higher score.")
        else:
            print("Tie game! Nobody wins.")

    playAgain = input("Would you like to play again? y/n ")
