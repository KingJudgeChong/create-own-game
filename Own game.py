import os
import time
import random
import re
# for shortcuts on doing my string outputs
def GC(gc_message):
    print(" \n\033[0;32m \n\033[1;32mGC: ", end='')
    time.sleep(0.8)
    for char in gc_message:
        print(char, end='', flush=True)
        time.sleep(0.03)

def EHunt(ehunt_message):
    print(" \n\033[0;37m \n\033[1;37mE. Hunt: ", end='')
    time.sleep(0.8)
    for char in ehunt_message:
        print(char, end='', flush=True)
        time.sleep(0.03)

def EHunt2(ehunt2_message):
    print(" \n\033[0;37m \n\033[1;37mE. Hunt: ", end='')
    time.sleep(0.8)
    for char in ehunt2_message:
        print(char, end='', flush=True)
        time.sleep(0.03)
    time.sleep(1.5)

def Narrator(narrator_message):
    print(" \n\033[3;37m \n\033[1;37m    ",end='')
    time.sleep(0.8)
    for char in narrator_message:
        print(char, end='', flush=True)
        time.sleep(0.03)

def Narrator2(narrator2_message):
    print(" \n\033[3;37m \n\033[1;37m    ",end='')
    time.sleep(0.8)
    for char in narrator2_message:
        print(char, end='', flush=True)
        time.sleep(0.03)
    time.sleep(1.5)

os.system('cls')
time.sleep(2)
print(" \n \n")
GC("Hello, and welcome to the game called the...\n \n \n")
time.sleep(1.5)
GC("PROJECT MI(MISSION IMPOSSIBLE)")
time.sleep(1.5)
print(" \n \n \n")
name = input("Please enter your codename: ")
name = name.lower()
name = name.title()
print(f" \n \n Good luck and have fun {name}... ")
time.sleep(3)
os.system('cls')
print(" \n \n \n")
time.sleep(3)
Narrator2("Once upon a time when the time is once times to the time...")
print(" \n")
Narrator2("then time times to time is still a time. Then that time times up...")
print(" \n")
Narrator2("very understandable right? So...")
Narrator("let's skip this part. Because I don't understand it either... XD")
time.sleep(3)
os.system('cls')

print(" \n \n \n")

for char in f"    Hello Agent {name}, my name is Ethan Hunt.":
    print(char, end='', flush=True)
    time.sleep(0.05)
time.sleep(1)
print("\n")
EHunt("You've been given a mission to rescue our missing/captured Agents.")
time.sleep(1.5)
os.system('cls')

win_count = 0
#starting game
def all_agents():
    
    os.system('cls')
    collections()
    global agent_name
    global codename
    print(" \n \n")
    print("E. Hunt:", end= '')

    for char in " Here is the list of names: \n \n":
        print(char, end="", flush=True)
        time.sleep(0.05)
        
    time.sleep(1)
    num = 1

    for list_a in easy_list:
        str_list = f"    {num}. {list_a} - easy"
        print()

        for char in str_list:
            print(char, end="", flush=True)
            time.sleep(0.007)
        num += 1
    print(" ")

    for list_b in hard_list:
        str_list = f"    {num}. {list_b} - HARD"
        print()
        for char in str_list:
            print(char, end="", flush=True)
            time.sleep(0.007)
        num += 1
    
    if win_count >= 3:
        print("\n \n\033[4;37m\033[2;37mUNLOCKED MODE\n\033[0;37m")
        
        for key in bonus_mission:
            
            print(f"\033[1;37m    0.\033[3;32m\033[1;32m {key}\033[0;37m", end='', flush=True)
            time.sleep(0.05)
    print("\033[1;37m ")
    time.sleep(2)
    print(" \n \n")
    
    print("E. Hunt:", end='')
    for char in f" Choose a number to rescue Agent {name}\n":
        print(char, end="", flush=True)
        time.sleep(0.05)
    
    choose = input()
    while len(choose) > 1 or choose == ' ' or choose.isalpha() is True:
        
        os.system('cls')    
        print(" \n \n")
        print("    E. Hunt: Here is the list of names: \n \n")
        num = 1
        
        for list_a in easy_list:
            print(f"    {num}. {list_a} - easy", sep='')
            num += 1
        print(" ")
        
        for list_b in hard_list:
            print(f"    {num}. {list_b} - HARD", sep='')
            num += 1
        
        if win_count == 3:
            print("\033[4;37m\033[2;37mUNLOCKED MODE\n\033[0;37m")
            
            for key in bonus_mission:
                
                print(f"\033[1;37m    0.\033[3;32m\033[1;32m {key}\033[0;37m", end='', flush=True)
                            
        print(" \033[1;37m\n \n")
        
        if len(choose) > 1 or choose == ' ':
            print("E. Hunt: Hey only 1 number is allowed. Not 2 or more!\n") 
        
        elif choose.isalpha() is True:          
            print("E. Hunt: That's not a number Agent, don't be scupid. Choose again.\n")
        
        elif win_count != 3 and choose == 0:
            print("E. Hunt: There's no 0 for the mean time. Don't be excited!\n")
        choose = input()
    choose = int(choose)
    os.system('cls')
    time.sleep(2)
    
    if choose >= 1 and choose <= 6:
        agent_name = easy_list[choose - 1]
        codename = target_list_easy[agent_name]
    
    elif choose >= 7 and choose <= 9:    
        agent_name = hard_list[choose % 7]
        codename = target_list_hard[agent_name]
    
    elif choose == 0:
        agent_name = key
        codename = bonus_mission[agent_name]
        
    print(" \n \n")
    print(f"    Name     : ", end='')
    time.sleep(1)
    
    for char in agent_name:
        print(f"\033[3;36m\033[1;36m{char}\033[0;37m", end='', flush=True)
        time.sleep(0.05)
    time.sleep(2)
    
    print(f"\n \n\033[1;37m    Codename : ", end='')
    time.sleep(1)
    
    for char in codename:
        print(f"\033[3;36m\033[1;36m{char}\033[0;37m", end='', flush=True)
        time.sleep(0.05)
    time.sleep(1)
    
    
    difficulty()
