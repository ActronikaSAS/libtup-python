import unittest
from input import Input


class TestInput(unittest.TestCase):
    def setUp(self):
        self.input = Input()

    def test_id(self):
        self.assertEqual(self.input.id, 0, "Default id must be 0")
        self.input.id = 42
        self.assertEqual(self.input.id, 42, "Id must be 42 now")
        self.input.id = "45"
        self.assertEqual(self.input.id, 42, "Id must not be 45")
        self.input.id = 13.37
        self.assertEqual(self.input.id, 42, "Id must not be 45")
        self.input.id = 255
        self.assertEqual(self.input.id, 255, "Id must be max value : 255")
        self.input.id = 256
        self.assertEqual(self.input.id, 255, "Id must not change")
        self.input.id = -1
        self.assertEqual(self.input.id, 255, "Id must not be negative")

    def test_value(self):
        self.assertEqual(self.input.value, 0, "Default Value must be 0")
        self.input.value = 42
        self.assertEqual(self.input.value, 42, "Value must be 42 now")
        self.input.value = "45"
        self.assertEqual(self.input.value, 42, "Value must not be 45")
        self.input.value = 13.37
        self.assertEqual(self.input.value, 42, "Value must not be 45")
        self.input.value = 2147483647
        self.assertEqual(self.input.value, 2147483647, "Value must be max")
        self.input.value = 2147483648
        self.assertEqual(self.input.value, 2147483647, "Value must not change")
        self.input.value = -2147483648
        self.assertEqual(self.input.value, -2147483648, "Must be min value")
        self.input.value = -2147483649
        self.assertEqual(self.input.value, -2147483648, "Must not change")


if __name__ == '__main__':
    unittest.main()
