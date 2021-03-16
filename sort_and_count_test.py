import unittest
from main import sort_and_count


def get_inv_count(arr, n):
    inv_count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                inv_count += 1
    return inv_count


class MyTestCase(unittest.TestCase):
    def test1(self):
        arr = [1, 20, 6, 4, 5, 2, 3]
        self.assertEqual(get_inv_count(arr, len(arr)), sort_and_count(arr))

    def test2(self):
        arr2 = [-3, 20, 6, -4, 5, 2, 3.5]
        self.assertEqual(get_inv_count(arr2, len(arr2)), sort_and_count(arr2))

    def test3(self):
        arr3 = [1, 5, 3, -2, 2, 6, 90, 4, 8, 9, -3, 12]
        self.assertEqual(get_inv_count(arr3, len(arr3)), sort_and_count(arr3))


if __name__ == '__main__':
    unittest.main()
