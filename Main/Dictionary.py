import math
from WordInformation import WordInformation

class Dictionary:
    """
    Dictionary class that stores unigrams and bigrams. The key/value pair
    is n-gram : WordInformation, where WordInformation is a class.

    Attributes:
        dictionary (dictionary): The dictionary to store n-grams
    """

    def __init__(self):
        """
        Constructor method.
        """
        self.dictionary = {}


    def addItem(self, key):
        """
        Add a new n-gram to the dictionary. Method should not be called
        if the key already exist in the dictionary.

        Raises:
            Exception: Raises an exception is key already exist in the
                       dictionary

        Arguments:
            key (str): an n-gram to be added to the dictionary
        """
        if key in self.dictionary:
            raise Exception("Key already exist in dictionary")
        self.dictionary[key] = WordInformation()
        
        
    def scanSentence(self, rating, writtenReview):
        """
        Add unigrams, then bigrams from a written review.

        Arguments:
            rating (int): The rating given for a written review
            writtenReview (str): The written review
        """
        self.addUnigrams(rating, writtenReview)
        self.addBigrams(rating, writtenReview)


    def addUnigrams(self, rating, writtenReview):
        """"
        Add unigrams into a dictionary.

        Arguments:
            rating (int): The rating given for a written review
            writtenReview (str): The written review
        """
        sentence = writtenReview.split()
        for word in sentence:
            if word != ".":
                if word not in self.dictionary:
                    self.addItem(word)
                self.dictionary[word].incrementFrequency(rating)


    def addBigrams(self, rating, writtenReview):
        """"
        Add bigrams into a dictionary.

        Arguments:
            rating (int): The rating given for a written review
            writtenReview (str): The written review
        """
        sentence = writtenReview.split()
        
        for i in range(len(sentence) - 1):
            currentWord = sentence[i]
            nextWord = sentence[i]
            bigram = currentWord + " " + nextWord
            
            if currentWord != "." and nextWord != ".":
                if bigram not in self.dictionary:
                    self.addItem(bigram)
                self.dictionary[bigram].incrementFrequency(rating)


    def computeTFIDF(self, MAX_RATING):
        """
        Compute the TFIDF scores for each n-gram in the dictionary

        Arguments:
            MAX_RATING (int): The maximum rating given in the whole data set
        """
        for word in self.dictionary:
            numOfAppearance = self.dictionary[word].getNumRatingsWordAppears()
            idf = math.log( (MAX_RATING + 1) / (numOfAppearance + 1) )
            self.dictionary[word].setTFIDF(idf)


    def predictRating(self, writtenReview):
        totalKeywords = [0] * 6
        totalScores = [0] * 6
        sentence = writtenReview.split()
        
        for word in sentence:
            if word in self.dictionary:
                wordScores = self.dictionary[word].getTFIDF()
                for i in range(1, len(totalScores)):
                    if wordScores[i] != 0:
                        totalKeywords[i] += 1
                        totalScores[i] += wordScores[i]

        indexOfHighestScore = 1
        for i in range(1, len(totalKeywords)):
            if totalScores[i] != 0 and totalKeywords[i] != 0:
                totalScores[i] /= totalKeywords[i]
                if totalScores[i] > totalScores[indexOfHighestScore]:
                    indexOfHighestScore = i
      
        return indexOfHighestScore
