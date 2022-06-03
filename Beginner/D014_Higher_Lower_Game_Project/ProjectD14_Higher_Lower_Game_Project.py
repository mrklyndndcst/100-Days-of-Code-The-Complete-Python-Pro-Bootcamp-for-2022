import Higher_Lower_Game_Project_Art
import Higher_Lower_Game_Project_Data
from replit import clear

def random():
    import random
    return random.randint(1,len(Higher_Lower_Game_Project_Data.data))
    
randnuma = random()

aname = Higher_Lower_Game_Project_Data.data[randnuma]['name']
adescription = Higher_Lower_Game_Project_Data.data[randnuma]['description']
acountry = Higher_Lower_Game_Project_Data.data[randnuma]['country']
afollower_count = Higher_Lower_Game_Project_Data.data[randnuma]['follower_count']

score = 0
game = True
while game == True:
    clear()
    print(Higher_Lower_Game_Project_Art.logo)

    if score > 0:
        print(f"You're right! Current score: {score}.")

    print(f"Compare A: {aname}, a {adescription}, from {acountry}.")

    print(Higher_Lower_Game_Project_Art.vs)

    same = True
    while same == True:
        randnumb = random()
        bname = Higher_Lower_Game_Project_Data.data[randnumb]['name']
        bdescription = Higher_Lower_Game_Project_Data.data[randnumb]['description']
        bcountry = Higher_Lower_Game_Project_Data.data[randnumb]['country']
        bfollower_count = Higher_Lower_Game_Project_Data.data[randnumb]['follower_count']
        if aname == bname:
            same = True
        else:
            same = False

    print(f"Against B: {bname}, a {bdescription}, from {bcountry}.")

    if afollower_count > bfollower_count:
        higher = 'a'
    else:
        higher = 'b'

    choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    if choice == higher:
        score += 1
        aname = bname
        adescription = bdescription
        acountry = bcountry
        afollower_count = bfollower_count

    else:
        clear()
        print(Higher_Lower_Game_Project_Art.logo)
        print(f"Sorry, that's wrong. Final score: {score}.")
        game = False

#  yy   yy  uu  uu 
#   yy yy   uu  uu
#    yy     uu  uu
#    yy     uu  uu 
#    yy      uuuu     version below 

# from game_data import data 
# import random
# from art import logo, vs
# from replit import clear

# def get_random_account():
#   """Get data from random account"""
#   return random.choice(data)

# def format_data(account):
#   """Format account into printable format: name, description and country"""
#   name = account["name"]
#   description = account["description"]
#   country = account["country"]
#   # print(f'{name}: {account["follower_count"]}')
#   return f"{name}, a {description}, from {country}"

# def check_answer(guess, a_followers, b_followers):
#   """Checks followers against user's guess 
#   and returns True if they got it right.
#   Or False if they got it wrong.""" 
#   if a_followers > b_followers:
#     return guess == "a"
#   else:
#     return guess == "b"


# def game():
#   print(logo)
#   score = 0
#   game_should_continue = True
#   account_a = get_random_account()
#   account_b = get_random_account()

#   while game_should_continue:
#     account_a = account_b
#     account_b = get_random_account()

#     while account_a == account_b:
#       account_b = get_random_account()

#     print(f"Compare A: {format_data(account_a)}.")
#     print(vs)
#     print(f"Against B: {format_data(account_b)}.")
    
#     guess = input("Who has more followers? Type 'A' or 'B': ").lower()
#     a_follower_count = account_a["follower_count"]
#     b_follower_count = account_b["follower_count"]
#     is_correct = check_answer(guess, a_follower_count, b_follower_count)

#     clear()
#     print(logo)
#     if is_correct:
#       score += 1
#       print(f"You're right! Current score: {score}.")
#     else:
#       game_should_continue = False
#       print(f"Sorry, that's wrong. Final score: {score}")

# game()