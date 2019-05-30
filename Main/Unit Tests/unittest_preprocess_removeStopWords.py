import unittest
from nltk.corpus import stopwords

def removeStopWords(inputSentence):
    """
    Arguments:
        inputSentence (str): A written review

    Returns:
        outputSentence (str): The written review with stop words filtered out
    """
    outputSentence = []
    inputSentence = inputSentence.split()

    for word in inputSentence:
        if word not in stop_words:
            outputSentence.append(word)
    
    return " ".join(outputSentence)


class MyTest(unittest.TestCase):
    
    def test_removeStopWords(self):
        stopwordsList = list(stop_words)
        print(stopwordsList)

        # Add all stop words into a string.
        # Call removeStopWords on that string,
        # output should be empty string
        testString = " ".join(stopwordsList)
        outputString = removeStopWords(testString)
        self.assertEqual(outputString, "")

        testString = "such a turn off i other what these"
        outputString = removeStopWords(testString)
        self.assertEqual(outputString, "turn")

        testString = "after so now have hers we will do it"
        outputString = removeStopWords(testString)
        self.assertEqual(outputString, "")

        testString = "i have been over this again and again"
        outputString = removeStopWords(testString)
        self.assertEqual(outputString, "")

        testString = "through be down until ma have in other"
        outputString = removeStopWords(testString)
        self.assertEqual(outputString, "")

        testString = "i wish there was a bit more features in this"
        outputString = removeStopWords(testString)
        self.assertEqual(outputString, "wish bit features")

        testString = "both our hands could not fit the product"
        outputString = removeStopWords(testString)
        self.assertEqual(outputString, "hands could fit product")

        testString = "it made it feel like our own"
        outputString = removeStopWords(testString)
        self.assertEqual(outputString, "made feel like")

        testString = "while this was between the kindle or the express"
        outputString = removeStopWords(testString)
        self.assertEqual(outputString, "kindle express")

        testString = "i can have this under at any time"
        outputString = removeStopWords(testString)
        self.assertEqual(outputString, "time")
        
        
if __name__ == '__main__':
    stop_words = set(stopwords.words('english'))
    unittest.main()