# difficulty depends on what number is chosen
def difficulty():
    
    if agent_name in target_list_easy:
        print(" \033[1;37m\n \n")
        EHunt2("Your first mission is to find the location of the target")
        print(" \n")
        EHunt2("Best of luck Agent!")
        os.system('cls')
        print(" \n \n")
        EHunt2("You only have 5 guesses to make it to the next stage Agent\n")
        
        for char in "\n    ... This is easy. You can do this!":
            print(char, end='', flush=True)
            time.sleep(0.007)
        time.sleep(2)
        os.system('cls')
        easy_game()
    
    elif agent_name in target_list_hard:
        print(" \033[1;37m\n \n")
        EHunt2("Your first mission is to find the location of the target")
        print(" \n")
        EHunt2("Best of luck Agent!")
        os.system('cls')
        print(" \n \n")
        EHunt2("You only have 3 guesses to make it to the next stage Agent\n")
        
        for char in "\n    ... This is hard. You still can do this!":
            print(char, end='', flush=True)
            time.sleep(0.007)
        time.sleep(2)
        os.system('cls')
        hard_game()

    else:
        os.system('cls')
        print(" \n \n")
        print("uhm... Good luck? Don't cheat!\n \n")
        time.sleep(2)
        print("\n    You only have 1 guess!")
        time.sleep(2)
        os.system('cls')
        time.sleep(1)
        print("\n \n")
        print("...")
        time.sleep(1.5)   
        EHunt2(f"Hey Agent {name}! We have a major problem...")
        EHunt(f"Have you heard of {agent_name}(\033[1;32mGC\033[0;37m\033[1;37m)")
        time.sleep(1)
        EHunt(f"CODENAME: {codename}")
        time.sleep(1)
        EHunt2("We need to find its data source... A server room, but I don't have a clue yet where it is hiding...")
        EHunt2("But... we can find its location where it was last used.")
        EHunt2("Not the pinpoint but, this will lead us to it.")
        EHunt2(f"Here... as soon as the {agent_name} acted up,\n    it encrypted it's all information just to secure itself from harm")
        EHunt2("I need to go... you do this alone, I might get some information from someone I know.")
        EHunt2(f"Call me later when you finish that one... Good luck agent {name}")
        time.sleep(1)
        Mission_Impossible_Game1()

def easy_game():
    global easy_list
    global easy_hint
    global easyContinent
    global easylength
    global lengthContinent
    global guessed
    global keys_used
    global count
    print(" \n \n ")
    print(easy_hint)
    print(" \n")
    print("    :", lengthContinent )
    print(" \n")
    guess = input()
    guess = guess.upper()
    
    # conditions
    if len(guess) > 1 or guess == ' ':
        print(" \n \n"
        " \n \n"
        "    E. Hunt: Only 1 letter is allowed Agent, not 2 or more and no number alright?") 
        time.sleep(2)  
        os.system('cls')
        
    elif guess.isdigit() is True or len(guess) == 0:
        guess = int()
        print(" \n \n"
        " \n \n"
        "    E. Hunt: that's not a letter, it's a number.")
        time.sleep(2)
        os.system('cls')
       
    elif guess in easyContinent:
        
        if guess in guessed:
            print(" \n \n"
        " \n \n"
        f"    E. Hunt: You already chose '{guess}' earlier. Try another one Agent {name}")
            time.sleep(2)
            os.system('cls')

        else:
            print(" \n \n"
        " \n \n"
        "    E. Hunt: Nice, another one...")
            time.sleep(1)
        
        guessed.extend([guess])
        result = [*easyContinent]
        result2 = [*lengthContinent]
        

        for index, word in enumerate(result):
            
            if index == len(result2):
                continue
            if word == guess:
                result2[index] = result[index]
                        
        easyContinent = easyContinent.replace(guess, "_")
        easyContinent = "".join(result)
        lengthContinent = "".join(result2)
        
        os.system('cls')
    elif guess in keys_used:
        
        print(" \n \n"
        " \n \n"
        f"    E. Hunt: You already chose '{guess}' earlier. Try another one Agent {name}")
        time.sleep(2)
        os.system('cls')
    else:
        
        count += 1
        
        if count == 1:
            
            print(" \n \n"
            "\n \n"
            "   E. Hunt: It's okay! We all make mistakes sometimes.")
            time.sleep(2)
            os.system('cls')

        elif count == 2:
            print(" \n \n"
            " \n \n"
            "   E. Hunt: Take it easy alright?")
            time.sleep(2)
            os.system('cls')
            
        elif count == 3:
            print(" \n \n"
            " \n \n"
            "   E. Hunt: Hey hey, take it slow. Don't rush.")
            time.sleep(2)
            os.system('cls')
            
        elif count == 4:
            
            print(" \n \n"
            " \n \n"
            f"   E. Hunt: {name}... Listen... I want you to think carefully. focus!\n")
            time.sleep(5)
            print("   This is your last chance... Don't let me down Agent")
            time.sleep(5)
            os.system('cls')

        elif count == 5:
            os.system('cls')
            time.sleep(2)
            print(" \n \n \n...")
            time.sleep(2)

            import tkinter as tk
            root = tk.Tk()
            root.title("WTF!")
            root.geometry("1197x732")

            photo = tk.PhotoImage(file= "ehunt.png")

            label = tk.Label(root, image= photo, width= 1197, height= 732,
            bg= "black", fg= "yellow", font=('Arial',30,'bold'))
            label.pack()

            root.mainloop()
            time.sleep(5)
            
            pass

    keys_used.extend([guess]) 

    # end game
    if lengthContinent == easyContinent:       
        os.system('cls')
        print(" \n \n \n \n    ", end='')
        EHunt(f"Good Job Agent {name}, you got it right.\n \n")
        time.sleep(1)
        print(f"  It is '{lengthContinent}'\n \n" )
        print()
        time.sleep(3)
        os.system('cls')
        print(" \n \n")
        Narrator(f"...After locating and planning the place of {codename}... E. Hunt and {name} arrived at their target destination \n")
        time.sleep(3)
        os.system('cls')
        print("")
        time.sleep(1)
        print(" \n \n...\n \n")
        time.sleep(1.5)
        Narrator(f"E. Hunt and {name} disguised themselves and enters the building...")
        time.sleep(1.5)
        os.system('cls')
        time.sleep(2)
        print(" \n \n...\n \n")
        time.sleep(1)
        Narrator(f"As they walk along inside the building, E. Hunt suddenly stops and pretends to talk with {name} just right beside the corner...\n")
        time.sleep(3)
        EHunt2(f"Okay {name}... I want you to stay calm alright...\n")      
        EHunt2("Look at my 8... [8 o'clock of Hunt]\n")       
        EHunt2("See that guy? He has the card on the upper floor... but before he can go up in that elevator...\n")      
        EHunt2("He gonna put that passcode first. And that passcode is only 1.\n")       
        EHunt("I want you to look carefully and guess what did he put...")
        time.sleep(3)
        os.system('cls')
        Narrator(f" \n \n...As soon as the guy went in going up... They walk towards the passcode and {name} tries to guess it.")
        time.sleep(4)
        return easy_game2()
                    
    elif count == 5:
            
        print(" \n \n \n")
        print(f"    It is '{easyContinent}'\n \n")
        time.sleep(2)
        print("   E. Hunt: I DON'T WANT TO SEE YOU AGAIN. GET OUTTA HERE!")
        time.sleep(3)
        print(
        " \n \n")                       

        collections()

        play_loop()

    return easy_game()

