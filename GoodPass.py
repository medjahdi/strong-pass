import string
import random
print(X + "----+----+-----+------+-----+")
print(C + "Welcome to your Strong Password Creator")
print(X + "----+----+-----+------+-----+")

st1 = list(string.ascii_lowercase)
st2 = list(string.ascii_uppercase)
st3 = list(string.digits)
st4 = list(string.punctuation)

while True:
    cha_number_str = input(F + "How many characters do you want for your password?\n==> ")
    try:
        cha_number = int(cha_number_str)
        if cha_number < 6:
            print(Z + "You need at least 6 characters")
        else:
            break  
    except ValueError:
        print(Z + "Please enter a number only\n==> ")

random.shuffle(st1)
random.shuffle(st2)
random.shuffle(st3)
random.shuffle(st4)

p1 = max(round(cha_number * 0.3), 1)
p2 = max(round(cha_number * 0.2), 1)  

password = []

for _ in range(p1):
    password.append(random.choice(st1))
    password.append(random.choice(st2))

for _ in range(p2):
    password.append(random.choice(st3))
    password.append(random.choice(st4))

while len(password) < cha_number:
    password.append(random.choice(st1 + st2 + st3 + st4))

random.shuffle(password) 
password_str = "".join(password)  
print(B + "Your generated password is:", password_str)
print(B + "Thank you for using this tool :)")
