import unittest

def sum_positive(a, b):
    return a + b

def get_all_name(name):
    return f'Hello {name}'

class TestBlackBox(unittest.TestCase):
    def test_sum(self):
        num1 = 5
        num2 = 6
        result = sum_positive(num1, num2)
        self.assertEqual(result, 11)

    def test_sum2(self):
        num1 = 5
        num2 = 7
        result = sum_positive(num1, num2)
        self.assertEqual(result, 12)
    
    def test_get_full_name(self):
        name = 'benji'
        result = get_all_name(name)
        self.assertEqual(result, 'Hello benji')
    

if __name__ == '__main__':
    unittest.main()
