"""
This program will simulate a predator/ prey simulation which have differeing genes

Prey/Rabbit Genes:
    - Age
        Threshold: (0<x<40 ticks)
        A set number

    - Mature Age:
        Boolean
        When they exceed a certain age lets say 10 ticks they become an adult
        and can mate

    - Sight
        Threshold: ()
        How far the rabbit can see food or foxes or mates

    - Energy
        ()
        The current energy level of the rabbit. When it hits 0, the rabbit dies

    - Mate Threshold
        ()
        The minimal energy required to start looking for a mate.

    - Movement Distance
        Threshold: ()
        How far the rabbit can move from their current position
        More distance means more energy per jump

    - Bite
        Thresholds:()
        How far a rabbit can bite, will be kept quite short

    - Breeding Cost
        The energy required to produce babies

    - Children
        The amount of children a mate will have. More children means less energy goes
        to all the children

    - Distance to Mate
        A preset distance which can't be changed


Predator/Fox Genes:
    - Age(0<x<40 ticks)
        A predefined number

    - Mature Age:
        Boolean
        When they exceed a certain age lets say 10 ticks they become an adult
        and can mate

    - Sight
        Threshold: ()
        How far the rabbit can see food or foxes or mates

    - Energy
        ()
        The current energy level of the fox. When it hits 0, the rabbit dies

    - Mate Threshold
        ()
        The minimal energy required to start looking for a mate.

    - Movement Distance
        Threshold: ()
        How far the predator can move from their current position

    - Bite
        Thresholds:()
        How far a rabbit can bite, will be kept quite short

    - Breeding Cost
        The energy required to produce babies

    - Children
        The amount of children a mate will have. More children means less energy goes
        to all the children

Characteristics of Prey/Rabbits:
    - Can run from predators?
    - Will actively look for food when energy is below a certain point
    - Will actively look for a mate when they have enough energy


Characteristics of Foxes/Predator:
    - Will chase prey
    - Will look for a mate when energy is enough

How genes are transferred:
    - Taking the average of the genes of the two and then give it a slight mutation
    OR
    - Take a 50/50 coin flip to determine which gene is given to the child
    and then add a slight mutation to the genes

    Maybe make it so plants spawn near other plants


    What data do I want to collect
"""
import tkinter as tk
import random
from RabbitFoxSim.constants import *
import math

