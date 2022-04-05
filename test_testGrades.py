import unittest
import testGrades

class TestGradesCalc(unittest.TestCase):

    def test_numberofstudents(self):
        self.assertEqual(11,len(testGrades.sql_reader))

if __name__ == '__main__':
    unittest.main()