def easy_game2():
    
    
    os.system('cls')
    print(" \n \n \n \n \n \n")
    time.sleep(2)
    EHunt(f"Now tell me Agent {name}... what did you see? What's your guess?")
    time.sleep(3)
    os.system('cls')
    random_num = random.randint(1, 10)
    num_guesses = 0
    easy_hint2 = " \n \nHint:    1-10"
    
    while num_guesses < 5:
        print(" \n \n")
        print(easy_hint2) 
        print(" \n \nE. Hunt: Remember, you only need to guess from 1 to 10. \n \n")
        print("    Guess the number! \n")
        num_guess = input("           ")
        
        if num_guess.isdigit() is False:
            print(f"\nE. Hunt: Oh... that's not a number {name}\n")
            time.sleep(2)
            os.system('cls')

        else:
            num_guess = int(num_guess)

            if num_guess < random_num:
                easy_hint2 = f"Hint:    Your guess is too low {name}." 
                os.system('cls')
            
            elif num_guess > random_num:
                easy_hint2 = f"Hint:    Your guess is too high {name}."
                os.system('cls')
            
            elif num_guess == random_num:
                EHunt2(f"YESSS, GUARD DUNK IT Agent {name}, YOU PACKING GOT IT. \n")                 
                EHunt2("I thought you're a loser for a second\n")                
                EHunt2("...Anyway, let's go to the next stage\n")               
                os.system('cls')
                Narrator(" \n \n...after the passcode became successful ...\n \n    They went straight to the elevator and goes up up and away. XD")
                time.sleep(3)
                Narrator("...As soon as they got out the elevator, they went further until they \n \n    saw the door where their comrade locked up. ")
                print(" \n \n")
                print("...\n \n")
                time.sleep(3)
                EHunt2("Wait a minute... we saw that guy with a card... but we dont need that at all...\n")                
                EHunt2("Instead, this is another passcode to open the door. but somehow it's kinda like it needs a password... \n \n")                
                Narrator2("They look around the place and saw a riddle...\n \n")                
                EHunt("Hold on, I think this riddle is the passcode...\n")
                time.sleep(3)
                os.system('cls')
                print(" \n \n \n")
                EHunt(f"{riddles_key} \n \n")
                return easy_game3()                
        
        num_guesses += 1
    
    time.sleep(1)
    print(" \n \n")
    print("...")   
    time.sleep(2)
    print("\n \n") 
    EHunt("Maybe you should accept the fact that you cant do this mission alone.")
    time.sleep(3)    

    play_loop()

    return easy_game2()

