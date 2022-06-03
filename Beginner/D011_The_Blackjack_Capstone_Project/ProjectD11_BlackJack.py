import random
import time
import BlackJack_Art
from replit import clear

deck = [
    "A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K",
    "A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K",
    "A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K",
    "A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K",
   ]

def draw_card():
    time.sleep(1)
    card = random.randint(0,len(deck)-1)
    del deck[card]
    return deck[card]

def sum():
    total=0
    for to_add in adding:
        if to_add != "A" and to_add != "J" and to_add != "Q" and to_add != "K":
            total += int(to_add)
        if to_add == "J" or to_add == "Q" or to_add == "K" :
            total += 10
    for add_a in adding:        
        if add_a == "A":
            if total + 11 > 21:
                total += 1
            elif total + 11 <= 21:
                total += 11
    return total    

game = False
while game == False:
    dealer_card = []    #card on hand of the dealer
    dealer_total = 0
    player_card = []    #card on hand of the player
    player_pick = 0     #card to pick of the player
    start = input("Do you want to play a game of Blackjack? Type 'y' or 'n':").lower()
    if start == "y":
        player_pick += 2
        clear()
        print(BlackJack_Art.logo)
        while player_pick != 0:
            if player_pick == 2:
                new_card = draw_card()
                print(f"Dealer picked {new_card}")
                dealer_card.append(new_card)

            new_card = draw_card()
            print(f"Player picked {new_card}")
            player_pick -= 1
            player_card.append(new_card)

            if player_pick == 0:
                adding = player_card
                player_total = sum()

                adding = dealer_card
                dealer_total = sum()

                if player_total > 21:
                    time.sleep(1)
                    print(f"Player have {player_total} BUSTS")
                    print("Dealer Wins!!!")
                elif player_total == 21 and len(player_card) == 2:
                    time.sleep(1)
                    print("Player have {player_card} BLACKJACK")
                    if dealer_total == 10 or dealer_total == 11: 
                        new_card = draw_card()
                        print(f"Dealer picked {new_card}")
                        dealer_card.append(new_card)  
                        adding = dealer_card
                        dealer_total = sum()      
                        if dealer_total == 21:
                            time.sleep(1)
                            print(f"The player {player_card} and dealer {dealer_card} each have Blackjack the result is a PUSH.")
                        elif dealer_total != 21:
                            time.sleep(1)
                            print(f"Player have {player_card} and dealer {dealer_card}")
                            print("Player Wins!!!")
                    elif dealer_total != 10 or dealer_total != 11:
                        time.sleep(1)
                        print(f"Player have {player_card} BLACKJACK")
                        print("Player Wins!!!")   
                elif player_total <= 21:
                    time.sleep(1)
                    print(f"Player have {player_card} total of {player_total}")
                    hit = input("HIT or STAND? type the word itself: ").lower()
                    if hit == "hit":
                        player_pick += 1
                    else:                
                        while dealer_total < 17:
                            new_card = draw_card()
                            print(f"Dealer picked {new_card}")
                            dealer_card.append(new_card)   
                            adding = dealer_card
                            dealer_total = sum()
                        if dealer_total == 21 and len(dealer_card) == 2:
                            print(f"Dealer have {dealer_card} BLACKJACK")
                            print("dealer Wins!!!")  
                        elif dealer_total > 21:
                            time.sleep(1)
                            print(f"The Dealer have {dealer_total} BUSTS")
                            print("Player Wins!!!")
                        elif dealer_total > player_total:
                            time.sleep(1)
                            print(f"Player have lower hand {player_card} total of {player_total}")
                            print(f"Dealer have higher hand {dealer_card} total of {dealer_total}")
                            print("Dealer Wins!!!")
                        elif dealer_total < player_total:
                            time.sleep(1)
                            print(f"Dealer have lower hand {dealer_card} total of {dealer_total}")
                            print(f"Player have higher hand {player_card} total of {player_total}")
                            print("Player Wins!!!")
                        else:
                            time.sleep(1)
                            print(f"Player have {player_card} total of {player_total}")
                            print(f"Dealer have {dealer_card} total of {dealer_total}")
                            print("The Player and The dealer have same value NO ONE WINS.")