# TODO: make a Meat Object for foxes to eat if a rabbit dies
# Helps the foxes have a fighting chance of surviving
class Entity:
    """
    Represent the multiple aspects on the board such as foxes, rabbits and plants
    May have to call entity data through
    """

    def __init__(self, age, sight, energy, mate_energy, move_distance, bite_range, children, breeding_cost, position,
                 gen):
        self._data = {
            "Age": age,
            "Gen": gen,
            "Name": random.choice(RABBIT_NAMES),
            "Mature": False,
            "Sight": sight,
            "WantMate": False,
            "Energy": energy,
            "CoolDown": 3,
            "MateEnergyThreshold": mate_energy,
            "MoveDistance": move_distance,
            "BiteRange": bite_range,
            "Children": children,
            "BreedingCost": breeding_cost,
            "MateRange": 10,
            "Dead": False

        }
        b = self._data["BiteRange"]
        self._position = position
        self._bounding_box = [self._position[0] - b, self._position[1] - b, self._position[0] + b,
                              self._position[1] + b]
        self.want_mate()

    def display(self):
        return "E"

    def is_dead(self):
        if self._data["Energy"] <= 0 or self._data["Age"] >= self.get_max_age():
            self._data["Dead"] = True

    def get_dead(self):
        return self._data["Dead"]

    def get_position(self):
        return self._position

    def get_bounding_box(self):
        return self._bounding_box

    def get_move_distance(self):
        return self._data["MoveDistance"]

    def age(self):
        self._data["Age"] += 1

    def want_mate(self):
        # print(f"{self.get_name()} is seeing if he can mate")
        # print(f"Data: {self.get_age()}, {self.get_energy()}, {self.get_mate_threshold()}, {self.get_cool_down()}, {self._data['Mature']}")
        if self._data["Energy"] > self._data["MateEnergyThreshold"] and self._data["Mature"] and self._data[
            "CoolDown"] <= 0 and not self._data["Dead"]:
            self._data["WantMate"] = True
            # print(f"{self.get_name()} can mate")
        else:
            self._data["WantMate"] = False
            # print(f"{self.get_name()} can't mate")

    def reset_cool_down(self):
        self._data["CoolDown"] = 3

    def decrease_cool_down(self):
        if self._data["CoolDown"] > 0:
            self._data["CoolDown"] -= 1

    def get_mate_threshold(self):
        return self._data["MateEnergyThreshold"]

    def get_cool_down(self):
        return self._data["CoolDown"]

    def check_mate(self):
        return self._data["WantMate"]

    def get_gen(self):
        return self._data["Gen"]

    def get_genes(self):
        return self._data

    def get_name(self):
        return self._data["Name"]

    def get_mate_range(self):
        return self._data["MateRange"]

    def get_age(self):
        return self._data["Age"]

    def get_children(self):
        return self._data["Children"]

    def get_breed_energy(self):
        return self._data["BreedingCost"]

    def get_sight(self):
        return self._data["Sight"]

    def get_energy(self):
        return self._data["Energy"]

    def random_movement(self):
        x_movement = random.randint(-self._data["MoveDistance"], self._data["MoveDistance"])
        y_movement = random.randint(-self._data["MoveDistance"], self._data["MoveDistance"])
        self.move_entity(x_movement, y_movement)

    def get_bite_range(self):
        return self._data["BiteRange"]

    def determine_distance(self, x_distance, y_distance):
        movement = int(math.sqrt((x_distance ** 2) + (y_distance ** 2)))
        return movement

    def move_entity(self, x_movement, y_movement):
        self._position[0] += x_movement
        self._position[1] += y_movement
        if self._position[0] > 1000:
            self._position[0] = 1000

        if self._position[1] > 800:
            self._position[1] = 800

        if self._position[0] < 0:
            self._position[0] = 0

        if self._position[1] < 0:
            self._position[1] = 0

        movement = int((math.sqrt((x_movement ** 2) + (y_movement ** 2))) / 10)
        if movement == 0:
            movement += 1

        self.remove_energy(movement)

        # Do a small check to make sure the entity hasn't run out of energy
        self.is_dead()
        self.reset_boundary_box()

    def get_max_age(self):
        return self._data["MaxAge"]

    def move_towards_entity(self, see_able, lowest_index):
        # Use pythagours to determine direction or maybe not
        plant_pos = see_able[lowest_index].get_position()
        rabbit_pos = self.get_position()
        rabbit_jump = self._data["MoveDistance"]
        x_distance, y_distance = plant_pos[0] - rabbit_pos[0], plant_pos[1] - rabbit_pos[1]

        if abs(x_distance) <= rabbit_jump:
            x_movement = x_distance

        if abs(y_distance) <= rabbit_jump:
            y_movement = y_distance
            #
        if abs(x_distance) > rabbit_jump:
            if x_distance < 0:
                x_movement = -rabbit_jump
            else:
                x_movement = rabbit_jump

        if abs(y_distance) > rabbit_jump:
            if y_distance < 0:
                y_movement = -rabbit_jump
            else:
                y_movement = rabbit_jump

        self.move_entity(x_movement, y_movement)

    def move_away_from_entity(self, see_able, lowest_index):
        """
        Used when a fox is in the see_able range
        :param see_able:
        :param lowest_index:
        :return:
        """
        plant_pos = see_able[lowest_index].get_position()
        rabbit_pos = self.get_position()
        rabbit_jump = self._data["MoveDistance"]
        x_distance, y_distance = plant_pos[0] - rabbit_pos[0], plant_pos[1] - rabbit_pos[1]

        if x_distance < 0:
            x_movement = rabbit_jump
            x_movement -= random.randint(0, 15)
        elif x_distance >= 0:
            x_movement = -rabbit_jump
            x_movement += random.randint(0, 15)

        if y_distance < 0:
            y_movement = rabbit_jump
            y_movement -= random.randint(0, 15)
        elif y_distance >= 0:
            y_movement = -rabbit_jump
            y_movement += random.randint(0, 15)

        self.move_entity(x_movement, y_movement)

    def reset_boundary_box(self):
        b = self._data["BiteRange"]
        self._bounding_box = [self._position[0] - b, self._position[1] - b, self._position[0] + b,
                              self._position[1] + b]

    def add_energy(self, energy):
        self._data["Energy"] += energy

    def remove_energy(self, energy):
        self._data["Energy"] -= energy


