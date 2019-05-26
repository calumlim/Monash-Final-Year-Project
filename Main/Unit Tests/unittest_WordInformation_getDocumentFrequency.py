import unittest
import sys
sys.path.append("..")
from Main_Drivers.Classes.WordInformation import WordInformation


class MyTest(unittest.TestCase):
    
    def test_getDocumentFrequency(self):
        """
        Test with valid test cases.
        """
        testUnit = WordInformation(5)

        testUnit.tf = [0, 0, 0, 0, 0, 0]
        self.assertEqual( testUnit.getDocumentFrequency(), 0)

        testUnit.tf = [0, 5, 0, 0, 0, 0]
        self.assertEqual( testUnit.getDocumentFrequency(), 1)

        testUnit.tf = [0, 0, 7, 0, 0, 0]
        self.assertEqual( testUnit.getDocumentFrequency(), 1)

        testUnit.tf = [0, 0, 0, 9, 0, 0]
        self.assertEqual( testUnit.getDocumentFrequency(), 1)

        testUnit.tf = [0, 0, 0, 0, 4, 0]
        self.assertEqual( testUnit.getDocumentFrequency(), 1)

        testUnit.tf = [0, 0, 0, 0, 0, 3]
        self.assertEqual( testUnit.getDocumentFrequency(), 1)
        
        testUnit.tf = [0, 3, 3, 0, 0, ]
        self.assertEqual( testUnit.getDocumentFrequency(), 2)

        testUnit.tf = [0, 3, 0, 3, 0, 0]
        self.assertEqual( testUnit.getDocumentFrequency(), 2)

        testUnit.tf = [0, 3, 0, 0, 3, 0]
        self.assertEqual( testUnit.getDocumentFrequency(), 2)

        testUnit.tf = [0, 5, 0, 5, 7, 0]
        self.assertEqual( testUnit.getDocumentFrequency(), 3)

        testUnit.tf = [0, 5, 1, 5, 7, 0]
        self.assertEqual( testUnit.getDocumentFrequency(), 4)

        testUnit.tf = [0, 5, 1, 5, 7, 2]
        self.assertEqual( testUnit.getDocumentFrequency(), 5)


    def test_getDocumentFrequencyError(self):
        """
        Test with invalid test cases.
        """
        testUnit = WordInformation(5)
        
        testUnit.tf = [1, 5, 3, 5, 7, 44]
        with self.assertRaises(Exception):
            testUnit.getDocumentFrequency()

        testUnit.tf = [1, 0, 0, 0, 2, 4]
        with self.assertRaises(Exception):
            testUnit.getDocumentFrequency()

        testUnit.tf = [1, 0, 0, 0, 0, 0]
        with self.assertRaises(Exception):
            testUnit.getDocumentFrequency()


if __name__ == '__main__':
    unittest.main()
