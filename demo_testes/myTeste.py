import unittest
import main as m


class MyTestCase(unittest.TestCase):

    def test_something(self):
        self.assertEqual(1+1, 2)  # add assertion here

    def test_soma(self):
        self.assertEqual(4, m.soma(1,3), "valor incorrecto")

    def test_soma2(self):
        self.assertEqual(2, m.soma(-1,3))

    def test_multip(self):
        self.assertEqual(-3, m.multip(-1, 3))

    def test_multip2(self):
        self.assertEqual(6, m.multip(2, 3))

    def test_div(self):
        self.assertEqual(True, True)
        self.assertEqual(-3, m.div(3, -1))
        self.assertEqual(3, m.div(9, 3))



if __name__ == '__main__':
    unittest.main()
