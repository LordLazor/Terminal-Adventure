import time


def slow_print(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.02)

def slower_print(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(1)
        
wizard_name = "Otto:"

slow_print(
"""
Someone: Hello Adventurer, welcome to Adventopia!

Could you please tell me your name?
"""
)

name = str(input())

slow_print(f"""
Someone: Hello {name}, it's nice to meet you.           

Wait a second, is it really you {name}?
      
My name is Otto and I am the great wizard of Adventopia, and I have been waiting for you to arrive my king.
""")

time.sleep(2)

slow_print(f"""
{wizard_name} While you were away there was a great war between the forces of good and evil. 
The evil wizard has taken over the kingdom and has enslaved the people of Adventopia.

We now need you to defeat the evil wizard and bring peace to the kingdom.

""")

answer = ""

count_declined = 0
declined = False

while answer != "yes":
    if count_declined >= 1:
        slow_print(f"{wizard_name} Ok if you don't want to help us I will destroy you.\nGAME OVER\n")
        exit()
    
    if declined:
        slow_print(f"{wizard_name} You must accept the quest to save the kingdom! There is no way around it so just type 'yes' idiot.\n")
        count_declined += 1    
    
    slow_print(f"Do you accept this quest? (yes/no)\n")
    declined = True
    
    answer = str(input())
    
slow_print(f"{wizard_name} Alright let's do it!\nYou have to travel to the Myster Castle through the Forrest of the kind Dead Souls. which lies next to the beach of the angry pirates.\n")

slow_print(f"Write 1 to go this way or 2 to ask him if there is a easier way. (Try to use something else aswell)\n")

answer = str(input())

if answer == "2":
    slow_print(f"{wizard_name} I could defeat him but I am too lazy to do it. I will just tell you the way.\n")

if answer != "2" and answer != "1":
    slow_print(f"{wizard_name} You are not very smart are you? I don't care if you don't want to do this quest. I don't have more time to waste. Leave me alone and go.\n")

slow_print(f"{wizard_name} Good luck on your journey {name}!\n")

slow_print("--- CHAPTER 1 -> Beach of the Angry Pirates ---\n")

slow_print(f"You have arrived at the beach of the dead angry pirates. You see a pirate with a map in his hand. You need this map to find the exakt way to the Forrest of the kind Dead Souls. How do you want to defeat him?\n")
slow_print(f"Write 1 to use you fist.\n")
slow_print(f"Write 2 to use sand.\n")
slow_print(f"Write 3 to use a stone.\n")
slow_print(f"Write 4 to use a stick.\n")
slow_print(f"Write 5 to try to run.\n")
slow_print(f"Write 6 to ask hime nicely.\n")

answer = str(input())

if answer == "1":
    slow_print(f"He uses your fist to kill you.\nGAME OVER\n")
    exit()
    
if answer == "2":
    slow_print(f"You throw sand in his eyes ... ... ... ... not very affective. Dead people don't have eyes. He killed you.\nGAME OVER\n")
    exit()

if answer == "3":
    slow_print(f"You throw a stone at him but he evaded it and killed you.\nGAME OVER\n")
    exit()
    
if answer == "4":
    slow_print(f"You hit him with the stick but it did nothing to him. He is now very angry and kills you.\nGAME OVER\n")
    exit()

if answer == "5":
    slow_print(f"You tripped over a stone and died.\nGAME OVER\n")
    exit()

if answer == "6":
    slow_print(f"You ask him nicely and he gives you the map.\n")
    
slow_print("--- CHAPTER 2 -> Forrest of the kind Dead Souls\n")

slow_print("You arrive at the forrest. You see a dead soul flying above your head and want to get past him. What do you wan't to do?\n")
slow_print("Write 1 to ask him nicely\n")
slow_print("Write 2 to throw a rock\n")
slow_print("Write 3 to hit him with a stick\n")
slow_print("Write 4 to run\n")
slow_print("Write 5 to go the other way\n")

answer = str(input())

if answer == "1":
    slow_print("He doesn't care about you and kills you.\nGAME OVER\n")
    exit()
    
if answer == "2":
    slow_print("The rock went through him because he is only a sould and now he is very angry and kills you.\nGAME OVER\n")
    exit()
    
if answer == "3":
    slow_print("You hit him with the stick but it did nothing to him. He is now very angry and kills you.\nGAME OVER\n")
    exit()
    
if answer == "4":
    slow_print("You run but he is faster and kills you.\nGAME OVER\n")
    exit()
    
if answer == "5":
    slow_print("You go the other way and find a secret path to the castle.\n")
    
slow_print("--- CHAPTER 3 -> Myster Castle\n")

slow_print("You arrive at the castle. You see the evil wizard standing in front of you. What do you want to do?")
slow_print("Write 1 to ask him nicely")
slow_print("Write 2 to throw a rock")
slow_print("Write 3 to hit him with a stick")
slow_print("Write 4 to find a way to the castle")
slow_print("Write 5 to run")

answer = str(input())

if answer == "1":
    slow_print("He doesn't care about you and kills you with his mighty staff of fire.\nGAME OVER\n")
    exit()
    
if answer == "2":
    slow_print("He dodges the rock and kills you with his mighty staff of water.\nGAME OVER\n")
    exit()
    
if answer == "3":
    slow_print("He destroyed your stick with his mighty staff of earth and kills you.\nGAME OVER\n")
    exit()
    
if answer == "4":
    slow_print("You are already inside the castle and in front of the evil wizard? Wow, good job he now stands in front of you and kills you with his mighty staff of wind.\nGAME OVER\n")
    exit()
    
if answer == "5":
    slow_print("You run and he trips over a stone and dies.\n")
    
slow_print("You have defeated the evil wizard and saved the kingdom of Adventopia!\n")

slower_print("...\n")
slower_print("...\n")
slower_print("...\n")

slow_print("Now as you return as the king who defeated the evil wizard you will be remembered as the greatest king of all time.\n")

slow_print("Until you decided to kill everyone in your kindom. :)\n")

slow_print("THE END\n")