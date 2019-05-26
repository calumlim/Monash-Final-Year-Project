import unittest
import os
import sys
sys.path.append("..")
from preprocess import cleanSentence

class MyTest(unittest.TestCase):
    
    def test_cleanWord(self):
        testString = "Look out!!! Over here, Green!"
        self.assertEqual( cleanSentence(testString), "look out over here green")

        testString = "This product,,,is quite good indeed yes?"
        self.assertEqual( cleanSentence(testString), "this product is quite good indeed yes")

        testString = "Although..He did seem a bit odd"
        self.assertEqual( cleanSentence(testString), "although he did seem a bit odd")

        testString = "aa..bb..cc..dd"
        self.assertEqual( cleanSentence(testString), "aa bb cc dd")

        testString = "Hello There!... this bottle is free"
        self.assertEqual( cleanSentence(testString), "hello there this bottle is free")

        testString = "Alonso.................."
        self.assertEqual( cleanSentence(testString), "alonso")

        testString = "Although.. He did seem a bit odd"
        self.assertEqual( cleanSentence(testString), "although he did seem a bit odd")

        testString = "Although ..He did seem a bit odd"
        self.assertEqual( cleanSentence(testString), "although he did seem a bit odd")

        testString = "....!!...why"
        self.assertEqual( cleanSentence(testString), "why")

        testString = "excuses .. excuses ... excuses .... excuses "
        self.assertEqual( cleanSentence(testString), "excuses excuses excuses excuses")

        testString = "Hello. My name is Julian."
        self.assertEqual( cleanSentence(testString), "hello my name is julian")

        testString = "i. am. dot. world."
        self.assertEqual( cleanSentence(testString), "i am dot world")

        testString = "i. am. dot. world."
        self.assertEqual( cleanSentence(testString), "i am dot world")

        testString = ".Word"
        self.assertEqual( cleanSentence(testString), "word")

        testString = "!@#$%^&*(*)-_=+-+=-{}[];':,.<>//?"
        self.assertEqual( cleanSentence(testString), "")

        testString = "4325<>,.''"
        self.assertEqual( cleanSentence(testString), "4325")

        testString = "A1B2C3"
        self.assertEqual( cleanSentence(testString), "a1b2c3")

        testString = "OVER.HERE.SON     ."
        self.assertEqual( cleanSentence(testString), "over here son")

        testString = "HOW ..32903()"
        self.assertEqual( cleanSentence(testString), "how 32903")

        testString = ""
        self.assertEqual( cleanSentence(testString), "")
        
if __name__ == '__main__':
    
    unittest.main()
