# Assignment 3 - Introduction to Programming 2 (Python OOP)
# Magical Academy Creatures & Potions
# OOP Concepts: Inheritance, Polymorphism, Association

import random
# =========================
# CREATURE (PARENT CLASS)
# =========================

class Creature:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.potion = None

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} took {damage} damage!")

    def is_alive(self):
        return self.health > 0

    # Polymorphism (must override)
    def attack(self):
        raise NotImplementedError("Each creature must implement its own attack method")

    # Association with Potion
    def drink_potion(self, potion):
        self.potion = potion
        self.health += potion.potency
        potion.use()
        print(f"{self.name} gained {potion.potency} health!")


# =========================
# DRAGON CLASS
# =========================

class Dragon(Creature):
    def __init__(self, name, fire_power):
        super().__init__(name)
        self.fire_power = fire_power

    def take_damage(self, damage):
        if self.fire_power > 30:
            damage -= 10

        if damage < 0:
            damage = 0

        self.health -= damage
        print(f"{self.name} blocked some damage!")
        print(f"{self.name} took {damage} damage!")

    def attack(self):
        damage = self.fire_power
        print(f"{self.name} breathes fire for {damage} damage!")
        return damage


# =========================
# UNICORN CLASS
# =========================

class Unicorn(Creature):
    def __init__(self, name, heal_amount):
        super().__init__(name)
        self.heal_amount = heal_amount

    def heal(self):
        self.health += self.heal_amount
        print(f"{self.name} healed for {self.heal_amount} health!")

    def attack(self):
        damage = 10
        print(f"{self.name} uses magic light attack for {damage} damage!")
        return damage


# =========================
# PHOENIX CLASS
# =========================

class Phoenix(Creature):
    def __init__(self, name, flame_health):
        super().__init__(name)
        self.flame_health = flame_health
        self.revived = False  # FIX: prevents infinite revival

    def attack(self):
        damage = random.randint(5, self.flame_health)
        print(f"{self.name} bursts into flames for {damage} damage!")
        return damage

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} took {damage} damage!")

        if self.health <= 0 and not self.revived:
            self.health = 50
            self.revived = True
            print(f"{self.name} revived from ashes!")


# =========================
# MAGIC POTION CLASS
# =========================

class MagicPotion:
    def __init__(self, name, effect, potency):
        self.name = name
        self.effect = effect
        self.potency = potency

    def use(self):
        print(f"{self.name} used! Effect: {self.effect}")


# =========================
# BATTLE CLASS
# =========================

class Battle:
    def __init__(self, creature1, creature2):
        self.creature1 = creature1
        self.creature2 = creature2

    def fight_rounds(self, rounds):

        for i in range(rounds):
            print(f"\n--- ROUND {i+1} ---")

            # OPTIONAL HEALING (IMPROVEMENT)
            if isinstance(self.creature1, Unicorn):
                self.creature1.heal()

            if isinstance(self.creature2, Unicorn):
                self.creature2.heal()

            # Creature 1 attacks
            dmg1 = self.creature1.attack()
            self.creature2.take_damage(dmg1)

            if not self.creature2.is_alive():
                print(f"{self.creature2.name} has died!")
                print("Battle Over!")
                break

            # Creature 2 attacks
            dmg2 = self.creature2.attack()
            self.creature1.take_damage(dmg2)

            if not self.creature1.is_alive():
                print(f"{self.creature1.name} has died!")
                print("Battle Over!")
                break

            print(f"{self.creature1.name} HP: {self.creature1.health}")
            print(f"{self.creature2.name} HP: {self.creature2.health}")
            print("---------------------")


# =========================
# TESTING SECTION
# =========================

dragon = Dragon("Smaug", 50)
unicorn = Unicorn("Sparkle", 25)
phoenix = Phoenix("Flare", 30)

# Potion test (FIXED: multiple creatures use potion)
potion = MagicPotion("Healing Potion", "Restores Health", 20)

dragon.drink_potion(potion)
unicorn.drink_potion(potion)
phoenix.drink_potion(potion)

print("\n--- POLYMORPHISM TEST ---")
creatures = [dragon, unicorn, phoenix]

for c in creatures:
    c.attack()

print("\n--- BATTLE TEST ---")
battle = Battle(dragon, phoenix)
battle.fight_rounds(3)