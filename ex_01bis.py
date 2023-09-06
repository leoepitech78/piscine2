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
