import unittest
from ex_02 import Athlete, Competition

class TestCompetition(unittest.TestCase):
    
    def test_create_competition(self):
        ufc = Competition('2025 Ultimate Fight Championship')
        self.assertEqual(ufc._Competition__name, '2025 Ultimate Fight Championship')
        self.assertEqual(ufc._Competition__athletes, [])

    def test_add_athlete(self):
        ufc = Competition('2025 Ultimate Fight Championship')
        bob = Athlete('Bobby Bob', 'Bolivia', '1998-09-09')
        ufc.add_athlete(bob)
        self.assertEqual(ufc._Competition__athletes, [bob])

    def test_exclude(self):
        ufc = Competition('2025 Ultimate Fight Championship')
        bob = Athlete('Bobby Bob', 'Bolivia', '1998-09-09')
        john = Athlete('Johny John', 'Jordan', '1976-03-17')
        ufc.add_athlete(bob)
        ufc.add_athlete(john)
        ufc.exclude(john)
        self.assertEqual(ufc._Competition__athletes, [bob])

    def test_rank(self):
        ufc = Competition('2025 Ultimate Fight Championship')
        bob = Athlete('Bobby Bob', 'Bolivia', '1998-09-09')
        ufc.add_athlete(bob)
        ufc.rank(bob, 1)
        self.assertEqual(bob._Athlete__records, {'2025 Ultimate Fight Championship': 1})

if __name__ == '__main__':
    unittest.main()