def easy_game3():
    time.sleep(3)
    EHunt2(f"I know you can figure this out Agent {name}")
    EHunt2("Only 5 guesses or else, they will know that somebody is here... ")
    os.system('cls')
   
    answer_count = 0

    while answer_count < 6:
        print(" \n \n \n")
        print(riddles_key)
        print(" \n \n")
        answer = input()
        answer = answer.upper()
        
        if answer == riddle_ans:
            os.system('cls')
            print(" \n \n")
            time.sleep(2)
            print("...\n \n")
            Narrator(f"Door opened... there {codename} was tied up, Agent {name} cut it loose!")
            time.sleep(1)
            Narrator2("E. Hunt came after few minutes...\n")
            EHunt(f"Well done Agent! Here take a drink *gives a bottled water* and after that...\n\n    let's get the hell out of here guys.\n \n")
            time.sleep(3)
            Narrator("After the rescue mission, they left without the enemy noticing them...\n \n")
            time.sleep(3)
            print("    Mission Accomplished! \n\n    ...and they live happily ever after")
            time.sleep(3)
            import tkinter as tk
            root = tk.Tk()
            root.title("Happily Ever After!")
            root.geometry("1197x732")

            photo = tk.PhotoImage(file= "shrek.png")

            label = tk.Label(root, image= photo, width= 1197, height= 732,
            bg= "black", fg= "yellow", font=('Arial',30,'bold'))
            label.pack()

            root.mainloop()
            time.sleep(3)
            os.system('cls')
            
            replay = input(" \n \n \n  "
            "     Would you like to play again and choose another rescue mission?\n \n")   
            os.system('cls')

            if replay == 'y':
            
                os.system('cls')
                all_agents()
    
            elif replay == 'n':
                for char in " \n \n \n \nPagkatapos mo paglaruan iiwan mo din pala... \n \n    Grabe kana... naiintindihan ko. Go lang keep it up\n \n \n \n \n":
                    print(char, end='', flush=True)
                    time.sleep(0.007)
                time.sleep(2)
                exit()    
    
            else:
                print(" \n \n \n \n \n \n \n \n"
                "    Sorry, the game will exit because you chose something that is not there. Thank you! \n \n \n \n \n \n \n \n \n \n")
                time.sleep(3)
                exit()

        else:
            os.system('cls')
            print(" \n \nWrong!")
            answer_count += 1

    collections()
    play_loop()
    os.system('cls')
    return easy_game3()

def hard_game():
    global hard_hint
    global hardCountry
    global hardlength
    global lengthCountry
    global guessed
    global keys_used
    global count
    print(" \n \n ")
    print(f"    Hint: {hard_hint}")
    print(" \n")
    print("    :", lengthCountry )
    print(" \n")
    guess = input()
    guess = guess.upper()
    
    # conditions
    if len(guess) > 1 or guess == ' ':
        print(" \n \n"
        " \n \n"
        "    E. Hunt: Only 1 letter is allowed Agent, not 2 or more and no number alright?")  
        time.sleep(2) 
        os.system('cls')
        
    elif guess.isdigit() is True or len(guess) == 0:
        guess = int()
        print(" \n \n"
        " \n \n"
        "    E. Hunt: that's not a letter, it's a number.")
        time.sleep(2)
        os.system('cls')
       
    elif guess in hardCountry:
        
        if guess in guessed:
            print(" \n \n"
        " \n \n"
        f"    E. Hunt: You already chose '{guess}' earlier. Try another one Agent {name}")
            time.sleep(2)
            os.system('cls')

        else:
            print(" \n \n"
        " \n \n"
        "    E. Hunt: Nice, another one...")
            time.sleep(1)
        
        guessed.extend([guess])
        result = [*hardCountry]
        result2 = [*lengthCountry]
        

        for index, word in enumerate(result):
            
            if index == len(result2):
                continue

            if word == guess:
                result2[index] = result[index]
                        
        hardCountry = hardCountry.replace(guess, "_")
        hardCountry = "".join(result)
        lengthCountry = "".join(result2)   
        os.system('cls')

    elif guess in keys_used:
        
        print(" \n \n"
        " \n \n"
        f"    E. Hunt: You already chose '{guess}' earlier. Try another one Agent {name}")
        time.sleep(2)
        os.system('cls')
        
    else:
        
        count += 1
        
        if count == 1:
            print(" \n \n"
            " \n \n"
            "    E. Hunt: Take it easy alright?")
            time.sleep(2)
            os.system('cls')
            
        elif count == 2:
            
            print(" \n \n"
            " \n \n"
            f"    E. Hunt: {name}... Listen... I want you to think carefully. focus!\n")
            time.sleep(3)
            print("   This is your last chance... Don't let me down Agent")
            time.sleep(4)
            os.system('cls')

        elif count == 3:
            os.system('cls')
            time.sleep(2)
            print(" \n \n \n...")
            time.sleep(2)

            import tkinter as tk
            root = tk.Tk()
            root.title("WTF!")
            root.geometry("1197x732")

            photo = tk.PhotoImage(file= "ehunt.png")

            label = tk.Label(root, image= photo, width= 1197, height= 732,
            bg= "black", fg= "yellow", font=('Arial',30,'bold'))
            label.pack()

            root.mainloop()
            time.sleep(5)
            
            pass

    keys_used.extend([guess]) 

    # end game of hard game 1
    if lengthCountry == hardCountry:
        
        os.system('cls')
        print(" \n \n \n \n    ", end='')
        EHunt(f"Good Job Agent {name}, you got it right.\n \n")
        time.sleep(1)
        print(f"    It is '{lengthCountry}'\n \n" )
        print()
        time.sleep(3)
        os.system('cls')
        print(" \n \n")
        EHunt2("Let's get ready for our next mission...")
        print(" \n \n")
        os.system('cls')
        Narrator(f"...After locating and planning the place of {codename}... E. Hunt and {name} arrived at their target destination \n")
        time.sleep(3)
        os.system('cls')
        print("")
        time.sleep(1)
        print(" \n \n...\n \n")
        time.sleep(2)
        Narrator2(f"E. Hunt and {name} disguised themselves and enters the building...") 
        os.system('cls')
        time.sleep(2)
        print(" \n \n...\n \n")
        time.sleep(1)
        Narrator(f"As they walk along inside the building, E. Hunt suddenly stops and pretends to talk with {name} just right beside the corner...\n")
        time.sleep(3)
        EHunt2(f"Okay {name}... I want you to stay calm alright...\n")        
        EHunt2("Look at my 8... [8 o'clock of Hunt]\n")        
        EHunt2("See that guy? He has the card on the upper floor... but before he can go up in that elevator...\n")        
        EHunt2("He gonna put that passcode first. And that passcode is only 1.\n")        
        EHunt2("I want you to look carefully and guess what did he put...")
        os.system('cls')
        print(" \n")
        Narrator(f"...As soon as the guy went in going up... They walk towards the passcode and {name} tries to guess it. \n \n")
        time.sleep(3)
        os.system('cls')
        return hard_game2()
                    
    elif count == 3:
            
        print(" \n \n \n")
        print(f"    It is '{hardCountry}'\n \n")
        time.sleep(2)
        print("\n    ", end='')
        EHunt("I DON'T WANT TO SEE YOU AGAIN. GET OUTTA HERE!")
        time.sleep(2)
        print(
        " \n \n")                       

        collections()
        play_loop()
        return hard_game()
    hard_game()

