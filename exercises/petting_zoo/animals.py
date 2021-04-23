from Ball_python import Ball_python
from Capybara import Capybara
from Coi import Coi
from Cottonmouth import Cottonmouth
from Cow import Cow
from Donkey import Donkey
from Eastern_diamond_back import Eastern_diamond_back
from Goat import Goat
from Goldfish import Goldfish
from Hognose_snake import Hognose_snake
from Kingsnake import Kingsnake
from Llama import Llama
from Mallard import Mallard
from Red_eared_slider import Red_eared_slider
from Wallaby import Wallaby

gary = Goldfish("Gary", "Goldfish")
christian = Coi("Christian", "Coi")
marvin = Mallard("Marvin", "Mallard")
carl = Capybara("Carl", "Capybara")
reed = Red_eared_slider("Reed", "Read Eared Slider")
kristin = Kingsnake("Kristin", "Kingsnake")
boyd = Ball_python("Boyd", "Ball Python")
everett = Eastern_diamond_back("Everett", "Eastern Diamond Back")
holly = Hognose_snake("Holly", "Hognose Snake")
cynthia = Cottonmouth("Cynthia", "Cottonmouth")
georgia = Goat("Georgia", "Goat")
dan = Donkey("Dan", "Donkey")
chase = Cow("Chase", "Cow")
larry = Llama("Larry", "Llama")
whitney = Wallaby("Whitney", "Walaby")


all_animals = [gary, christian, marvin, carl, reed, kristin, boyd, everett, holly, cynthia, georgia, dan, chase, larry, whitney ]

for animal in all_animals:
    print(animal.name)