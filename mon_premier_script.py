import unittest

from typing import List

def count_names_with_more_than_seven_letters(prenoms: List[str]) -> int:
    count = 0
    for prenom in prenoms:
        if len(prenom) > 7:
            count += 1
            print(f"Name with more than 7 letters: {prenom}")
        else:
            print(f"Name with 7 letters or less: {prenom}")
    return count


class TestNamesMethod(unittest.TestCase):
     def test_names(self):
        prenoms = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
        more_than_seven = count_names_with_more_than_seven_letters(prenoms=prenoms)
        self.assertEqual(more_than_seven, 4)

 
if __name__ == '__main__':
    unittest.main()