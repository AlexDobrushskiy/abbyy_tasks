import unittest
import random


def partition(A, s, e):  # A - array to partition , s - start index, e - end index, so we apply partition for A[s:e+1]
    rnd_idx = random.randint(s, e)
    A[e], A[rnd_idx] = A[rnd_idx], A[e]
    i = s - 1
    j = s
    x = A[e]
    while j < e:
        if A[j] < x:
            A[i+1], A[j] = A[j], A[i+1]
            i = i + 1
        j = j + 1
    A[i+1], A[e] = A[e], A[i+1]
    return i + 1


def quicksort(A, s, e):  # same - A - array, s - start index, e - end index.
    if s >= e:
        return  # already sorted
    while s < e:
        i = partition(A, s, e)
        if i-s < e-i:
            quicksort(A, s, i - 1)
            s = i + 1
        else:
            quicksort(A, i+1, e)
            e = i-1


class Test(unittest.TestCase):
    def test1(self):
        s = [2, 3, 1]
        quicksort(s, 0, 2)
        self.assertEqual(s, sorted(s))
        s = []
        quicksort(s, 0, 0)
        self.assertEqual(s, sorted(s))

        s = [random.randint(-1000, 1000) for i in range(100)]

        quicksort(s, 0, len(s)-1)
        self.assertEqual(s, sorted(s))


    def test2(self):
        s = [2, 3, 1, -1, 100, -999]
        quicksort(s, 0, 5)
        self.assertEqual(s, sorted(s))


if __name__ == '__main__':
    unittest.main()
