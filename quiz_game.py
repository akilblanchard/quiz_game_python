playing = input('Do you know as much as a Service Desk Technician? ')
if playing.lower() == "yes":
    print("Welcome to my quiz!")
else:
    print("Yea, I didn't think so either :p")
    exit()

score = 0


answer = input("1. Can a device connected to the internet have an IP Address of 127.0.0.1? ")
if answer.lower() == "no":
    print("Lucky guess")
    score += 1
else:
    print("Incorrect...")


answer = input("2. Does a HDD offer better performance than an SSD? ")
if answer.lower() == "no":
    print("Lucky guess")
    score += 1
else:
    print("Incorrect...")


answer = input("3. Does the command ipconfig allow you to see a computer's network settings? ")
if answer.lower() == "yes":
    print("Maybe you are smart...")
    score += 1
else:
    print("Incorrect...")


answer = input("4. Wat does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Lucky guess")
    score += 1
else:
    print("Incorrect...")


answer = input("5. Are files stored on the RAM? ")
if answer.lower() == "no":
    print("Lucky guess")
    score += 1
else:
    print("Incorrect...")
print("You got " + str(score) + " questions correct!")

if score < 5 :
    print("Go study!")
    exit()


if score == 5 :
    print("You are smart!")
    bonus = input('Are you up for the bonus question? ')
    if bonus.lower() == "no":
     exit()
else:
    pass



extra = input("BONUS. A filled DHCP server means no printers can connect? ")
if extra == "no":
    score += 1
    print("You know what you're about! You got all " + str(score) + " questions correct!")
else:
    print("Too much dip on your chip buddy!")
    exit()

