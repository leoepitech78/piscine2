import unittest
from ex_01 import Athlete

class TestAthlete(unittest.TestCase):
    
    def test_create_athlete(self):
        bob = Athlete('Bobby Bob', 'Bolivia', '1998-09-09')
        self.assertEqual(bob.name, 'Bobby Bob')
        self.assertEqual(bob.country, 'Bolivia')
        self.assertEqual(bob.birthdate, '1998-09-09')
        self.assertEqual(bob.records, {})

    def test_add_record(self):
        bob = Athlete('Bobby Bob', 'Bolivia', '1998-09-09')
        bob.add_record('2020 La Paz Championship', '2nd')
        self.assertEqual(bob.records, {'2020 La Paz Championship': '2nd'})

if __name__ == '__main__':
    unittest.main()
