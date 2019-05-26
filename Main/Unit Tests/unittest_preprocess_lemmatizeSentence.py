import unittest
from nltk.corpus import wordnet
from nltk.stem.wordnet import WordNetLemmatizer
from nltk import word_tokenize, pos_tag
from collections import defaultdict


def lemmatizeSentence(inputSentence):
    """
    Lemmatize all the words in a given sentence.
    
    Arguments:
        inputSentence (str): A written review
        
    Returns:
        outputSentence (str): A written review with the words lemmatized
    """
    tag_map = defaultdict(lambda : wordnet.NOUN)
    tag_map['J'] = wordnet.ADJ
    tag_map['V'] = wordnet.VERB
    tag_map['R'] = wordnet.ADV
    
    outputSentence = []
    inputSentence = word_tokenize(inputSentence)

    for token, tag in pos_tag(inputSentence):
        lemma = lemmatizer.lemmatize(token, tag_map[tag[0]])
        outputSentence.append(lemma)

    return " ".join(outputSentence)


class MyTest(unittest.TestCase):
    
    def test_lemmatizeSentence(self):

        # Test cases that are expected to pass
        # FORMAT FOR TUPLE IN ARRAY -->>
        # (Input sentence, Expected output sentence)
        testCases = [("", ''),
                     ("originated", 'originate'),
                     ("products shines in many ways", 'product shine in many way'),
                     ("wolves are meanies", 'wolf be meany'),
                     ("loves loving loved", 'love love love'),
                     ("drawing draws drew", 'draw draw draw'),
                     ("running runs ran", 'run run run'),
                     ("studies studying studied", 'study study study'),
                     ("playing plays played", 'play play play'),
                     ("fire fires fired", 'fire fire fire'),
                     ("following follows followed", 'follow follow follow'),
                     ("a b c d e f g h i j k l m", 'a b c d e f g h i j k l m'),
                     ("n o p q r s t u v q x y z", 'n o p q r s t u v q x y z')
                    ]

        for test in testCases:
            testString = test[0]
            expectedOutput = test[1]
            self.assertEqual(lemmatizeSentence(testString), expectedOutput)

        # ----------------------------------------------------------------------------------------
        # Test cases that failed
        # FORMAT FOR TUPLE IN ARRAY -->>
        # (Input word, Expected output word)
        wronglyLemmatized = [("ies", 'ies'),
                             ("disappointed", 'disappoint'),
                             ("disappoints", 'disappoint')
                            ]

        stringFormat = '{:>15}{:>15}{:>15}'
        print('\n{:^45}'.format("Unexpected results from lemmatization"))
        print(stringFormat.format('Input', 'Expected', 'Output'))
        print( ("-") * 45 )
        for test in wronglyLemmatized:
            print(stringFormat.format(test[0], test[1], lemmatizeSentence(test[0])) )
        
if __name__ == '__main__':
    lemmatizer = WordNetLemmatizer()
    unittest.main()
