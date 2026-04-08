import random

def game_win(user, computer):
    if user == computer:
        return None
    elif user == "s":
        if computer == "w":
            return True
        elif computer == "g":
            return False
    elif user == "w":
        if computer == "g":
            return True
        elif computer == "s":
            return False
    elif user == "g":
        if computer == "s":
            return True
        elif computer == "w":
            return False
        
rand_no = random.randint(1, 3)

print("Computers_turn : Snake(s), Water(w), Gun(g)")

if rand_no == 1:
    computer = "s"
elif rand_no == 2:
    computer = "w"
else:
    computer = "g"

print("Choose any one: Snake(s), Water(w), Gun(g)")
user = input("Enter your turn: ").lower()

result = game_win(user  , computer)

print(f"Computer choose : {computer}")
print(f"User choose : {user}")

if result is None:
    print("Game is Draw")
elif result:
    print("You Win")
else:
    print("You Lose")