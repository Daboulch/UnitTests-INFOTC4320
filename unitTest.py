import unittest
from datetime import datetime

class TestClass(unittest.TestCase):

    def test_symbol(self):
        #True Tests
        self.assertEqual(1 <= len(s := "AAPL") <= 7 and s.isalpha() and s.isupper(), True)
        self.assertEqual(1 <= len(s := "TESTABC") <= 7 and s.isalpha() and s.isupper(), True)
        self.assertEqual(1 <= len(s := "A") <= 7 and s.isalpha() and s.isupper(), True)
        #False Tests
        self.assertEqual(1 <= len(s := "aapl") <= 7 and s.isalpha() and s.isupper(), False)
        self.assertEqual(1 <= len(s := "") <= 7 and s.isalpha() and s.isupper(), False)
        self.assertEqual(1 <= len(s := "AAAAAAAA") <= 7 and s.isalpha() and s.isupper(), False)
        self.assertEqual(1 <= len(s := "1234-%") <= 7 and s.isalpha() and s.isupper(), False)

    def test_chart(self):
        #True Tests
        self.assertEqual((choice := "1") in ["1", "2"], True)
        self.assertEqual((choice := "2") in ["1", "2"], True)
        #False Tests
        self.assertEqual((choice := "3") in ["1", "2"], False)
        self.assertEqual((choice := "0") in ["1", "2"], False)
        self.assertEqual((choice := "wasd") in ["1", "2"], False)

    def test_timeSeries(self):
        #True Tests
        self.assertEqual((choice := "1") in ["1", "2", "3", "4"], True)
        self.assertEqual((choice := "2") in ["1", "2", "3", "4"], True)
        self.assertEqual((choice := "3") in ["1", "2", "3", "4"], True)
        self.assertEqual((choice := "4") in ["1", "2", "3", "4"], True)
        #False Tests
        self.assertEqual((choice := "5") in ["1", "2", "3", "4"], False)
        self.assertEqual((choice := "0") in ["1", "2", "3", "4"], False)
        self.assertEqual((choice := "wasd") in ["1", "2", "3", "4"], False)

    def test_startDate(self):
        #True Tests
        self.assertEqual(valid := bool(datetime.strptime("2023-01-15", "%Y-%m-%d")), True)
        self.assertEqual(valid := bool(datetime.strptime("2000-12-31", "%Y-%m-%d")), True)
        #False Tests
        with self.assertRaises(ValueError):
            datetime.strptime("2023-13-15", "%Y-%m-%d")
        with self.assertRaises(ValueError):
            datetime.strptime("2023-01-40", "%Y-%m-%d")
        with self.assertRaises(ValueError):
            datetime.strptime("15-01-2023", "%Y-%m-%d")



    def test_endDate(self):
        #Same as startDate since same requirements
        #True Tests
        self.assertEqual(valid := bool(datetime.strptime("2023-01-15", "%Y-%m-%d")), True)
        self.assertEqual(valid := bool(datetime.strptime("2000-12-31", "%Y-%m-%d")), True)
        #False Tests
        with self.assertRaises(ValueError):
            datetime.strptime("2023-13-15", "%Y-%m-%d")
        with self.assertRaises(ValueError):
            datetime.strptime("2023-01-40", "%Y-%m-%d")
        with self.assertRaises(ValueError):
            datetime.strptime("15-01-2023", "%Y-%m-%d")

if __name__ == '__main__':
    unittest.main()