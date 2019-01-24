import math
import unittest


def get_2_missed_numbers(n, l):
    # TODO: corner cases to process when disctiminant < 0. currently just raising python exception
    sa = 0
    s = 0
    sqa = 0
    sq = 0
    # calc sa and sqa
    for i in range(n + 1):
        sa += i
        sqa += i * i
    for i in l:
        s += i
        sq += i * i

    # say first digit we're looking is q1 second is q2
    # we have square equation for q1:
    x = sa - s
    y = sqa - sq

    a = 2
    b = -2 * x
    c = x * x - y

    d = (b ** 2) - (4 * a * c)
    sol1 = (-b - math.sqrt(d)) / (2 * a)
    sol2 = (-b + math.sqrt(d)) / (2 * a)
    if 0 <= sol1 <= n:
        q1 = sol1
    else:
        q1 = sol2
    q2 = x - q1
    return (q1, q2)


class Test(unittest.TestCase):
    def test1(self):
        seq = [0, 2, 4]
        n = 4
        self.assertIn(1, get_2_missed_numbers(n, seq))
        self.assertIn(3, get_2_missed_numbers(n, seq))

    def test2(self):
        seq = [0, 1, 2, 4, 5, 6]
        n = 7
        self.assertIn(3, get_2_missed_numbers(n, seq))
        self.assertIn(7, get_2_missed_numbers(n, seq))


if __name__ == '__main__':
    unittest.main()
