#create item store.


import random


n_of_days = 1

def day_counter():
    global n_of_days
    return (f"it's day {n_of_days}.")



def start_day():
    player_choice = input(f"\n{day_counter()} what would you like to do?\n\na: enter cat event \nb: buy a cat \nc: go to the item store\n").lower()
    if player_choice == "a":
        get_cat_choice()
    elif player_choice == "b":
        cat_store()


def cat_store():
    global cat_store_list
    global player_inventory
    loop_times = len(cat_store_list)
    loop_counter = 0
    print("\nhello there, we have the following cats for sale.\n")
    while loop_counter < loop_times:
        for c in cat_store_list:
            print(f"{c.name} {c.cost} gold")
            print(loop_counter)
            loop_counter += 1
    buy_choice = input("\nwhich cat would you like to buy? (please type in the number displayed beneath the cat you'd like to buy).\n")
    added_cat = cat_store_list[int(buy_choice)]
    if added_cat.cost == player_inventory["gold"] or added_cat.cost < player_inventory["gold"]:
        player_inventory['cats'] += [added_cat]
        player_inventory["gold"] -= added_cat.cost
        print("\nexcelent choice")
        start_day()
    else:
        print("\noh no, you do not have enough gold!")
        start_day()



def get_cat_choice():
    global player_inventory
    loop_times = len(player_inventory['cats'])
    loop_counter = 0
    print("\nyour options are:")
    while loop_counter < loop_times:
        for c in player_inventory['cats']:
            print(c.name)
            print(loop_counter)
            loop_counter += 1
    cat_choice = input("\nwhich cat would you like to enter? (please type in the number displayed beneath the cat you'd like to use).\n")
    player_cat = player_inventory["cats"][int(cat_choice)]
    get_event_choice(player_cat)
    


def get_event_choice(player_cat):
        event_choice = input('''\nalright which event would you like to enter?\n
a: easy cat event\n
b: medium cat event\n
c: difficult cat event\n
d: very difficult cat event\n
e: extremely difficult cat event\n
f: insanely difficult cat event\n
g: catto madness cat event\n
h: catto madness return of the cat, cat even\n
i: super special catto cup return of the mad catto's legacy, cat event\n
j: the cat-tastic cat event\n''').lower()
        if event_choice == "a":
            print(cat_event(random.sample(player_cat.hunt, k=1), random.sample(cat_one.hunt, k=1), random.sample(cat_two.hunt, k=1), random.sample(cat_three.hunt, k=1)))
        elif event_choice == "b":
            print(cat_event(random.sample(player_cat.hunt, k=1), random.sample(cat_four.hunt, k=1), random.sample(cat_five.hunt, k=1), random.sample(cat_six.hunt, k=1)))
        elif event_choice == "c":
            print(cat_event(random.sample(player_cat.hunt, k=1), random.sample(cat_seven.hunt, k=1), random.sample(cat_eight.hunt, k=1), cat_nine.hunt))
        elif event_choice == "d":
            print(cat_event(random.sample(player_cat.hunt, k=1), random.smaple(cat_ten.hunt, k=1), random.sample(cat_eleven.hunt, k=1), random.sample(cat_twelve.hunt, k=1)))
        elif event_choice == "e":
            print(cat_event(random.sample(player_cat.hunt, k=1), random.sample(cat_thirteen.hunt, k=1), random.sample(cat_fourteen.hunt, k=1), random.sample(cat_fifteen.hunt, k=1)))
        elif event_choice == "f":
            print(cat_event(random.sample(player_cat.hunt, k=1), random.sample(cat_sixteen.hunt, k=1), random.sample(cat_seventeen.hunt, k=1), cat_eighteen.hunt))
        elif event_choice == "g":
            print(cat_event(random.sample(player_cat.hunt, k=1), random.sample(cat_nineteen.hunt, k=1), random.sample(cat_twenty.hunt, k=1), random.sample(cat_twenty_one.hunt, k=1)))
        elif event_choice == "h":
            print(cat_event(random.sample(player_cat.hunt, k=1), random.random.sample(cat_twenty_two.hunt, k=1), random.sample(cat_twenty_three.hunt, k=1), random.sample(cat_twenty_four.hunt, k=1)))
        elif event_choice == "i":
            print(cat_event(random.sample(player_cat.hunt, k=1), random.sample(cat_twenty_five.hunt, k=1), random.sample(cat_twenty_six.hunt, k=1), cat_twenty_seven.hunt))
        elif event_choice == "j":
            print(cat_event(random.sample(player_cat.hunt, k=1), random.sample(cat_twenty_eight.hunt, k=1), random.sample(cat_twenty_nine.hunt, k=1), random.sample(cat_thirty.hunt, k=1), cat_thirty_one.hunt, random.sample(cat_thirty_two.hunt, k=1), random.sample(cat_thirty_three.hunt, k=1)))
        else:
            return get_event_choice()
            


