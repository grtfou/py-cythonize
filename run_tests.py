import unittest


class TestCythonizeCode(unittest.TestCase):

    def test_func_code(self):
        from my_test_zoo.elephant.monkey import coffee

        assert coffee.get_coffee(cup=2) == 3

    def test_package_code(self):
        from my_test_zoo.lion import hello
        assert hello.say_hi('Micky Mouse') == 'Hi, Micky Mouse'


if __name__ == '__main__':
    unittest.main()
