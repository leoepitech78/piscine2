class Competition:
    def __init__(self, name):
        self.__name = name
        self.__athletes = []

    def add_athlete(self, athlete):
        self.__athletes.append(athlete)

    def exclude(self, athlete):
        if athlete in self.__athletes:
            self.__athletes.remove(athlete)

    def rank(self, athlete, ranking):
        athlete.add_record(f"{self.__name}", ranking)

def get_ranking(self):
    ranked_athletes = sorted(self.__athletes, key=lambda x: x.get_record(self.__name))
    result = "---- COMPETITION\nHere is the {0} ranking:".format(self.__name)
    for i, athlete in enumerate(ranked_athletes, start=1):
            print(f"{i}st: {athlete.getName()} ({athlete.getBirthdate()}) from {athlete.getCountry()}")

class Athlete:
    def __init__(self, name, country, birthdate):
        self.__name = name
        self.__country = country
        self.__birthdate = birthdate
        self.__records = {}

    def add_record(self, championship, ranking):
        self.__records[championship] = ranking

    def print(self):
        print("---- ATHLETE")
        print(f"My name is {self.__name}, from {self.__country}.")
        print(f"My birth date is {self.__birthdate}.")
        if self.__records:
            print("Here is my ranking:")
            for championship, ranking in self.__records.items():
                print(f"{ranking} at the {championship}")

    def getName(self):
        return self.__name

    def getCountry(self):
        return self.__country

    def getBirthdate(self):
        return self.__birthdate

    def get_record(self, championship):
        return self.__records.get(championship, None)
