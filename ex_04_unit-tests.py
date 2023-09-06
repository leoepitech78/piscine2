import unittest
from ex_04 import Athlete, FighterAthlete, MMAFighterAthlete, SoccerAthlete

class TestAthleteSubclasses(unittest.TestCase):
    
    def test_athlete(self):
        bob = Athlete('Bobby Bob', 'Bolivia', '1998-09-09')
        self.assertEqual(bob.getName(), 'Bobby Bob')
        self.assertEqual(bob.getCountry(), 'Bolivia')
        self.assertEqual(bob.getBirthdate(), '1998-09-09')

    def test_fighter_athlete(self):
        john = FighterAthlete('Johny John', 'Jordan', '1976-03-17', 4, 0, 1)
        self.assertEqual(john.getName(), 'Johny John')
        self.assertEqual(john.getCountry(), 'Jordan')
        self.assertEqual(john.getBirthdate(), '1976-03-17')
        self.assertEqual(john._FighterAthlete__wins, 4)
        self.assertEqual(john._FighterAthlete__draws, 0)
        self.assertEqual(john._FighterAthlete__losses, 1)

    def test_mma_fighter_athlete(self):
        organizations = ['UFC', 'Bellator', 'One Championship']
        bob = MMAFighterAthlete('Bobby Bob', 'Bolivia', '1998-09-09', 5, 0, 1, organizations)
        self.assertEqual(bob.getName(), 'Bobby Bob')
        self.assertEqual(bob.getCountry(), 'Bolivia')
        self.assertEqual(bob.getBirthdate(), '1998-09-09')
        self.assertEqual(bob._MMAFighterAthlete__wins, 5)
        self.assertEqual(bob._MMAFighterAthlete__draws, 0)
        self.assertEqual(bob._MMAFighterAthlete__losses, 1)
        self.assertEqual(bob._MMAFighterAthlete__organizations, organizations)

    def test_soccer_athlete(self):
        bob = SoccerAthlete('Bobby Bob', 'Bolivia', '1998-09-09', 'La Paz United', 'goal keeper')
        self.assertEqual(bob.getName(), 'Bobby Bob')
