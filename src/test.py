import unittest
import main

class Test(unittest.TestCase):
    def test_total(self):
        self.assertEqual(main.run(['total']), 'Total')

    def test_available(self):
        self.assertEqual(main.run(['available']), 'Available')

if __name__ == '__main__':
    t = Test()
    t.test_total()
    t.test_available()
