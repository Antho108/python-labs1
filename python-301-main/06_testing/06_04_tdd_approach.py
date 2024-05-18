# Write a script that demonstrates TDD. Using pseudocode, plan out
# a couple of small functions. They could be as fundamental as adding
# and subtracting numbers with each other,
# or more complex such as functions that read and write to files.
#
# Instead of writing the functions, however, only write the tests for them.
# Think about how your functions might fail and write tests that will check 
# for that and identify these failures.
#
# You do not need to implement the actual functions after writing the tests 
# but of course you can do that, too.

# one function hello world 

import unittest

def hello_world():
    return 'hello world'

class MyFirstTests(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(hello_world(), 'hello world')



def add_num(num1, num2): 
    return num1 + num2

class MySecondTests(unittest.TestCase):

    def test_add_num(self):
        self.assertEqual(add_num(2, 1), 3)


def read_write_files():
    file = open("test.txt", "r")
    contents = file.read()
    print(contents)

class MyThirdTests(unittest.TestCase):

    # Test si le fichier a etait lu ou open 
    def test_open_file(self):
        with open("python-301-main/06_testing/myfile.txt", "r") as file:
            contents = file.read()
        self.assertIsNotNone(contents, "Failed to read file")




if __name__ == "__main__":
    unittest.main()


# https://www.freecodecamp.org/news/learning-to-test-with-python-997ace2d8abe