def cat_event(player_cat_score, *args):
    highest_cat = max(args)
    if player_cat_score > highest_cat:
        print("congrats, your cat won\n")
        get_reward(player_cat_score)
    else:
        print("that's too bad you lost\n")
        end_day()


def get_reward(player_cat_score):
    global player_inventory
    player_inventory["gold"] += player_cat_score[0]
    print(f"you have received {player_cat_score[0]} gold\n")
    end_day()


def end_day():
    global n_of_days
    player_choice = input("it's the end of the day, what would you like to do?\n\na: go to sleep\nb: buy a cat\nc: go to the item store\n")
    if player_choice == "a":
        n_of_days += 1
        start_day()
    elif player_choice == "b":
        print("\nnah you are too tired\n")
        return end_day()


class Cat:
    def __init__(self, name, color, age, hunt, cost):
        self.name = name
        self.color = color
        self.age = age
        self.hunt = hunt
        self.cost = cost

#starter cats
lenny = Cat("lenny", "black", 3, list(range(1,12)), 0)
lizzy = Cat("lizzy", "brown", 3, list(range(5,7)), 0)
phoebe = Cat("phoebe", "white", 3, list(range(3,9)), 0)
smelly_cat = Cat("smelly cat", "brown", "unknown", 0, 0)

#ez lvl cats
cat_one = Cat("snickers", "brown", 12, list(range(1,4)), 0)
cat_two = Cat("noodle", "white", 4, list(range(2,8)), 0)
cat_three = Cat("cake", "brown", 6, list(range(1,6)), 0)

#medium lvl cats
cat_four = Cat("andrew", "black/white", 7, list(range(3,9)), 0)
cat_five = Cat("matty", "grey", 9, list(range(4,7)), 0)
cat_six = Cat("lena", "black", 4, list(range(2,13)), 0)

#difficult lvl cats
cat_seven = Cat("may", "white/brown", 6, list(range(7,13)), 0)
cat_eight = Cat("bastian", "grey", 7, list(range(4,16)), 0)
cat_nine = Cat("ludwig", "red/white", 5, 10, 0)

#very diffuculy lvl cats
cat_ten = Cat("anna", "red/brown", 4, list(range(10,14)), 0)
cat_eleven = Cat("sammy", "white/black", 8, list(range(8,17)), 0)
cat_twelve = Cat("jake", "brown", 3, list(range(11,13)), 0)

#extremely difficult lvl cats
cat_thirteen = Cat("jonny", "black", 13, list(range(1,36)), 0)
cat_fourteen = Cat("maple", "maple", 7, list(range(15,19)), 0)
cat_fifteen = Cat("suzie", "grey", 5, list(range(13,23)), 0)

#insanely difficult lvl cats
cat_sixteen = Cat("buttons", "black", 8, list(range(18,25)), 0)
cat_seventeen = Cat("jakkie", "brown", 7, list(range(15,28)), 0)
cat_eighteen = Cat("georgie", "brown/white", 5, 21, 0)

