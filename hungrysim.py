import random

s_name = ''
hunger_level = 15
hunger_int = 3
s_alive = True
h_levels = ["(Extremely Full)","(Quite Full)","(Full)","(Not Hungry)","(Hungry)","(Very Hungry)","(Starving)"]
choices = ["Eat","Cook","Fish"]
fishes = 0
sammies = 1
inventory = sammies * ["Fish Sammy"]
current_time = 6
fishing_skill = 0
SKILL_BONUS = 1.625
BASE_CHANCE = 2.5

#need to find the rates of hunger decay at various levels to 
# determine how the passing of time affects hunger
# 76 point scale with milestones to mark hunger levels

def safe_input(prompt,options):
    first_letters = []
    print(prompt)
    for option in options:
        first_letter = option[0]
        first_letters.append(first_letter.casefold())
        print("("+option[0].upper()+")"+option[1:(len(option)+1)])
    a = str(input("?"))
    a = a.casefold()
    if a not in first_letters:
        print(a, "is not an option.")
        a = safe_input(prompt,options)
        return a
    else: return a

def increment_time(increment):
    global hunger_level
    global current_time
    hunger_level = hunger_level + increment
    current_time = current_time + increment
    get_hunger_int()

def get_hunger_int():

    # should I be using local variables and returning these 
    # instead of acting on them globally?
    # also, if I do take them as arguments instead of global, is there 
    # any reason not to use the same variable name inside the function?

    global hunger_int
    global s_alive
    global hunger_level

    if hunger_level < 2 : hunger_int = 0
    elif hunger_level < 6 : hunger_int = 1
    elif hunger_level < 12 : hunger_int = 2
    elif hunger_level < 18 : hunger_int = 3
    elif hunger_level < 24 : hunger_int = 4
    elif hunger_level < 36 : hunger_int = 5
    elif hunger_level < 72 : hunger_int = 6
    else: 
        s_alive = False
        print("Whoa.",s_name,"died of hunger.")
        enter_to_continue()
        exit()

def go_fishin():
    
    #I don't really get why I need so many local variables
    #What's the benefit here? Why can't all variables just be global?

    global fishing_skill
    fish_caught = 0

    a_string = ("Fishing Skill: " + str(fishing_skill))
    b_string = ("Fish Caught: " + str(fish_caught))

    print(5 * "\n")
    print(40 * "~")
    print(line_break)
    print("~ " + s_name + (37 - len(s_name)) * " " + "~")
    print(line_break)
    print("~ " + a_string + (37 - len(a_string)) * " " + "~")
    print(line_break)
    print("~ " + b_string + (37 - len(b_string)) * " " + "~")
    print(line_break)
    print(40 * "~")
    print("\nFor how many hours would you like",s_name,"to fish?",end='')
    fish_time = force_number_input()

    chance_to_catch = round((fishing_skill * SKILL_BONUS) + BASE_CHANCE)
    #for skill level 0 this is 3
    total_casts = int(fish_time * 12)

    for x in range(total_casts):
        increment_time(1/12)
        get_hunger_int()
        a = random.randint(1,(100 - chance_to_catch))
        if a == chance_to_catch: 
            print(s_name,"caught a fish!")
            fish_caught += 1
        else: print("Cast and caught... nothing.")
    
    print(s_name,"caught",fish_caught,"fish.")
    for x in range(fish_caught): inventory.append("Fishy")
    enter_to_continue()
    
    return fish_caught

def enter_to_continue():
    input("[PRESS ENTER]")

def force_number_input():
    
    try:
        a = float(input("\n?"))
    except:
        print("Whatchoo talkin' bout?")
        a = force_number_input
    return a

def eat():

    global hunger_level

    if hunger_int == 6: hunger_level = 24
    if hunger_int == 5: hunger_level = 18
    if hunger_int == 4: hunger_level = 12
    if hunger_int == 3: hunger_level = 6
    if hunger_int == 2: hunger_level = 2
    if hunger_int == 1: hunger_level = 0
    increment_time(.5)

print("HUNGER SIMULATOR\n________________\n")

while s_name == '':
    try:
        s_name = str(input("Please name our simulant:\n"))
    except:
        print("That's crazy talk. Try again.")

increment_time(0)

while s_alive:

    a_string = ("Hunger Level: " + str(hunger_int) + "  " + h_levels[hunger_int])
    line_break = "~" + 38 * " " + "~"
    
    inventory.sort()

    print(5 * "\n")
    print(40 * "~")
    print(line_break)
    print("~ " + s_name + (37 - len(s_name)) * " " + "~")
    print(line_break)
    print("~ " + a_string + (37 - len(a_string)) * " " + "~")
    print(line_break)
    print(line_break)
    print("~ " + "Inventory:" + 27 * " " + "~")
    for ea in inventory:
        print("~ " + ea + (37 - len(ea)) * " " + "~")
    print(line_break)
    print(40 * "~")

    A = safe_input("What would you like "+s_name+" to do?",choices)
    
    print(A)

    if A == "e": 
        if  sammies < 1:
            print(s_name,"ain't got none sammies!")
            enter_to_continue()
        else:
            sammies -= 1
            print("mmmm. yummy.")
            inventory.remove("Fish Sammy")
            eat()
            enter_to_continue()
        continue
    elif A == "c":
        if fishes < 1:
            print(s_name,"ain't got none fishes!")
            enter_to_continue()
        else: 
            increment_time(1)
            sammies += 1
            fishes -= 1
            print(s_name,"cooked another mouth-watering sammie!")
            inventory.remove("Fishy")
            inventory.append("Fish Sammy")
            enter_to_continue()
        continue
    elif A == "f":
        fishes += go_fishin()
        
        continue




    

    break    

