import random


RABBIT_COUNT = 30
FOX_COUNT = 3
PLANT_COUNT = 100
X_MIN, X_MAX = 100, 900
Y_MIN, Y_MAX = 100, 700

RABBIT_NAMES = ["Jeff", "Liam", "Apple", "Steve", "Coraline", "Peter", "Craig", "Aiden", "Bezos", "Bill", "Freddy", "Bonny", "Rhys", "Davey", "Micheal", "Trump", "Biden", "Joe", "Chris", "Tyler"]

def create_rabbit():
    RABBIT_DETAILS = {
        "Age": random.randint(0, 30),
        "Mature": False,
        "Sight": random.randint(70, 180),
        "Energy": random.randint(20, 50),
        "MateEnergyThreshold": 45,
        "MoveDistance": random.randint(25, 75),
        "BiteRange": random.randint(10, 20),
        "Children": random.randint(1, 4),
        "BreedingCost": random.randint(10, 40),
        "Position": [random.randint(X_MIN, X_MAX), random.randint(Y_MIN, Y_MAX)],
        "Gen": 0,
        "MutationRate": 5
    }
    return RABBIT_DETAILS


def create_fox():
    FOX_DETAILS = {
        "Age": random.randint(0, 15),
        "Mature": False,
        "Sight": random.randint(100, 130),
        "Energy": random.randint(40, 60),
        "MateEnergyThreshold": 50,
        "MoveDistance": random.randint(50, 100),
        "BiteRange": random.randint(20, 23),
        "Children": random.randint(1, 2),
        "BreedingCost": random.randint(10, 40),
        "Position": [random.randint(X_MIN, X_MAX), random.randint(Y_MIN, Y_MAX)],
        "Gen": 0
    }
    return FOX_DETAILS



