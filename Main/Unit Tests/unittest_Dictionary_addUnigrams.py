import unittest
import sys
sys.path.append("..")
from Main_Drivers.Classes.Dictionary import Dictionary


class MyTest(unittest.TestCase):
    
    def test_addUnigrams(self):
        """
        Test add unigrams function. Check if the total number of words
        for each class label is correct. Then check if the frequency
        for each word is correct.
        """
        dictionaryUnit = Dictionary(5)
        dictionary = dictionaryUnit.dictionary
        
        for i in range(15):
            dictionaryUnit.addUnigrams(1, "once")
            dictionaryUnit.addUnigrams(2, "charming two")
            dictionaryUnit.addUnigrams(3, "word words wordies")
            dictionaryUnit.addUnigrams(4, "fox tail him now")
            dictionaryUnit.addUnigrams(5, "here is where he lived")
    
        self.assertEqual( dictionaryUnit.getTotalTerms(), [0, 15, 30, 45, 60, 75])
        
        self.assertEqual( "once" in dictionary, True)
        
        self.assertEqual( "charming" in dictionary, True)
        self.assertEqual( "two" in dictionary, True)
        
        self.assertEqual( "word" in dictionary, True)
        self.assertEqual( "words" in dictionary, True)
        self.assertEqual( "wordies" in dictionary, True)
        
        self.assertEqual( "fox" in dictionary, True)
        self.assertEqual( "tail" in dictionary, True)
        self.assertEqual( "him" in dictionary, True)
        self.assertEqual( "now" in dictionary, True)
        
        self.assertEqual( "here" in dictionary, True)
        self.assertEqual( "is" in dictionary, True)
        self.assertEqual( "where" in dictionary, True)
        self.assertEqual( "he" in dictionary, True)
        self.assertEqual( "lived" in dictionary, True)

        self.assertEqual( "heeae" in dictionary, False)
        self.assertEqual( "lasdsad" in dictionary, False)

        self.assertEqual( dictionary["once"].tf, [0, 15, 0, 0, 0, 0])
        
        self.assertEqual( dictionary["charming"].tf, [0, 0, 15, 0, 0, 0])
        self.assertEqual( dictionary["two"].tf, [0, 0, 15, 0, 0, 0])
        
        self.assertEqual( dictionary["word"].tf, [0, 0, 0, 15, 0, 0])
        self.assertEqual( dictionary["words"].tf, [0, 0, 0, 15, 0, 0])
        self.assertEqual( dictionary["wordies"].tf, [0, 0, 0, 15, 0, 0])
        
        self.assertEqual( dictionary["fox"].tf, [0, 0, 0, 0, 15, 0])
        self.assertEqual( dictionary["tail"].tf, [0, 0, 0, 0, 15, 0])
        self.assertEqual( dictionary["him"].tf, [0, 0, 0, 0, 15, 0])
        self.assertEqual( dictionary["now"].tf, [0, 0, 0, 0, 15, 0])

        self.assertEqual( dictionary["here"].tf, [0, 0, 0, 0, 0, 15])
        self.assertEqual( dictionary["is"].tf, [0, 0, 0, 0, 0, 15])
        self.assertEqual( dictionary["where"].tf, [0, 0, 0, 0, 0, 15])
        self.assertEqual( dictionary["he"].tf, [0, 0, 0, 0, 0, 15])
        self.assertEqual( dictionary["lived"].tf, [0, 0, 0, 0, 0, 15])


if __name__ == '__main__':
    unittest.main()
