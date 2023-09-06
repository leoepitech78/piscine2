import unittest
from ex_01ter import Athlete

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

    def test_set_name(self):
        bob = Athlete('Bobby Bob', 'Bolivia', '1998-09-09')
        bob.setName('John Doe')
        self.assertEqual(bob._Athlete__name, 'John Doe')

    def test_set_country(self):
        bob = Athlete('Bobby Bob', 'Bolivia', '1998-09-09')
        bob.setCountry('Bora Bora')
        self.assertEqual(bob._Athlete__country, 'Bora Bora')

    def test_set_birthdate(self):
        bob = Athlete('Bobby Bob', 'Bolivia', '1998-09-09')
        bob.setBirthdate('2000-01-01')
        self.assertEqual(bob._Athlete__birthdate, '2000-01-01')

if __name__ == '__main__':
    unittest.main()
