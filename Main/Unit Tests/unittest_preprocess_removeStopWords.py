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
        
        
if __name__ == '__main__':
    stop_words = set(stopwords.words('english'))
    unittest.main()