def hard_game2():
    os.system('cls')    
    print(" \n \n \n \n \n")
    time.sleep(1)
    EHunt2("You only have 3 guesses... \n")
    EHunt(f"Now tell me Agent {name}... what did you see? What's your guess?")
    time.sleep(3)
    os.system('cls')
    randomUpperLetter = chr(random.randint(ord('A'), ord('Z')))
    num_guesses = 0
    hard_hint2 = " \n \nHint:    A - Z"
    
    while num_guesses < 3:
        print(" \n \n")
        print(hard_hint2) 
        print(f" \n \nE. Hunt: Remember, you have to guess from A - Z Agent {codename} \n \n")
        print("    Guess the letter! \n")
        str_guess = input("           ")
        
        if str_guess.isalpha() is False:
            print(f"\nE. Hunt: Oh... that's not a number {name}\n")
            time.sleep(2)
            os.system('cls')

        else:
            str_guess = str(str_guess)
            str_guess = str_guess.upper()
            
            if ord(str_guess) < ord(randomUpperLetter):
                hard_hint2 = f"Hint:    Your guess is too low {name}." 
                os.system('cls')
            
            elif ord(str_guess) > ord(randomUpperLetter):
                hard_hint2 = f"Hint:    Your guess is too high {name}."
                os.system('cls')
            
            elif str_guess == randomUpperLetter:
                EHunt2(f"YESSS, GUARD DAM IT Agent {name}, YOU PACKING GOT IT. \n")                
                EHunt2("I thought you're a loser for a second\n")                
                EHunt2("...Anyway, let's go to the next stage\n")
                os.system('cls')
                time.sleep(1)
                Narrator("\n...after the passcode became successful ... \n \nThey went straight to the elevator and goes up up and away. XD")
                time.sleep(3)
                Narrator("...As soon as they got out the elevator, they went further until they \n \n    saw the door where their comrade locked up. ")
                print(" \n \n")
                print("...\n \n")
                time.sleep(3)
                EHunt2("Wait a minute... we saw that guy with a card... but we dont need that at all...\n")
                EHunt("Instead, this is another passcode to open the door. but somehow it's kinda like it needs a password... \n \n")
                time.sleep(3)
                Narrator2("... They look around the place and saw a riddle...\n \n")
                EHunt2("Hold on, I think this riddle is the passcode...\n")
                os.system('cls')
                print(" \n \n \n")
                EHunt2("... \n \n")
                EHunt2(f"{name}, you better solve this one... I need to find us a way out... \n \n")
                EHunt2(f"We can't go back down there... or we'll be dead {name}... \n \n")
                EHunt("Only 3 guesses or else, they will know that we're here... ")                

                return hard_game3()                
        
        num_guesses += 1
    
    time.sleep(1)
    print(" \n \n")
    print("...")   
    time.sleep(2) 
    print(" \n \n")
    EHunt2("Maybe you should accept the fact that you can't do this mission alone.")
    play_loop()
    return hard_game2()

