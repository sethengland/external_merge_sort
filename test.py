import random
import struct
import unittest
import os
from write import write_integers
from sort import read_and_sort
from verify import verify_is_sorted
from helpers import tear_down_previous


class TestExternalMergeSort(unittest.TestCase):

    def setUp(self):
        self.N = 1000  
        self.M = 10    
        self.test_input_file = 'test_input.bin'
        self.test_sorted_file = 'test_sorted.bin'

        write_integers(self.test_input_file, self.N)

    def tearDown(self):
        tear_down_previous(self.test_input_file, self.test_sorted_file)

    def test_write_integers(self):
        filename = 'random_integers.bin'
        write_integers(filename, self.N)

        # Check if the file exists and has the correct size
        self.assertTrue(os.path.exists(filename))
        self.assertEqual(os.path.getsize(filename), self.N * 4)
        os.remove('random_integers.bin')
    
    def test_verify_is_sorted_on_unsorted_data(self):
        unsorted_file = 'unsorted_test_input.bin'
        write_integers(unsorted_file, self.N)

        is_sorted = verify_is_sorted(unsorted_file, self.M)
        self.assertFalse(is_sorted)
        
        os.remove(unsorted_file)

    def test_verify_is_sorted(self):
        file = open("known_sorted.bin", 'wb')
        sorted_integers = sorted(random.randint(0, (2 ** 32) - 1) for _ in range(self.N))
        for integer in sorted_integers:
            file.write(struct.pack("I", integer))
            
        is_sorted = verify_is_sorted("known_sorted.bin", self.M)
        self.assertTrue(is_sorted)
        file.close()
        os.remove("known_sorted.bin")

    def test_read_and_sort(self):
        read_and_sort(self.test_input_file, self.test_sorted_file, self.M)
        is_sorted = verify_is_sorted(self.test_sorted_file, self.M)
        self.assertTrue(is_sorted)

if __name__ == '__main__':
    unittest.main()