#catto madness lvl cats
cat_nineteen = Cat("dodie", "white", 4, list(range(28,33)), 0)
cat_twenty = Cat("clark", "black", 7, list(range(25,41)), 0)
cat_twenty_one = Cat("melody", "black/white", 4, list(range(26,38)), 0)

#catto madness return of the cat lvl cats
cat_twenty_two = Cat("april", "red", 6, list(range(32,41)), 0)
cat_twenty_three = Cat("candy", "brown/black", 4, list(range(34,39)), 0)
cat_twenty_four = Cat("snow", "white", 7, list(range(30,43)), 0)

#super special catto cup return of the mad catto's legacy lvl cats
cat_twenty_five = Cat("panzer", "brown", 10, list(range(35,51)), 0)
cat_twenty_six = Cat("princess", "pink", 2, list(range(40,45)), 0)
cat_twenty_seven = Cat("hello-kitty", "white", 4, 42, 0)

#cat-tastic lvl cats
cat_twenty_eight = Cat("buttercup", "yellow", 5, list(range(1,90)), 0)
cat_twenty_nine = Cat("felix", "black/white", 7, list(range(55,65)), 0)
cat_thirty = Cat("marsh-mellow", "white", 4, list(range(45,72)), 0)
cat_thirty_one = Cat("shadow", "black", 9, 62, 0)
cat_thirty_two = Cat("rainbowdash", "rainbow", 8, list(range(50,70)), 0)
cat_thirty_three = Cat("mittens", "red/white", 1, list(range(1,140)), 0)

#cats available in cat store
cat_thirty_four = Cat("djenger", "white/black", 6, list(range(10,16)), 40)
cat_thirty_five = Cat("mimi", "white/black", 6, list(range(8,14)), 30)
cat_thirty_six = Cat("liv", "black/white", 9, list(range(50,71)), 1000)
cat_thirty_seven = Cat("garfield", "red/black", 46, list(range(7,26)), 80)
cat_thirty_eight = Cat("tom", "grey/white", 7, list(range(15,21)), 90)
cat_thirty_nine = Cat("mr.kitty", "grey", 7, list(range(18,28)), 120)
cat_fourty = Cat("talking cat", "grey/white", 8, list(range(22,33)), 150)
cat_fourty_one = Cat("princess carolyn", "pink", 47, list(range(27,39)), 170)

cat_store_list = [cat_thirty_four, cat_thirty_five, cat_thirty_six, cat_thirty_seven, cat_thirty_eight, cat_thirty_nine, cat_fourty, cat_fourty_one]

player_inventory = {
    "gold" : 0,
    "items": [],
    "cats" : []
}

print('''welcome, in this game you will be entering cats in fish catching events.
\nearn money to buy cats and items.
\nthe goal of the game is to beat the cat-tastic cat event.\n''')


starter_cat = input('''please choose your starter cat by typing a, b or c, your options are......\n
a: lenny, lenny is a black cat at the age of three (lenny is a risk taker who rolls 1/11)
b: lizzy, lizzy is a brown cat at the age of three (lizzy likes to play it save and rolls a 5 or 6)
c: phoebe, phoebe is a white cat at the age of three (phoebe is tactical and rolls a solid 3/8)\n''').lower()
if starter_cat == "a":
    player_inventory['cats'] += [lenny]
    print("excelent choice")
elif starter_cat == "b":
    player_inventory['cats'] += [lizzy]
    print("excelent choice")
elif starter_cat == "c":
    player_inventory['cats'] += [phoebe]
    print("excelent choice")
else:
    player_inventory['cats'] += [smelly_cat]
    print("I guess you could not type in a, b or c......\nyour starter cat is now smelly cat (smelly cat always rolls a 0)")

#for x in player_inventory["items"]:
    #if "black collar" in player_inventory["items"]:
        #for c in player_inventory['cats']:
            #if c.color == "black" or c.color == "black/white" or c.color == "white/black":
                #x = len(c.hunt) + 1
                #z = [x, x + 1, x + 2, x + 3, x + 4]
                #c.hunt.extend(z)

start_day()



