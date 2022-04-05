import unittest
import testGrades


class TestGradesCalc(unittest.TestCase):

#Check if the number of students are correct
    def test_numberofstudents(self):
        self.assertEqual(10,len(testGrades.sql_reader))
#Check if grades match calculated average marks
    def test_averageMarkGrades(self):
            self.assertEqual("A",testGrades.val[0][3])

if __name__ == '__main__':
    unittest.main()