class Rabbit(Entity):
    def __init__(self, age, sight, energy, mate_energy, move_distance, bite_range, children, breeding_cost, position,
                 gen):
        super().__init__(age, sight, energy, mate_energy, move_distance, bite_range, children, breeding_cost, position,
                         gen)
        self._data["MaxAge"] = 40

    def mature_check(self):
        if not self._data["Mature"]:
            if self._data["Age"] >= 10:
                # print(f"{self.get_name()} has matured.")
                self._data["Mature"] = True

    def __repr__(self):
        return f"Rabbit({self._data['Name']})"

    def display(self):
        return "R"

    def mate(self, game: 'Board', index):
        # TODO: Review this section for is_dead()
        for indexes, entity in enumerate(game.get_entities()):

            pos1 = self.get_position()
            pos2 = entity.get_position()
            sight = self.get_mate_range()
            x_range, y_range = (pos1[0] - sight, pos1[0] + sight), (pos1[1] - sight, pos1[1] + sight)
            # Make sure it doesn't breed with itself

            if x_range[0] < pos2[0] < x_range[1] and y_range[0] < pos2[1] < y_range[
                1] and entity.display() == "R" \
                    and entity.check_mate() and index == indexes and not entity.get_dead():
                print(f"{self.get_name()} is mating with {entity.get_name()}")
                print(entity.get_cool_down())
                self.reset_cool_down()
                entity.reset_cool_down()
                print(entity.get_cool_down())
                child_choice = random.randint(0, 1)

                #Decide which parent will give its energy
                if child_choice == 0:
                    amount_of_children = self.get_children()
                    energy_using = self.get_breed_energy()
                else:
                    amount_of_children = entity.get_children()
                    energy_using = entity.get_breed_energy()

                self.remove_energy(energy_using)
                entity.remove_energy(energy_using)
                print(f"Having {amount_of_children} kids")
                print(self.get_genes())
                print(entity.get_genes())
                for child in range(amount_of_children):
                    self.make_babies(game, entity, (energy_using / amount_of_children))
                break

    def make_babies(self, game, partner: "Rabbit", energy):
        # age, sight, energy, mate_energy, move_distance, bite_range, children, breeding_cost
        # maybe add mutation rate and breeding
        # TODO: Review this section for mutation rates when added
        rabbit1_genes = [0,
                         self.get_sight(),
                         int(energy),
                         self.get_mate_threshold(),
                         self.get_move_distance(),
                         self.get_bite_range(),
                         self.get_children(),
                         self.get_breed_energy()]

        rabbit2_genes = [0,
                         partner.get_sight(),
                         int(energy),
                         partner.get_mate_threshold(),
                         partner.get_move_distance(),
                         partner.get_bite_range(),
                         partner.get_children(),
                         partner.get_breed_energy()]
        baby_genes = []
        for index, gene_trait in enumerate(rabbit1_genes):
            choice = random.randint(0, 1)
            if choice == 0:
                baby_genes.append(gene_trait)
            else:
                baby_genes.append(rabbit2_genes[index])
        parent1_gen = self.get_gen()
        parent2_gen = partner.get_gen()
        if parent1_gen >= parent2_gen:
            baby_gen = parent1_gen + 1
        else:
            baby_gen = parent2_gen + 1

        my_position = self.get_position()
        baby_position = [random.randint(my_position[0] - 30, my_position[0] + 30), my_position[1] - 30,
                         my_position[1] + 30]
        new_rabbit = Rabbit(baby_genes[0],
                            baby_genes[1],
                            baby_genes[2],
                            baby_genes[3],
                            baby_genes[4],
                            baby_genes[5],
                            baby_genes[6],
                            baby_genes[7],
                            baby_position,
                            baby_gen)
        game.add_entity(new_rabbit)

        print(new_rabbit.get_genes())

    def bite(self, game: "Board", index):
        """
        Occurs when the bunny has moved while looking for food, they then attempt to bite any food in range
        :return:
        """
        # TODO: Make so a plant is labeled as dead=True when bitten
        temp = game.get_entities()
        for indexes, entity in enumerate(temp):

            pos1 = self.get_position()
            pos2 = entity.get_position()
            sight = self.get_bite_range()
            x_range, y_range = (pos1[0] - sight, pos1[0] + sight), (pos1[1] - sight, pos1[1] + sight)
            # Make sure it doesn't eat itself or other rabbits
            # It can only bite a plant within its bite range

            if x_range[0] < pos2[0] < x_range[1] and y_range[0] < pos2[1] < y_range[1] and entity.display() == "P" and \
                    not self.get_dead() and not entity.get_dead():
                # print(x_range[0], x_range[1])
                # print(y_range[0], y_range[1])
                # print(pos1)
                # print(pos2)

                # Make the rabbit bite the food

                print(f"{self.get_name()} Bite Plant")
                print("")
                # make the plant "dead" and unable to be targeted by any other rabbits
                entity.make_dead()
                self.add_energy(20)
                break

    def move(self, game: "Board", self_index):
        """
        Move rabbit, Maybe
        Need to use push back to remove the right index, but to rectify it, it needs to add
        a push back later. When
        :return:
        """
        # Find anything that the rabbit can "see"
        see_able = []
        see_able_display = []
        for index, entity in enumerate(game.get_entities()):

            pos1 = self.get_position()
            pos2 = entity.get_position()
            sight = self.get_sight()
            x_range, y_range = (pos1[0] - sight, pos1[0] + sight), (pos1[1] - sight, pos1[1] + sight)

            if x_range[0] < pos2[0] < x_range[1] and y_range[0] < pos2[1] < y_range[1]:

                # Make sure it isn't looking at itself.
                # When a rabbit dies, anyother rabbits can see themself for the next turn
                if pos2[0] == pos1[0] and pos2[1] == pos1[1] and self_index  == index:
                    continue
                else:
                    # Make the rabbit move towards the food
                    # print(f"{self.get_name()}({self_index-game.get_back_up()}) sees entity {entity.get_name()}({index})")
                    see_able.append(entity)
                    see_able_display.append(entity.display())
        # print(see_able)

        # Check if any entities are edible
        # Create a list which is a display version of see-able
        if "F" in see_able_display:
            print("See Fox")
            # self.random_movement()
            lowest_distance = None
            lowest_index = None
            for index, entity in enumerate(see_able):
                # if entity.display() == "R":
                # print(entity.check_mate(), entity.get_age(), entity.get_energy(), entity.get_genes()["Mature"])
                if entity.display() == "F":
                    plant_pos = entity.get_position()
                    rabbit_pos = self.get_position()

                    x_distance, y_distance = plant_pos[0] - rabbit_pos[0], plant_pos[1] - rabbit_pos[1]
                    distance = int(self.determine_distance(x_distance, y_distance))
                    # print(distance)

                    if lowest_distance is None and entity.display() == "F":
                        lowest_distance = distance
                        lowest_index = index

                    elif lowest_distance is not None and distance < lowest_distance and entity.display() == "F":
                        lowest_distance = distance
                        lowest_index = index

            if lowest_distance is not None:
                # With this set up it means that a rabbit with 55 energy could move far enough to be below 50 energy, but still
                # be able to mate as their status is still available to mate, which for now I shall allow
                self.move_away_from_entity(see_able, lowest_index)

        elif "R" in see_able_display and self.check_mate():
            print("See Rabbit")
            # self.random_movement()
            lowest_distance = None
            lowest_index = None

            for index, entity in enumerate(see_able):
                # if entity.display() == "R":
                # print(entity.check_mate(), entity.get_age(), entity.get_energy(), entity.get_genes()["Mature"])
                if entity.display() == "R" and entity.check_mate() and self.check_mate():
                    plant_pos = entity.get_position()
                    rabbit_pos = self.get_position()

                    x_distance, y_distance = plant_pos[0] - rabbit_pos[0], plant_pos[1] - rabbit_pos[1]
                    distance = int(self.determine_distance(x_distance, y_distance))
                    # print(distance)

                    if lowest_distance is None and entity.display() == "R":
                        lowest_distance = distance
                        lowest_index = index

                    elif lowest_distance is not None and distance < lowest_distance and entity.display() == "R":
                        lowest_distance = distance
                        lowest_index = index

            if lowest_distance is not None:
                # With this set up it means that a rabbit with 55 energy could move far enough to be below 50 energy, but still
                # be able to mate as their status is still available to mate, which for now I shall allow
                self.move_towards_entity(see_able, lowest_index)

                self.mate(game, self_index)

            elif "P" in see_able_display:
                print("Eat plant since rabbit wont mate")
                lowest_distance = None
                lowest_index = None
                for index, entity in enumerate(see_able):
                    plant_pos = entity.get_position()
                    rabbit_pos = self.get_position()

                    x_distance, y_distance = plant_pos[0] - rabbit_pos[0], plant_pos[1] - rabbit_pos[1]
                    distance = int(self.determine_distance(x_distance, y_distance))

                    if lowest_distance is None and entity.display() == "P":
                        lowest_distance = distance
                        lowest_index = index

                    elif lowest_distance is not None and distance < lowest_distance and entity.display() == "P":
                        lowest_distance = distance
                        lowest_index = index

                self.move_towards_entity(see_able, lowest_index)
                self.bite(game, self_index)
            else:
                self.random_movement()

        elif "P" in see_able_display:
            print("See Plant")
            # Remove any entities which are not plants
            lowest_distance = None
            lowest_index = None
            for index, entity in enumerate(see_able):
                plant_pos = entity.get_position()
                rabbit_pos = self.get_position()

                x_distance, y_distance = plant_pos[0] - rabbit_pos[0], plant_pos[1] - rabbit_pos[1]
                distance = int(self.determine_distance(x_distance, y_distance))

                if lowest_distance is None and entity.display() == "P":
                    lowest_distance = distance
                    lowest_index = index

                elif lowest_distance is not None and distance < lowest_distance and entity.display() == "P":
                    lowest_distance = distance
                    lowest_index = index
            """
            plant_pos = see_able[lowest_index].get_position()
            rabbit_pos = self.get_position()
            rabbit_jump = self._data["MoveDistance"]
            x_distance, y_distance = plant_pos[0] - rabbit_pos[0], plant_pos[1] - rabbit_pos[1]

            if abs(x_distance) <= rabbit_jump:
                x_movement = x_distance

            if abs(y_distance) <= rabbit_jump:
                y_movement = y_distance
                #
            if abs(x_distance) > rabbit_jump:
                if x_distance < 0:
                    x_movement = -rabbit_jump
                else:
                    x_movement = rabbit_jump

            if abs(y_distance) > rabbit_jump:
                if y_distance < 0:
                    y_movement = -rabbit_jump
                else:
                    y_movement = rabbit_jump
            """
            # Bite doesn't work as intended here as the location of the
            # Rabbit is not updated before bite is called
            # this may call for a universal movement system for Entities
            self.move_towards_entity(see_able, lowest_index)

            self.bite(game, self_index)
            """
                for entity in see_able:
                    # Currently if plant isn't the first thing in their list of see-able items, it will randomly move
                    # And since the orginal foxes and orginal rabbits were generated before plants, they are always "seen" first and therefore
                    # random movement occurs

                    # Make it so it moves towards the closest plant or rabbit.
                    if entity.display() == "P":
                        plant_pos = entity.get_position()
                        rabbit_pos = self.get_position()
                        rabbit_jump = self._data["MoveDistance"]
                        x_distance, y_distance = plant_pos[0] - rabbit_pos[0], plant_pos[1] - rabbit_pos[1]
                        # print(x_distance, y_distance)
                        # print(self._data["MoveDistance"])

                        # Calculate how far the rabbit will jump
                        if abs(x_distance) <= rabbit_jump:
                            x_movement = x_distance
                        if abs(y_distance) <= rabbit_jump:
                            y_movement = y_distance
                        #
                        if abs(x_distance) > rabbit_jump:
                            if x_distance < 0:
                                x_movement = -rabbit_jump
                            else:
                                x_movement = rabbit_jump

                        if abs(y_distance) > rabbit_jump:
                            if y_distance < 0:
                                y_movement = -rabbit_jump
                            else:
                                y_movement = rabbit_jump
                                # Bite doesn't work as intended here as the location of the
                                # Rabbit is not updated before bite is called
                                # this may call for a universal movement system for Entities
                                # No
                        self.move_entity(x_movement, y_movement)
                        self.bite(game, self_index)
                        break
                    """
        else:
            self.random_movement()

    def step(self, game, index):
        # all the steps above are enacted
        self.is_dead()
        self.decrease_cool_down()
        self.mature_check()
        self.want_mate()
        self.move(game, index)
        self.is_dead()
        self.age()
        self.is_dead()
        self.want_mate()


