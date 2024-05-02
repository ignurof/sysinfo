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

    def test_convert_kb_to_gb(self):
        self.assertEqual(main.convert_kb_to_gb(1024), 0.001024)
        self.assertEqual(main.convert_kb_to_gb(1024000), 1.024)
        self.assertEqual(main.convert_kb_to_gb(1000000), 1)

    def test_parse_meminfo(self):
        self.assertEqual(type(main.parse_meminfo('MemTotal')), type([]))


if __name__ == '__main__':
    t = Test()
    t.test_total()
    t.test_available()
    t.test_handle_empty_string()
    t.test_handle_invalid_string()
    t.test_convert_kb_to_gb()
    t.test_parse_meminfo()
