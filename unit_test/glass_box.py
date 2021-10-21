import unittest

def is_major(age):
    return age >= 18

class TestGlassBox(unittest.TestCase):
    def test_get_major_age(self):
        age = 20
        result = is_major(age)

        self.assertEqual(result, True)

if __name__ == '__main__':
    unittest.main()