class Fox(Entity):
    def __init__(self, age, sight, energy, mate_energy, move_distance, bite_range, children, breeding_cost, position,
                 gen):
        super().__init__(age, sight, energy, mate_energy, move_distance, bite_range, children, breeding_cost, position,
                         gen)
        self._data["MaxAge"] = 60

    def age_check(self):
        if not self._data["Mature"]:
            if self._data["Age"] > 10:
                self._data["Mature"] = True

    def __repr__(self):
        return "Fox()"

    def display(self):
        return "F"

    def mature_check(self):
        if not self._data["Mature"]:
            if self._data["Age"] >= 10:
                # print(f"{self.get_name()} has matured.")
                self._data["Mature"] = True

    def bite(self, game: "Board", index):
        """
        Occurs when the bunny has moved while looking for food, they then attempt to bite any food in range
        :return:
        """

        temp = game.get_entities().copy()
        for indexes, entity in enumerate(temp):

            pos1 = self.get_position()
            pos2 = entity.get_position()
            sight = self.get_bite_range()
            x_range, y_range = (pos1[0] - sight, pos1[0] + sight), (pos1[1] - sight, pos1[1] + sight)
            # Make sure it doesn't eat itself or other rabbits

            if x_range[0] < pos2[0] < x_range[1] and y_range[0] < pos2[1] < y_range[1] and entity.display() == "R":
                # print(x_range[0], x_range[1])
                # print(y_range[0], y_range[1])
                # print(pos1)
                # print(pos2)

                # Make the rabbit bite the food

                # TODO: Instead of using back up, use a state of the rabbit. True for not dead, false for dead
                # Dead creatures on that tick won't be able to interact with any other creatures

                print(f"{self.get_name()} Bite Rabbit")
                print("")
                game.remove_entity(indexes)
                self.add_energy(30)
                break

    def mate(self, game, index):

        for indexes, entity in enumerate(game.get_entities()):

            pos1 = self.get_position()
            pos2 = entity.get_position()
            sight = self.get_mate_range()
            x_range, y_range = (pos1[0] - sight, pos1[0] + sight), (pos1[1] - sight, pos1[1] + sight)
            # Make sure it doesn't eat itself or other rabbits
            # Currently they mate with themselves as they try to look
            if x_range[0] < pos2[0] < x_range[1] and y_range[0] < pos2[1] < y_range[
                1] and entity.display() == "F" \
                    and entity.check_mate() and (index - game.get_back_up()) != indexes:

                print(f"{self.get_name()} is mating with {entity.get_name()}")
                print(entity.get_cool_down())

                self.reset_cool_down()
                entity.reset_cool_down()
                print(entity.get_cool_down())

                child_choice = random.randint(0, 1)
                if child_choice == 0:
                    amount_of_children = self.get_children()
                    energy_using = self.get_breed_energy()
                else:
                    amount_of_children = entity.get_children()
                    energy_using = entity.get_breed_energy()

                self.remove_energy(energy_using)
                entity.remove_energy(energy_using)
                print(f"Having {amount_of_children} kids")
                print(self.get_genes())
                print(entity.get_genes())
                for child in range(amount_of_children):
                    self.make_babies(game, entity, (energy_using / amount_of_children))
                break

    def make_babies(self, game, partner: "Fox", energy):
        """
        Allow two foxes to make babies, just copied from rabbits
        :param game:
        :param partner:
        :param energy:
        :return:
        """
        # age, sight, energy, mate_energy, move_distance, bite_range, children, breeding_cost
        rabbit1_genes = [0,
                         self.get_sight(),
                         int(energy),
                         self.get_mate_threshold(),
                         self.get_move_distance(),
                         self.get_bite_range(),
                         self.get_children(),
                         self.get_breed_energy()]

        rabbit2_genes = [0,
                         partner.get_sight(),
                         int(energy),
                         partner.get_mate_threshold(),
                         partner.get_move_distance(),
                         partner.get_bite_range(),
                         partner.get_children(),
                         partner.get_breed_energy()]
        baby_genes = []
        for index, gene_trait in enumerate(rabbit1_genes):
            choice = random.randint(0, 1)
            if choice == 0:
                baby_genes.append(gene_trait)
            else:
                baby_genes.append(rabbit2_genes[index])
        parent1_gen = self.get_gen()
        parent2_gen = partner.get_gen()
        if parent1_gen >= parent2_gen:
            baby_gen = parent1_gen + 1
        else:
            baby_gen = parent2_gen + 1

        my_position = self.get_position()
        baby_position = [random.randint(my_position[0] - 30, my_position[0] + 30), my_position[1] - 30,
                         my_position[1] + 30]
        new_rabbit = Fox(baby_genes[0],
                         baby_genes[1] + random.randint(-5, 5),
                         baby_genes[2],
                         baby_genes[3],
                         baby_genes[4] + random.randint(-5, 5),
                         baby_genes[5] + random.randint(-5, 5),
                         baby_genes[6],
                         baby_genes[7] + random.randint(-5, 5),
                         baby_position,
                         baby_gen)
        game.add_entity(new_rabbit)

        print(new_rabbit.get_genes())

    def move(self, game: "Board", self_index):
        """
        Move rabbit, Maybe
        Need to use push back to remove the right index, but to rectify it, it needs to add
        a push back later. When
        :return:
        """
        # Find anything that the rabbit can "see"
        see_able = []
        see_able_display = []
        for index, entity in enumerate(game.get_entities()):

            pos1 = self.get_position()
            pos2 = entity.get_position()
            sight = self.get_sight()
            x_range, y_range = (pos1[0] - sight, pos1[0] + sight), (pos1[1] - sight, pos1[1] + sight)

            if x_range[0] < pos2[0] < x_range[1] and y_range[0] < pos2[1] < y_range[1]:

                # Make sure it isn't looking at itself.
                # When a rabbit dies, any other rabbits can see themself for the next turn
                if pos2[0] == pos1[0] and pos2[1] == pos1[1] and (self_index - game.get_back_up()) == index:
                    continue
                else:
                    # Make the rabbit move towards the food
                    # print(f"{self.get_name()}({self_index-game.get_back_up()}) sees entity {entity.get_name()}({index})")
                    see_able.append(entity)
                    see_able_display.append(entity.display())
        # print(see_able)

        # Check if any entities are edible
        # Create a list which is a display version of see-able
        if "F" in see_able_display and self.check_mate():
            print("See Rabbit")
            # self.random_movement()
            lowest_distance = None
            lowest_index = None

            for index, entity in enumerate(see_able):
                # if entity.display() == "R":
                # print(entity.check_mate(), entity.get_age(), entity.get_energy(), entity.get_genes()["Mature"])
                if entity.display() == "F" and entity.check_mate() and self.check_mate():
                    plant_pos = entity.get_position()
                    rabbit_pos = self.get_position()

                    x_distance, y_distance = plant_pos[0] - rabbit_pos[0], plant_pos[1] - rabbit_pos[1]
                    distance = int(self.determine_distance(x_distance, y_distance))
                    # print(distance)

                    if lowest_distance is None and entity.display() == "F":
                        lowest_distance = distance
                        lowest_index = index

                    elif lowest_distance is not None and distance < lowest_distance and entity.display() == "F":
                        lowest_distance = distance
                        lowest_index = index

            if lowest_distance is not None:
                # With this set up it means that a rabbit with 55 energy could move far enough to be below 50 energy, but still
                # be able to mate as their status is still available to mate, which for now I shall allow
                self.move_towards_entity(see_able, lowest_index)

                self.mate(game, self_index)

            elif "R" in see_able_display:
                print("Eat Rabbit since fox wont mate")
                lowest_distance = None
                lowest_index = None
                for index, entity in enumerate(see_able):
                    plant_pos = entity.get_position()
                    rabbit_pos = self.get_position()

                    x_distance, y_distance = plant_pos[0] - rabbit_pos[0], plant_pos[1] - rabbit_pos[1]
                    distance = int(self.determine_distance(x_distance, y_distance))

                    if lowest_distance is None and entity.display() == "R":
                        lowest_distance = distance
                        lowest_index = index

                    elif lowest_distance is not None and distance < lowest_distance and entity.display() == "R":
                        lowest_distance = distance
                        lowest_index = index

                self.move_towards_entity(see_able, lowest_index)
                self.bite(game, self_index)
            else:
                self.random_movement()

        elif "R" in see_able_display:
            print("See Rabbit")
            # self.random_movement()
            lowest_distance = None
            lowest_index = None
            for index, entity in enumerate(see_able):
                # if entity.display() == "R":
                # print(entity.check_mate(), entity.get_age(), entity.get_energy(), entity.get_genes()["Mature"])
                if entity.display() == "R":
                    plant_pos = entity.get_position()
                    rabbit_pos = self.get_position()

                    x_distance, y_distance = plant_pos[0] - rabbit_pos[0], plant_pos[1] - rabbit_pos[1]
                    distance = int(self.determine_distance(x_distance, y_distance))
                    # print(distance)

                    if lowest_distance is None and entity.display() == "R":
                        lowest_distance = distance
                        lowest_index = index

                    elif lowest_distance is not None and distance < lowest_distance and entity.display() == "R":
                        lowest_distance = distance
                        lowest_index = index

            if lowest_distance is not None:
                # With this set up it means that a rabbit with 55 energy could move far enough to be below 50 energy, but still
                # be able to mate as their status is still available to mate, which for now I shall allow
                self.move_towards_entity(see_able, lowest_index)
                self.bite(game, self_index)
        else:
            self.random_movement()

    def step(self, game, index):
        self.decrease_cool_down()
        self.mature_check()
        self.want_mate()
        self.move(game, index)
        self.age()
        self.want_mate()


