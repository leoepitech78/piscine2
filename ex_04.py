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

    def getName(self):
        return self.__name

    def getCountry(self):
        return self.__country

    def getBirthdate(self):
        return self.__birthdate

    def get_record(self, championship):
        return self.__records.get(championship, None)

class FighterAthlete(Athlete):
    def __init__(self, name, country, birthdate, wins, draws, losses):
        super().__init__(name, country, birthdate)
        self.__wins = wins
        self.__draws = draws
        self.__losses = losses

    def print(self):
        print("------------ FIGHTER")
        super().print()
        print(f"I fought {self.__wins + self.__draws + self.__losses} times with a {self.__wins}/{self.__draws}/{self.__losses} record.")

class MMAFighterAthlete(FighterAthlete):
    def __init__(self, name, country, birthdate, wins, draws, losses, organizations):
        super().__init__(name, country, birthdate, wins, draws, losses)
        self.__organizations = organizations

    def print(self):
        print("------------ MMA")
        super().print()
        print("I fought in the following organizations:", ', '.join(self.__organizations))

class SoccerAthlete(Athlete):
    def __init__(self, name, country, birthdate, team, place):
        super().__init__(name, country, birthdate)
        self.__team = team
        self.__place = place

    def print(self):
        print("-------- SOCCER")
        super().print()
        print("Here is my record:")
        for championship, ranking in self._Athlete__records.items():
            print(f"{ranking} at the {championship}")
        print(f"I play as a {self.__place} in {self.__team}.")
