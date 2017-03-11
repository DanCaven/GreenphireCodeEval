import random
chars = "qwertyuiopasdfghjklzxcvbnm"
letters = [i for i in chars]
print(letters)
for i in range(10000):
    print(random.choice(letters))
    print(random.choice(letters))
    for i in range(5):
        print(random.randint(1,69))
    print(random.randint(1,16))
    print("no")
print("yes")
