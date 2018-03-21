import unittest
from parameter import Parameter


class TestParameter(unittest.TestCase):
    def setUp(self):
        self.parameter = Parameter()

    def test_id(self):
        self.assertEqual(self.parameter.id, 0, "Default id must be 0")
        self.parameter.id = 42
        self.assertEqual(self.parameter.id, 42, "Id must be 42 now")
        self.parameter.id = "45"
        self.assertEqual(self.parameter.id, 42, "Id must not be 45")
        self.parameter.id = 13.37
        self.assertEqual(self.parameter.id, 42, "Id must not be 45")
        self.parameter.id = 255
        self.assertEqual(self.parameter.id, 255, "Id must be max value : 255")
        self.parameter.id = 256
        self.assertEqual(self.parameter.id, 255, "Id must not change")
        self.parameter.id = -1
        self.assertEqual(self.parameter.id, 255, "Id must not be negative")

    def test_value(self):
        self.assertEqual(self.parameter.value, 0, "Default Value must be 0")
        self.parameter.value = 42
        self.assertEqual(self.parameter.value, 42, "Value must be 42 now")
        self.parameter.value = "45"
        self.assertEqual(self.parameter.value, 42, "Value must not be 45")
        self.parameter.value = 13.37
        self.assertEqual(self.parameter.value, 42, "Value must not be 45")
        self.parameter.value = 4294967295
        self.assertEqual(self.parameter.value, 4294967295, "Value must be max")
        self.parameter.value = 4294967296
        self.assertEqual(
                self.parameter.value,
                4294967295,
                "Value must not change"
            )
        self.parameter.value = 0
        self.assertEqual(self.parameter.value, 0, "Must be min value")
        self.parameter.value = -1
        self.assertEqual(self.parameter.value, 0, "Must not change")


if __name__ == '__main__':
    unittest.main()