class Plant:
    def __init__(self, position):
        """
        Plants will be able to propagate more plants from them
        Maybe Not
        """
        self._position = position
        self._bounding_box = [self._position[0] - 5, self._position[1] - 5, self._position[0] + 5,
                              self._position[1] + 5]
        self._data = {
            "Age": 0,
            "Energy": 10,
            "Name": "Plant",
            "Dead": False
        }

    def display(self):
        return "P"

    def get_position(self):
        return self._position

    def get_bounding_box(self):
        return self._bounding_box

    def get_name(self):
        return self._data["Name"]

    def get_dead(self):
        return self._data["Dead"]

    def make_dead(self):
        self._data["Dead"] = True

    def want_mate(self):
        pass

    def is_dead(self):
        # Used as it is technically not an entity but this still gets run against it.
        pass

    def move_entity(self):

        if self._position[0] > 1000:
            self._position[0] = 1000

        if self._position[1] > 800:
            self._position[1] = 800

        if self._position[0] < 0:
            self._position[0] = 0

        if self._position[1] < 0:
            self._position[1] = 0

    def step(self, game, index):
        """
        Maybe have plants create more plants around them.
        Scrap this idea, just make plants spawn randomly over the screen rather than gathereing in one spot
        to keep the rabbits moving around. Maybe have reproducing grasses up to 100 grasses with only a one in onehundred chance of reproducing
        :param game:
        :param index:
        :return:
        """
        """
        entities = game.display_entities()

        plants = entities.count("P")

        if plants < 100:
            upper_limit = 99

        else:
            upper_limit = "Stop"

        if upper_limit != "Stop":
            choice = random.randint(0, upper_limit)
            if choice == 0:
                # print(f"Plant({index-game.get_back_up()})")
                p = Plant([random.randint(self._position[0]-50, self._position[0]+50), random.randint(self._position[1]-50, self._position[1]+50)])
                p.move_entity()
                game.add_entity(p)
        else:
            pass
        """
        pass

    def get_age(self):
        return self._data["Age"]

    def get_energy(self):
        return self._data["Energy"]


