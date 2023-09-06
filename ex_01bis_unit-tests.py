import unittest
from ex_01bis import Athlete

class TestAthlete(unittest.TestCase):
    
    def test_create_athlete(self):
        bob = Athlete('Bobby Bob', 'Bolivia', '1998-09-09')
        self.assertEqual(bob._Athlete__name, 'Bobby Bob')
        self.assertEqual(bob._Athlete__country, 'Bolivia')
        self.assertEqual(bob._Athlete__birthdate, '1998-09-09')
        self.assertEqual(bob._Athlete__records, {})

    def test_add_record(self):
        bob = Athlete('Bobby Bob', 'Bolivia', '1998-09-09')
        bob.add_record('2020 La Paz Championship', '2nd')
        self.assertEqual(bob._Athlete__records, {'2020 La Paz Championship': '2nd'})

if __name__ == '__main__':
    unittest.main()
