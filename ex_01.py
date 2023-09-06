class Athlete:
    def __init__(self, name, country, birthdate):
        self.name = name
        self.country = country
        self.birthdate = birthdate
        self.records = {}

    def add_record(self, championship, ranking):
        self.records[championship] = ranking

    def print(self):
        print("---- ATHLETE")
        print(f"My name is {self.name}, from {self.country}.")
        print(f"My birth date is {self.birthdate}.")
        if self.records:
            print("Here is my ranking:")
            for championship, ranking in self.records.items():
                print(f"{ranking} at the {championship}")

# Test the Athlete class
if __name__ == '__main__':
    bob = Athlete('Bobby Bob', 'Bolivia', '1998-09-09')
    bob.print()

    bob.add_record('2020 La Paz Championship', '2nd')
    bob.print()
