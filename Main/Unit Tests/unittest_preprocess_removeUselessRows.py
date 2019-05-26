import unittest
import sys
sys.path.append("..")
from preprocess import removeUselessRows


class MyTest(unittest.TestCase):
    
    def test_removeUselessRows1(self):

        """
        Test using a tab-delimited .txt file with empty cells, and an empty row.
        The test case will have a total of 9 rows, but 5 of them is not viable.
        4 of the rows have an empty cell, and 1 row has is completely empty.
        Expected output file should have only 4 remaining rows.
        
        TEST TEXT FILE FORMAT
        |--------------------
        |	hello       |-> no rating
        |2	this        |
        |4	            |-> no text review
        |1	is          |
        |	            |-> no both
        |5	testing     |
        |1	            |-> no text review
        |4	over        |
        |	roger       |-> no rating
        ---------------------
        """
        print("\n\n===== TEST CASE 1 =====")
        testCaseString = ["\thello",
                        "2\tthis",
                        "4",
                        "1\tis",
                        "\t",
                        "5\ttesting",
                        "1",
                        "4\tover",
                        "\troger"
                        ]

        # Write input string into file
        testCaseString = "\n".join(testCaseString)
        print("Before cleaning dataset\n-----------------------")
        print(testCaseString)

        testCaseFile = open("test_txt_file_for_cleanDataset.txt", "w")
        testCaseFile.write(testCaseString)
        testCaseFile.close()

        # Clean the input data set file
        removeUselessRows("test_txt_file_for_cleanDataset.txt")

        # Check if the data set file is correct after removing useless rows
        testCaseFile = open("test_txt_file_for_cleanDataset.txt", "r", encoding="utf-8-sig")
        outputString = ""
        for line in testCaseFile:
            outputString += line

        
        print("\nAfter cleaning dataset\n-----------------------")
        print(outputString)

        expectedOutputString = "\n".join(["2\tthis",
                                         "1\tis",
                                         "5\ttesting",
                                         "4\tover"])
        self.assertEqual(outputString, expectedOutputString)
        testCaseFile.close()

    def test_cremoveUselessRows2(self):

        """
        Only 1 viable row, which is the first row.
        
        TEST TEXT FILE FORMAT
        |----------------------------
        |3	THIS IS GOOD PRODUCT|
        |	                    |-> no both
        |4	                    |-> no text review
        |	NOT WELL MADE       |-> no rating
        -----------------------------
        """
        print("\n\n===== TEST CASE 2 =====")
        testCaseString = ['3\tTHIS IS GOOD PRODUCT',
                          '\t',
                          '4\t',
                          '\tNOT WELL MADE']

        testCaseString = "\n".join(testCaseString)
        print("Before cleaning dataset\n-----------------------")
        print(testCaseString)

        testCaseFile = open("test_txt_file_for_cleanDataset.txt", "w")
        testCaseFile.write(testCaseString)
        testCaseFile.close()

        # Clean the input data set file
        removeUselessRows("test_txt_file_for_cleanDataset.txt")

        # Check if the data set file is correct after removing useless rows
        testCaseFile = open("test_txt_file_for_cleanDataset.txt", "r", encoding="utf-8-sig")
        outputString = ""
        for line in testCaseFile:
            outputString += line

        
        print("\nAfter cleaning dataset\n-----------------------")
        print(outputString)

        expectedOutputString = "3\tTHIS IS GOOD PRODUCT"
        self.assertEqual(outputString, expectedOutputString)
        testCaseFile.close()


if __name__ == '__main__':
    unittest.main()