def hard_game3():
    
    time.sleep(2)
    os.system('cls')
    EHunt2(f"I know you can figure that out on your own Agent {name}")
    EHunt2("I'll be back! See you later...")
    os.system('cls')
    answer_count = 0
    
    while answer_count < 3:
        print(" \n \n \n")
        print(riddles_key)
        print(" \n \n")
        answer = input()
        answer = answer.upper()
        
        if answer == riddle_ans:
            os.system('cls')
            print(" \n \n")
            time.sleep(2)
            print("...\n \n")
            Narrator(f"...Door opened... there {codename} was tied up, Agent {name} cut it loose!")
            time.sleep(1)
            Narrator2("E. Hunt came after few minutes...\n")
            EHunt(f"Well done Agent! Here take a drink *gives a bottled water* and after that...\n\n    let's get the hell out of here guys.\n \n")
            time.sleep(3)
            Narrator2("After the rescue mission, they left without the enemy noticing them...\n \n")
            print("    Mission Accomplished!\n\n    ....and they live happily ever after")
            time.sleep(3)

            import tkinter as tk
            root = tk.Tk()
            root.title("Hangman Game!")
            root.geometry("1197x732")

            photo = tk.PhotoImage(file= "shrek.png")

            label = tk.Label(root, image= photo, width= 1197, height= 732,
            bg= "black", fg= "yellow", font=('Arial',30,'bold'))
            label.pack()

            root.mainloop()
            time.sleep(3)
            os.system('cls')
            secret_passage()
            
            replay = input(" \n \n \n  "
            "     Would you like to play again and choose another rescue mission?\n \n")   
            os.system('cls')
            if replay == 'y':
            
                os.system('cls')
                all_agents()
    
            elif replay == 'n':
                for char in " \n \n \n \nPagkatapos mo paglaruan iiwan mo din pala... \n \n    Grabe kana... naiintindihan ko. Go lang keep it up\n \n \n \n \n":
                    print(char, end='', flush=True)
                    time.sleep(0.007)
                time.sleep(2)
                exit()    
    
            else:
                print(" \n \n \n \n \n \n \n \n"
                "    Sorry, the game will exit because you chose something that is not there. Thank you! \n \n \n \n \n \n \n \n \n \n")
                time.sleep(3)
                exit()

        else:
            print(" \n \nWrong!")
            time.sleep(1)
            os.system('cls')
            answer_count += 1
    
    collections()
    play_loop()
    return hard_game3()
# this for unlocking insane mode
def secret_passage():
    global win_count
    win_count += 1
    
def Mission_Impossible_Game1():
    os.system('cls')
    print("\n \n")
    print(morse_hint)
    print(" \n \n")
    for char in result_morse_country:
        print(char, end='', flush=True)
        time.sleep(0.010)
    print("\n")
    guess = input("    Guess the code: ")
    guess = guess.upper()
    if guess == MIG_Country:
        time.sleep(1)
        os.system('cls')
        time.sleep(1)
        print("...")
        print(" \n \n    ", end='')
        EHunt2(f"Well done {name}. Did you cheat?")
        print("\n \n    ", end='')
        EHunt2("Jk, okay okay let's just move on to the next. You should go to that place ASAP...\n")
        EHunt2("I'll be there... call you later ...\n")
        os.system('cls')
        print("\n \n")
        Narrator("A FEW HUNDRED AND A HALF YEARS LATER")
        time.sleep(1)
        os.system('cls')
        time.sleep(1)
        print("\n \n...")
        print("\n")
        EHunt2(f"Agent {name}... According to the location that you found,\n \n    I spoke with one of our comrades who live there...")
        EHunt2("She said that she lost her partner when they tried to investigate one of the places they'd been to.")
        EHunt2("...You know what I mean. Anyway, before her partner died, her partner gave an information \n \n   that maybe would lead to us that is connected to what we're finding.")
        EHunt2("Here... I'll send you the message that she gave me.")
        EHunt2("It's encrypted so you better decrypt it. I'll see you later")
        EHunt2(f"Good luck Agent {name}!")
        Mission_Impossible_Game2()

    else:
        print(" \n \n")
        GC("Oops! Sorry, your answer is wrong.\n \n     Just go back to where you belong. Shu shu... Don't find me!\n \n    Come back when you're ready\n \033[0.37m \033[1.37m")
        time.sleep(1)
        collections()
        play_loop()
        return Mission_Impossible_Game1()
    os.system('cls')

def Mission_Impossible_Game2():
    os.system('cls')
    shift = random.randint(1,5)
    shift2 = random.randint(1,10)
    shift3 = random.randint(1,3)
    key_result = []
    value_result = []
    hint_result = []
    
    for char in use_CCipher:
        ascii_index = ord(char)

        if ascii_index >= 65 and ascii_index <= 90:         
            ascii_code = ascii_index + shift 
            if ascii_code > 90:
                solution = ascii_code % 90
                ascii_code = 64 + solution
            result = chr(ascii_code)
          

        elif ascii_index >= 97 and  ascii_index <= 122:
            ascii_code = ascii_index + shift
            if ascii_code > 122:
                solution = ascii_code % 122
                ascii_code = 96 + solution
            result = chr(ascii_code)


        elif ascii_index < 97 and ascii_index > 90:
            result = chr(ascii_index)
        
        elif ascii_index < 65 or ascii_index > 122:
            result = chr(ascii_index)

        key_result.append(result)
        key_code = ''.join(key_result)
    
    for char2 in value_CCipher:
        ascii_index2 = ord(char2)

        if ascii_index2 >= 65 and ascii_index2 <= 90:         
            ascii_code = ascii_index2 + shift2 
            if ascii_code > 90:
                solution2 = ascii_code % 90
                ascii_code = 64 + solution2
            result2 = chr(ascii_code)
          

        elif ascii_index2 >= 97 and  ascii_index2 <= 122:
            ascii_code = ascii_index2 + shift2
            if ascii_code > 122:
                solution2 = ascii_code % 122
                ascii_code = 96 + solution2
            result2 = chr(ascii_code)


        elif ascii_index2 < 97 and ascii_index2 > 90:
            result2 = chr(ascii_index2)
        
        elif ascii_index2 < 65 or ascii_index2 > 122:
            result2 = chr(ascii_index2)

        value_result.append(result2)
        value_code = ''.join(value_result)

    for char3 in "Caesar Cipher":
        ascii_index3 = ord(char3)

        if ascii_index3 >= 65 and ascii_index3 <= 90:         
            ascii_code = ascii_index3 + shift3
            if ascii_code > 90:
                solution3 = ascii_code % 90
                ascii_code = 64 + solution3
            result3 = chr(ascii_code)
          
        elif ascii_index3 >= 97 and  ascii_index3 <= 122:
            ascii_code = ascii_index3 + shift3
            if ascii_code > 122:
                solution3 = ascii_code % 122
                ascii_code = 96 + solution3
            result3 = chr(ascii_code)

        elif ascii_index3 < 97 and ascii_index3 > 90:
            result3 = chr(ascii_index3)
        
        elif ascii_index3 < 65 or ascii_index3 > 122:
            result3 = chr(ascii_index3)
        
        hint_result.append(result3)
        hint_code = ''.join(hint_result)
    
    print("\n \n")
    print(f"    Hint:    {hint_code}\n \n")
    print(f"Message:    {key_code} \n")
    username = input("Decrypt Message: ")
    print("\n \n")
    print(f"Password:    {value_code} \n")
    password = input("Decrypt Password: ")

    if username == use_CCipher and password == value_CCipher:
        os.system('cls')
        print(" \n \n    Congratulations: You beat the game!")
        replay = input("\n \nDo you wish to play again and choose another rescue mission? y/n: ")
        
        if replay == 'y':
            all_agents()
        
        elif replay == 'n':
            print("\n \n")
            
            for char in "    PAGKATAPOS MO PAGLARUAN, SABAY IIWAN. NAKO HA, BAD YAN...\n \n    SIGE... HULI PERO HINDI KULONG :)":
                print(char, end='', flush=True)
                time.sleep(0.07)
                exit()
        else:
            print("\n \n    Wrong letter, this game will exit!")
            exit()        
        
    else:
        os.system('cls')
        print(" \n \n    Message or Password is incorrect!")
        collections()
        play_loop()
        return Mission_Impossible_Game2()
