import random
round = 0
coin = random.randint(1,2)
h = 0
t = 0

print("Tossing a coin...")
while round < 3:
    coin = random.randint(1,2)
    round += 1
    if coin == 1:
        print("Round", round,": Heads")
        h += 1
    elif coin == 2:
        print("Round", round,": Tails")
        t += 1
print("Heads:", h,", Tails:", t)
if h > t:
    print("You won")
else:
    print("You lost")
