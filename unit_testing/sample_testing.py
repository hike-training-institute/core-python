import unittest


def add(x, y):
    # 1000 lines
    return x + y




class SimpleTest(unittest.TestCase):
    def testadd1(self):
        self.assertEquals(add(4, 10), 2)

    def empty(self):
        print('asdasd')
        self.assertEquals(add(4, 10), 2)


class SimpleTest1(unittest.TestCase):
    def testadd1(self):
        self.assertEquals(add(4, 10), 14)


if __name__ == '__main__':
    unittest.main()