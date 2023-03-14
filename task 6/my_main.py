"""
my game
"""
import my_game
kozelnytska = my_game.Street("вулиця Козельницька")
kozelnytska.set_description("Вулиця де знаходиться УКУ.")

stryiska = my_game.Street("вулиця Стрийська")
stryiska.set_description("Вулиця біля парку.")

franka = my_game.Street("вулиця Івана Франка")
franka.set_description("Довга вуличка, яка веде до центру.")

shevchenka = my_game.Street("проспект Шевченка")
shevchenka.set_description("Проспект з гарною доріжкою по середині.")

kozelnytska.link_street(stryiska, "west")
kozelnytska.link_street(franka, "east")
stryiska.link_street(kozelnytska, "east")
franka.link_street(kozelnytska, "west")
stryiska.link_street(shevchenka, "north")
franka.link_street(shevchenka, "north")
shevchenka.link_street(stryiska, "west")
shevchenka.link_street(franka, "south")

roma = my_game.Enemy("Роман", "чоловік в не тверезому стані")
roma.set_conversation("Кис кис кис")
roma.set_weakness(["бита","перцовий балончик","книжка"])
stryiska.set_character(roma)

vasyl = my_game.Enemy("Василь", "Негідник, розбійник, грабіжник")
vasyl.set_conversation("Віддавай все що маєш")
vasyl.set_weakness("бита")
shevchenka.set_character(vasyl)

sasha = my_game.Friend("Саша", "Ваш друг")
sasha.set_conversation("Ось тобі подарок!")
kozelnytska.set_character(sasha)

balonchik = my_game.Weapon("перцовий балончик")
balonchik.set_description("Балончик, яким можна захиститись")
shevchenka.set_item(balonchik)

bita = my_game.Weapon("бита")
bita.set_description("Бейзбольна бита")
franka.set_item(bita)

aid = my_game.Support("аптечка")
aid.set_description("Для вилікування після нанесення удару")
stryiska.set_item(aid)

book = my_game.Gift("книжка")
book.set_description("Товста книга Стівена Кінга")
sasha.set_item(book)

current_street = kozelnytska
backpack = []


dead = False

while dead == False:

    print("\n")
    current_street.get_details()

    inhabitant = current_street.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    item = current_street.get_item()
    if item is not None:
        item.describe()

    command = input("> ")

    if command in ["north", "south", "east", "west"]:
        current_street = current_street.move(command)
    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()
        if inhabitant == sasha:
            print(inhabitant.give().description)
            print(f'{inhabitant.give().get_name()} is in your backpack')
            backpack.append(inhabitant.give().get_name())

    elif command == "fight":
        if inhabitant == sasha:
            print("You can't fight your friend")
        elif inhabitant is not None:
            print("What will you fight with?")
            fight_with = input()

            if fight_with in backpack:

                if inhabitant.fight(fight_with) == True:
                    print("Hooray, you won the fight!")
                    current_street.character = None
                    if inhabitant.get_defeated() == 2:
                        print("Congratulations, you have vanquished the enemy horde!")
                        dead = True
                else:
                    if inhabitant == vasyl:
                        print(f"Oh dear, you lost the fight, {fight_with} didn't help"+"\n"+\
                        'You can heal by printing heal if you have an aid')
                        heal = input('> ')
                        if heal == 'heal' and aid.get_name() in backpack:
                            print('You are healed')
                        else:
                            print("Oh dear, you lost the fight.")
                            print("That's the end of the game")
                            dead = True
                    else:
                        print("Oh dear, you lost the fight.")
                        print("That's the end of the game")
                        dead = True
            else:
                print("You don't have a " + fight_with)
        else:
            print("There is no one here to fight with")
    elif command == "take":
        if item is not None:
            print("You put the " + item.get_name() + " in your backpack")
            backpack.append(item.get_name())
            current_street.set_item(None)
        else:
            print("There's nothing here to take!")
    else:
        print("I don't know how to " + command)
