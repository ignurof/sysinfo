import unittest
import main

class Test(unittest.TestCase):
    def test_total(self):
        self.assertEqual(main.run(['total']), 0)

    def test_available(self):
        self.assertEqual(main.run(['available']), 0)

    def test_handle_empty_string(self):
        self.assertEqual(main.run(['']), 1)

    def test_handle_invalid_string(self):
        self.assertEqual(main.run(['blablab']), 1)


if __name__ == '__main__':
    t = Test()
    t.test_total()
    t.test_available()
    t.test_handle_empty_string()
    t.test_handle_invalid_string()
