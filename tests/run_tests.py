import unittest


class TestCythonizeCode(unittest.TestCase):

    def test_func_code(self):
        from aaa import hello

        print(hello.say_hi(name='Python'))

    def test_package_code(self):
        from bbb import main_code
        from bbb.ccc import coffee

        main_code.run()
        print(coffee.get_coffee(2))


if __name__ == '__main__':
    unittest.main()
