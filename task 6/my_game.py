"""
This module contains classes for game
"""
class Item:
    """
    a class for Item
    """
    def __init__(self,name) -> None:
        """
        book = Item("book")
        book.name
        book
        """
        self.name = name
        self.description = ""

    def set_description(self,description):
        """
        gets the description of the item
        """
        self.description = description

    def describe(self):
        """
        describes the item
        >>> cheese = Item("cheese")
        >>> cheese.set_description("A large and smelly block of cheese")
        >>> cheese.describe()
        A large and smelly block of cheese
        """
        print(f"The [{self.name}] is here - {self.description}")

    def get_name(self):
        """
        gets the name of the item
        """
        return self.name

class Weapon(Item):
    """
    a class Weapon
    """

class Gift(Item):
    """
    a class for gift
    """

class Support(Item):
    """
    a class for support item
    """

class Character:
    """
    a class for enemy
    """
    defeats_count = 0
    def __init__(self,name,description) -> None:
        """
        >>> dave = Enemy("Dave", "A smelly zombie")
        >>> dave.description
        'A smelly zombie'
        """
        self.name = name
        self.description = description
        self.string = ""
        self.weakness = ""

    def set_conversation(self,string):
        """
        adds a string for a conversation
        >>> dave = Enemy("Dave", "A smelly zombie")
        >>> dave.set_conversation("What's up, dude! I'm hungry.")
        """
        self.string = string

    def set_weakness(self,weakness):
        """
        set a weakness of an enemy
        """
        self.weakness = weakness

    def describe(self):
        """
        describes enemy
        >>> dave = Enemy("Dave", "A smelly zombie")
        >>> dave.set_weakness("cheese")
        """
        print(f'{self.name} is here!' + '\n' + self.description)

    def talk(self):
        """
        returns a string of conversation
        >>> dave = Enemy("Dave", "A smelly zombie")
        >>> dave.set_conversation("What's up, dude! I'm hungry.")
        >>> dave.talk()
        What's up, dude! I'm hungry.
        """
        print(f"[{self.name} says]: {self.string}")

    def fight(self,fight_with):
        """
        fights an enemy with given item
        >>> dave = Enemy("Dave", "A smelly zombie")
        >>> dave.set_weakness("cheese")
        >>> dave.fight('cheese')
        True
        """
        if fight_with in self.weakness:
            Character.defeats_count += 1
            print(f"You've defeted {self.name}")
            return True
        return False

    def get_defeated(self):
        """
        counts how many times an enemy was defeated
        """
        return Character.defeats_count

class Enemy(Character):
    """
    a class for enemy
    """

class Friend(Character):
    """
    a class for friend
    """
    def __init__(self, name, description) -> None:
        super().__init__(name, description)
        self.item = None

    def set_item(self,item):
        """
        sets item
        """
        self.item = item

    def give(self):
        """
        give an item
        """
        return self.item

class Street:
    """
    a class for rooms
    """
    def __init__(self,name) -> None:
        """
        >>> kitchen = Room("Kitchen")
        >>> kitchen.room
        'Kitchen'
        """
        self.name = name
        self.direction = []
        self.description = ""
        self.character = None
        self.item = None

    def set_description(self,description):
        """
        gives a description
        >>> kitchen = Room("Kitchen")
        >>> kitchen.set_description("A dank and dirty room buzzing with flies.")
        """
        self.description = description

    def link_street(self,street,direction):
        """
        links two rooms by directions
        >>> kitchen = Room("Kitchen")
        >>> kitchen.set_description("A dank and dirty room buzzing with flies.")
        >>> dining_hall = Room("Dining Hall")
        >>> kitchen.link_room(dining_hall, "south")
        """
        self.direction.append([direction,street])

    def set_character(self,character):
        """
        sets a character into the room
        """
        self.character = character

    def set_item(self,item):
        """
        sets an item into the room
        """
        self.item = item

    def get_character(self):
        """
        gets a charactes from the room
        """
        return self.character

    def get_item(self):
        """
        gets an item from the room
        """
        return self.item

    def get_details(self):
        """
        prints an information about the room
        >>> kitchen = Room("Kitchen")
        >>> kitchen.set_description("A dank and dirty room buzzing with flies.")
        >>> kitchen.get_details()
        Kitchen
        A dank and dirty room buzzing with flies.
        """
        direc = ''
        for i in self.direction:
            direc += '\n'+f'The {i[1].name} is {i[0]}'
        print(self.name + '\n'+ '--------------------'+'\n' + self.description\
         + direc)

    def move(self,direction):
        """
        moves to another room
        """
        for i in self.direction:
            if direction in i:
                return i[1]
        return self
