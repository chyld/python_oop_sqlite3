import random
import sqlite3


class Dog:
    def __init__(self, _id, name, age, sex, energy, farm_id):
        self._id = _id
        self.name = name
        self.age = age
        self.sex = sex
        self.energy = energy
        self.farm_id = farm_id

    @staticmethod
    def find(dbname):
        puppies = []
        conn = sqlite3.connect(dbname)
        cur = conn.cursor()
        for row in cur.execute('select * from dogs'):
            puppy = Dog(*row)
            puppies.append(puppy)
        conn.commit()
        conn.close()
        return puppies

    @staticmethod
    def find_by_id(dbname, id):
        conn = sqlite3.connect(dbname)
        cur = conn.cursor()
        for row in cur.execute('select * from dogs where id = {}'.format(id)):
            puppy = Dog(*row)
        conn.commit()
        conn.close()
        return puppy

    @staticmethod
    def find_by_farm_id(dbname, farm_id):
        puppies = []
        conn = sqlite3.connect(dbname)
        cur = conn.cursor()
        for row in cur.execute('select * from dogs where farm_id = {}'.format(farm_id)):
            puppy = Dog(*row)
            puppies.append(puppy)
        conn.commit()
        conn.close()
        return puppies

    def bark(self):
        return "woof! my name is {}".format(self.name)

    def play(self):
        if self.energy < 20:
            print("{} is too tired to play".format(self.name))
            self.rest()
            return
        expended = random.randrange(5, 20)
        self.energy -= expended

    def rest(self):
        gained = random.randrange(1, 7)
        self.energy += gained

    def __str__(self):
        return "{} - {} : woof! i am {} energy is {}".format(self._id, self.farm_id, self.name, self.energy)

    def __repr__(self):
        return self.__str__()
