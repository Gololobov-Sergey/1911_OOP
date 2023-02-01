import random


class Human:
    def __init__(self, name, house=None, car=None, job=None):
        self.name = name
        self.house = house
        self.car = car
        self.job = job
        self.money = 100
        self.gladness = 50
        self.satiety = 50


brand_of_cars = {"BMW": {"fuel": 100, "strength": 100, "consumption": 6},
                 "Audi": {"fuel": 80, "strength": 80, "consumption": 7},
                 "Mercedes": {"fuel": 100, "strength": 90, "consumption": 5},
                 "Запорожець": {"fuel": 50, "strength": 50, "consumption": 8}}


class Car:
    def __init__(self, brand_of_cars):
        self.brand = random.choice(list(brand_of_cars))
        # пальне
        self.fuel = brand_of_cars[self.brand]["fuel"]
        # амортизація
        self.strength = brand_of_cars[self.brand]["strength"]
        # витрати пального
        self.consumption = brand_of_cars[self.brand]["consumption"]

    def drive(self):
        pass


class House:
    def __init__(self):
        # наявність їжи
        self.food = 0
        # забрудненність
        self.mess = 0


job_list = {"Розробник на Python": {"salary": 100, "gladness_less": 10},
            "Викладач в академії": {"salary": 80, "gladness_less": 2},
            "Водій": {"salary": 60, "gladness_less": 5},
            "Продавець": {"salary": 50, "gladness_less": 8}}


class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness_less = job_list[self.job]["gladness_less"]