# my given variables collection   
def collections():
    global easy_list
    global hard_list
    global target_list_easy
    global target_list_hard
    global easy_hint
    global hard_hint
    global riddles_keys
    global riddles_key
    global riddle_ans
    global easyContinent
    global hardCountry
    global easylength
    global hardlength
    global lengthContinent
    global lengthCountry
    global guessed
    global keys_used
    global count
    global bonus_mission
    global morse_hint
    global result_morse_country
    global result_morse_continent
    global MIG_Country
    global use_CCipher
    global value_CCipher

    target_list_easy = {
    "Ace Mirasol": "MiraAce",   
    "Celso Diamante": "CelDi",
    "Dorothy Amante" : "DorAne ",
    "Mark Joseph Rivere": "MarvisJoe",
    "Paolo Pendon" : "PaloPeo",
    "Robert Anthony Daligdig" : "RoaD"}

    target_list_hard = {
    "Chiza Ma-ang" : "MaChi",
    "Eladio Dionisio" : "DonElon",
    "Rubeth Joy Padernal" : "RubyJadePearl"}

    easy_list = list(target_list_easy.keys())
    hard_list = list(target_list_hard.keys())

    easyContinents = ["AFRICA", "ANTARCTICA", "ASIA", "AUSTRALIA", "EUROPE", "NORTH AMERICA", "SOUTH AMERICA"]
    easy_hint = "Hint:   It is one of Earth's seven main divisions of land"

    easyContinent = random.choice(easyContinents)
    easylength = len(easyContinent)
    lengthContinent = re.sub(r'\S', '_', easyContinent)

    hardCountries = {
    "Africa" : "UGANDA",
    "Asia" : "TURKMENISTAN",
    "Europe" : "MONTENEGRO",
    "North America" : "HONDURAS",
    "Australia" : "PAPUA NEW GUINEA",
    "South America" : "SURINAME",
    "Europe(2)" : "BELARUS"}

    listCountries = list(hardCountries)
    hardCountry = random.choice(listCountries)
    hard_hint = f"{hardCountry} is waving"
    hardCountry = hardCountries.get(hardCountry)
    hardlength = len(hardCountry)
    lengthCountry = re.sub(r'\S', '_', hardCountry)
    


    riddles = {
    "   What goes up but never comes down? " : "AGE",
    "   What can fill a room but takes up no space? " : "LIGHT",
    "   What word can be written forward, backward or upside down, and can still be read from left to right? " : "NOON",
    "   What word of five letters has one left when two are removed? " : "STONE",
    "   What has many keys but can't open a single lock?" : "PIANO",
    "   What gets bigger when more is taken away? " : "HOLE",
    "   What is seen in the middle of March and April that can't be seen at the beginning or end of either month? " : 'R',
    "   What comes once in a minute, twice in a moment, but never in a thousand years? " : 'M',
    "   What is able to go up a chimney when down but unable to go down a chimney when up? " : "UMBRELLA",
    "   I am the beginning of the end of time and space that surrounds every place. What am I? " : 'E',
    }

    riddles_keys = list(riddles.keys())
    riddles_key = random.choice(riddles_keys)
    riddle_ans = riddles.get(riddles_key)
    
    guessed = []
    keys_used = []

    count = 0

    morse_code = {
    'E' : '.', 'I' : "..", 'S' : "...", 'H' : "....", '5' : ".....",
    'A' : ".-", 'R' : ".-.", 'L' : ".-..", 'W' : ".--", 'P' : ".--.", 'J' : ".---", '1' : ".----",
    'U' : "..-", 'F' : "..-.", '2' : "..--",
    'V' : "...-", '3' : "...--",
    '4' : "....-",
    'T' : '-', 'M' : "--", 'O' : "---", '0' : "-----", '9' : "----.",
    'N' : "-.", 'K' : "-.-", 'Y' : "-.--", 'C' : "-.-.", 'D' : "-..", 'X' : "-..-", 'B' : "-...", '6' : '-....',
    'G' : "--.", 'Q' : "--.-", 'Z' : "--..", '7' : "--...",
    '8' : "---..", ' ' : '/'
    }

    First_MIG_Countries = {
    "ERITREA" : "EAST AFRICA",
    "BURKINA FASO" : "WEST AFRICA",
    "KIRIBATI" : "OCEANIA",
    "PHILIPPINES" : "ASIA"}

    # it needs to be change to morse code before guessing
    MIG_Country = random.choice(list(First_MIG_Countries))
    morse_country = []
    
    # gets the result of morse code of country
    for char in MIG_Country:
        string_char = morse_code.get(char)
        morse_country.append(string_char)
        result_morse_country = ' '.join(morse_country)
    
    # get the value of mig country
    MIG_Continent = First_MIG_Countries.get(MIG_Country)
    morse_continent = []

    for char2 in MIG_Continent:
        string_char2 = morse_code.get(char2)
        morse_continent.append(string_char2)
        result_morse_continent = ' '.join(morse_continent)

    morse_hint = f"    Hint:  {result_morse_continent}"

    CCipher = {
    "Alam ko na ung sagot" : "Iknowtheanswer",
    "Ang hirap naman nyan" : "walabamasmadali",
    "Magaling ako" : "hindiakomagaling",           
    "Hindi ko din masagutan ung code ko" : "kayokasi",
    "King Judge David Aquino Chong" : "nicetomeetyouguysthankyou"}

    use_CCipher = random.choice(list(CCipher))
    value_CCipher = CCipher.get(use_CCipher)
    
    
    bonus_mission = {"GAME CODE" : "THE SOURCE"}