class Board(tk.Canvas):
    """
    Next step is data collection and gene mutations
    """

    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)
        self._entities = []
        self._index_to_back = []

        self._step = 0
        self._collected_data = {}
        for rabbit in range(RABBIT_COUNT):
            r = create_rabbit()
            new_rabbit = Rabbit(r["Age"],
                                r["Sight"],
                                r["Energy"],
                                r["MateEnergyThreshold"],
                                r["MoveDistance"],
                                r["BiteRange"],
                                r["Children"],
                                r["BreedingCost"],
                                r["Position"],
                                0)  # Gen
            self._entities.append(new_rabbit)

        for fox in range(FOX_COUNT):
            f = create_fox()
            new_fox = Fox(f["Age"],
                          f["Sight"],
                          f["Energy"],
                          f["MateEnergyThreshold"],
                          f["MoveDistance"],
                          f["BiteRange"],
                          f["Children"],
                          f["BreedingCost"],
                          f["Position"],
                          0)
            self._entities.append(new_fox)

        for plant in range(PLANT_COUNT):
            p = Plant([random.randint(X_MIN, X_MAX), random.randint(Y_MIN, Y_MAX)])
            self._entities.append(p)
        self.draw_board()
        self.step()


    def remove_entity(self, index):
        self._entities.pop(index)

    def add_entity(self, entity):
        self._entities.append(entity)

    def increment_step(self):
        self._step += 1



    def display_entities(self):
        display = []
        for entity in self._entities:
            display.append(entity.display())
        return display

    def construct_fox(self):
        pass

    def get_index(self):
        return self._index_to_back

    def refresh_index_to_back_up(self):
        self._index_to_back = []

    def add_index(self, index):
        self._index_to_back.append(index)

    def draw_board(self):
        """
        Will delete and redraw all items in the canvas
        :return:
        """
        self.delete(tk.ALL)
        for entity in self._entities:
            placeholder = entity.get_position()
            pos = entity.get_bounding_box()
            if entity.display() == "F":
                if entity.check_mate() and entity.get_cool_down() <= 0:
                    self.create_rectangle(pos[0], pos[1], pos[2], pos[3], fill="blue")
                else:
                    self.create_rectangle(pos[0], pos[1], pos[2], pos[3], fill="red")
                self.create_text(placeholder[0], placeholder[1], text=str(entity.get_cool_down()), fill="white")
                self.create_text(placeholder[0], placeholder[1] + 50, text=str(entity.get_age()))
                self.create_text(placeholder[0], placeholder[1] + 25, text=str(entity.get_energy()))
                self.create_text(placeholder[0], placeholder[1] - 25, text=str(entity.get_name()))
                self.create_text(placeholder[0], placeholder[1] - 50, text=f"Gen {entity.get_gen()}")
            elif entity.display() == "R":
                if entity.check_mate() and entity.get_cool_down() <= 0:

                    self.create_rectangle(pos[0], pos[1], pos[2], pos[3], fill="black")
                    self.create_text(placeholder[0], placeholder[1], text=str(entity.get_cool_down()), fill="white")
                else:

                    self.create_rectangle(pos[0], pos[1], pos[2], pos[3], fill="grey")
                    self.create_text(placeholder[0], placeholder[1], text=str(entity.get_cool_down()))
                self.create_text(placeholder[0], placeholder[1] + 50, text=str(entity.get_age()))
                self.create_text(placeholder[0], placeholder[1] + 25, text=str(entity.get_energy()))
                self.create_text(placeholder[0], placeholder[1] - 25, text=str(entity.get_name()))
                self.create_text(placeholder[0], placeholder[1] - 50, text=f"Gen {entity.get_gen()}")
            elif entity.display() == "P":
                self.create_rectangle(pos[0], pos[1], pos[2], pos[3], fill="green")
            # Display the entities age

    def step(self):
        """
        Call the step function of every entity and also call the step function of every entity
        :return:
        # maybe a check status for the entity
        """
        # self._back_up resets each step
        print(f"Step: {self._step}")
        next_board = []

        # Go through all entities on the board
        self.refresh_index_to_back_up()
        # make it so it just
        for index, entity in enumerate(self._entities):
            # print(self._index_to_back)
            # print(self.get_entities())
            # Check if entity wants to mate
            # print()
            # print(self._entities, index, index-self._back_up)
            # print(f"Back_up called on index: {index}")

            entity.step(self, index)
            entity.is_dead()

        for entity in self._entities:
            if not entity.get_dead():
                next_board.append(entity)

        self.set_entities(next_board)
        for plant in range(8):
            p = Plant([random.randint(X_MIN, X_MAX), random.randint(Y_MIN, Y_MAX)])
            self.add_entity(p)
        self.draw_board()
        """
        # Used for visualising sight lines for testing
        for index1, entity in enumerate(self.get_entities()):
            for index2, entity2 in enumerate(self.get_entities()):
                if entity.display() == "P" or index1 == index2:
                    continue
                else:
                    pos1 = entity2.get_position()
                    pos2 = entity.get_position()
                    sight = entity.get_sight()
                    x_range, y_range = (pos2[0] - sight, pos2[0] + sight), (pos2[1] - sight, pos2[1] + sight)
                    if x_range[0] < pos1[0] < x_range[1] and y_range[0] < pos1[1] < y_range[1]:
                        self.create_line(pos1[0], pos1[1], pos2[0], pos2[1])"""

        self.increment_step()
        self.after(100, self.step)

    def collect_data(self):
        # Meant to collect data of simulation
        pass

    def age_check(self, entity: Entity, index):
        """
        Checks all entities haven't exceeded their maximum age then kills them
        :param entity:
        :param index:
        :return:
        """

        if entity.display() != "P":
            entity__max_age = entity.get_max_age()
            if entity.get_age() > entity__max_age:
                print(f"{entity.get_name()} died of old age.")


    def energy_check(self, entity, index):
        """
        Kills entities when their energy has gone below zero
        :param entity:
        :param index:
        :return:
        """

        if entity.get_energy() <= 0:
            print(f"{entity.get_name()} died of starvation.")
            self._entities.pop(index)


    def get_entities(self):
        return self._entities

    def set_entities(self, new_entities):
        self._entities = new_entities


class App:
    def __init__(self, root):
        self._root = root

        self._board = Board(root, bg="brown", highlightthickness=0)
        self._board.pack(expand=True, fill=tk.BOTH)


def main():
    root = tk.Tk()
    root.geometry("1000x800")
    app = App(root)
    root.mainloop()


if __name__ == "__main__":
    main()
# TODO: Go through every part of Fox, Rabbit and plant and make sure is_dead appears
# When rabbit eats a plant  set "Dead" True