# Implement Test functions for filecmp.cmp() function
# author: Saul DLD

import unittest
import filecmp
import os

common_1 = os.getcwd() + os.sep + "dir1" + os.sep + "common.txt"
common_2 = os.getcwd() + os.sep + "dir2" + os.sep + "common.txt"

file_1 = os.getcwd() + os.sep + "dir1" + os.sep + "file.txt"
file_2 = os.getcwd() + os.sep + "dir2" + os.sep + "file.txt"

file_a = os.getcwd() + os.sep + "dir1" + os.sep + "file_a.txt"
file_b = os.getcwd() + os.sep + "dir2" + os.sep + "file_b.txt"


class TestFileCmpSuite(unittest.TestCase):

    # Right and Correct: Basic test that verify and confirm the functionality of the cmp() function
    def test_basic(self):
        # Both documents are the same, same metadata and content
        c1 = filecmp.cmp(common_1, common_2)
        c2 = filecmp.cmp(common_1, common_2, shallow=False)
        self.assertTrue(c1)
        self.assertTrue(c2)

        # (Inverse) Both documents are not the same, neither metadata nor content
        c1 = filecmp.cmp(file_1, file_2)
        c2 = filecmp.cmp(file_1, file_2, shallow=False)
        self.assertFalse(c1)
        self.assertFalse(c2)

    # Work in progress:
    # B: Compare metadata against content
    # This test should validate that metadata are not the same, but content it is.
    # should return False - True
    def test_boundaries(self):
        c1 = filecmp.cmp(file_a, file_b)
        c2 = filecmp.cmp(file_a, file_b, shallow=False)
        print(os.stat(c1))
        print(os.stat(c2))
        print(c1)
        print(c2)

    # Forcing error
    # cmp() function should return true for two identical files (metadata and content)
    # If there are any reason this function return "false" then there is an error in cmp()
    @unittest.expectedFailure
    def test_inverse(self):
        c1 = filecmp.cmp(common_1, common_2)
        c2 = filecmp.cmp(common_1, common_2, shallow=False)
        self.assertFalse(c1, c2)

    # Performance: filecmp.cmp() performance is in charge of a third party developer (Python core)


if __name__ == '__main__':
    unittest.main()