# play loop for my game
def play_loop():
    replay = input(" \n \n \n  "
    "     Would you like to play again? y/n \n \n")  
    replay = replay.lower() 
    os.system('cls')
    if replay == 'y':
        print(" \n \n")
        for char in "    LALARO KA ULIT? GANYAN KA NAMAN TALAGA, NANGLALARO NG FEELINGS\n":
            print(char, end="", flush=True)
            time.sleep(0.02)
        time.sleep(2)
        retry = input(" \n    Do you wish to go back and choose another rescue mission? y/n: ")
        retry = retry.lower()
        if retry == 'y':
            os.system('cls')
            print(f" \n \n    Good luck and have fun Agent {name}!")
            time.sleep(2)
            all_agents()
        elif retry == 'n':
            for char in "\n \n    GUSTO MO BUMAWI AND ITAMA UNG PAGKAKAMALI MO NG SHORTCUT?\n \n        SIGE SIGE GOOD IDEA. HAHAHAHA\n":
                print(char, end="", flush=True)
                time.sleep(0.02)
            time.sleep(1)
            retry1 = input(" \n    Oh I see now, you like to retry the stage intead? y/n: ")
            retry1 = retry1.lower()
            if retry1 == 'y':
                os.system('cls')
                print(" \n \n")
                print(f"    Good luck Agent {name}!")
                time.sleep(2)
                return True
            elif retry1 == 'n':
                os.system('cls')
                print(" \n \n")
                for char in"    WALA KA PALA E... MAGYEYES YES KA TAPOS SA HULI AATRAS KA DIN PALA.\n \n    TAKOT PALA EH... WOOOH!!!\n":
                    print(char, end="", flush=True)
                    time.sleep(0.02)
                time.sleep(2)
                print("\n \n    Thank you for playing! \n \n \n \n \n \n \n \n")
                exit()
                
            else:
                os.system('cls')
                print(" \n \n \n")
                for char in "    Y OR N LANG HINIHINGI KO TAPOS GUSTO MO PA NG IBA. KAYA KA NASASAKTAN EH.\n    MAPILI KA KASI":
                    print(char, end="", flush=True)
                    time.sleep(0.02)
                print(" \n \n \n    YOU CLICKED THE WRONG BUTTON. GOODBYE NA SAYO MAPILI!\n \n \n \n \n")
                time.sleep(2)
                exit()
        else:
            os.system('cls')
            print(" \n \n \n")
            for char in "    Y OR N LANG HINIHINGI KO TAPOS GUSTO MO PA NG IBA. KAYA KA NASASAKTAN EH.\n    MAPILI KA KASI":
                print(char, end="", flush=True)
                time.sleep(0.02)
            print(" \n \n \n    YOU CLICKED THE WRONG BUTTON. GOODBYE NA SAYO MAPILI!\n \n \n \n \n")
            time.sleep(2)
            exit()
    elif replay == 'n':
        os.system('cls')
        for char in "    TAMA YAN PALAKAS KA MUNA MGA LEVEL 69 PARA PAGBALIK MO, \n     MAY CHANCE NA BALIKAN KA NYA OKAY?":
            print(char, end="", flush=True)
            time.sleep(0.02)
        time.sleep(2)
        print(" \n \n    Bye! Thank you for playing! ^_^")
        print(" \n \n \n \n \n")
        exit()
    else:
        os.system('cls')
        print(" \n \n \n")
        for char in "    Y OR N LANG HINIHINGI KO TAPOS GUSTO MO PA NG IBA. KAYA KA NASASAKTAN EH.\n    MAPILI KA KASI":
            print(char, end="", flush=True)
            time.sleep(0.02)
        print(" \n \n \n    YOU CLICKED THE WRONG BUTTON. GOODBYE NA SAYO MAPILI!\n \n \n \n \n")
        time.sleep(2)
        exit()



collections()
all_agents()