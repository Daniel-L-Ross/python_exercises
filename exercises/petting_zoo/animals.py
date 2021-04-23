from datetime import date
from os import wait

class Goldfish():
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.swimming = True
        self.date_added = date.today()

class Coi():
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.swimming = True
        self.date_added = date.today()

class Mallard():
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.swimming = True
        self.date_added = date.today()

class Capybara():
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.swimming = True
        self.date_added = date.today()

class Red_eared_slider():
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.swimming = True
        self.date_added = date.today()

class Kingsnake():
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.slithering = True
        self.date_added = date.today()

class Ball_python():
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.slithering = True
        self.date_added = date.today()

class Eastern_diamond_back():
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.slithering = True
        self.date_added = date.today()

class Hognose_snake():
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.slithering = True
        self.date_added = date.today()

class Cottonmouth():
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.slithering = True
        self.date_added = date.today()

class Goat():
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.walking = True
        self.date_added = date.today()

class Donkey():
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.walking = True
        self.date_added = date.today()

class Cow():
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.walking = True
        self.date_added = date.today()

class Llama():
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.walking = True
        self.date_added = date.today()

class Wallaby():
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.walking = True
        self.date_added = date.today()

gary = Goldfish("Gary", "Goldfish")
christian = Coi("Christian", "Coi")
marvin = Mallard("Marvin", "Mallard")
carl = Capybara("Carl", "Capybara")
reed = Red_eared_slider("Reed", "Read Eared Slider")
kristin = Kingsnake("Kristin", "Kingsnake")
boyd = Ball_python("Boyd", "Ball Python")
everett = Eastern_diamond_back("Everett", "Eastern Diamond Back")
holly = Hognose_snake()
cynthia = Cottonmouth()
georgia = Goat()
dan = Donkey()
chase = Cow()
larry = Llama()
whitney = Wallaby()


all_animals = [gary, christian, marvin, carl, reed, kristin, boyd, everett, holly, cynthia, georgia, dan, chase, larry, whitney ]

