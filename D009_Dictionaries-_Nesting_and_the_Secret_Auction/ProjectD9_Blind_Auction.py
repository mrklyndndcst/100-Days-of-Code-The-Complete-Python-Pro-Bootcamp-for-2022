from replit import clear
import Blind_Auction_Art

all_bidder = {}
winner = []
highest = 0
draw_value = 0

run = "yes"
draw = 0
while run == "yes" :
  clear()
  print(Blind_Auction_Art.logo)
  bidder = input("What is your name?: ")
  bid = int(input("What is your bid?: $"))
  if bid == highest:
    draw_value = bid
    draw += 1
  if bid > highest:
    highest = bid
    winner = bidder  
  all_bidder[bidder] : bid
  again = "ok"
  while again == "ok":
    run = input("Are there any other bidders? Type 'yes' or 'no' \n")
    if run == "yes" or run == "no":
      again = "proceed"
    else:
      print("Please type 'yes' or 'no' only")
if draw > 0 and draw_value == highest:
  print("There are two or more than highest bidder!! it's a draw, try again")
else:
  print(f"The winner is {winner} with a bid of ${highest}")
  
#  yy   yy  uu  uu 
#   yy yy   uu  uu
#    yy     uu  uu
#    yy     uu  uu 
#    yy      uuuu     version below 
# 
# from replit import clear
# from art import logo
# print(logo)
# bids = {}
# bidding_finished = False

# def find_highest_bidder(bidding_record):
#   highest_bid = 0
#   winner = ""
#   # bidding_record = {"Angela": 123, "James": 321}
#   for bidder in bidding_record:
#     bid_amount = bidding_record[bidder]
#     if bid_amount > highest_bid: 
#       highest_bid = bid_amount
#       winner = bidder
#   print(f"The winner is {winner} with a bid of ${highest_bid}")

# while not bidding_finished:
#   name = input("What is your name?: ")
#   price = int(input("What is your bid?: $"))
#   bids[name] = price
#   should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
#   if should_continue == "no":
#     bidding_finished = True
#     find_highest_bidder(bids)
#   elif should_continue == "yes":
#     clear()