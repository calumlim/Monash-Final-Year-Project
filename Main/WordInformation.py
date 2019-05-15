class WordInformation:
    """
    The WordInformation class stores information about a unigram.
    Each unique unigram in the dictionary will have a WordInformation
    object as its key in the dictionary.
    
    Attributes:
        MAX_RATING (int): The number of class ratings (normally 1-5 stars)

        tf (float[])    : Term frequency for each class rating
                                  
        tfidf (float[]) : The weighted score given for each class rating
    """

    
    def __init__(self, maxRating):
        """
        Every WordInformation when instantiated starts with 0 values for
        all its attribute array values.
        
        - The values in tf is incremented while the training data set
        is being read in.
        - The values in tfidf is computed after the whole training data
        set has been read.
        """
        self.MAX_RATING = maxRating
        self.tf = [0] * (self.MAX_RATING + 1)
        self.tfidf = [0] * (self.MAX_RATING + 1)           
        

    def getNumRatingsWordAppears(self):
        """
        Get the number of documents that the word appears in. For example,
        if the word "excellent" appears in reviews that are rated 4 and 5,
        this method will return 2.
        
        Returns:
            The number of documents that has the word.
        """
        count = 0
        for frequency in self.tf:
            if frequency != 0:
                count += 1
        return count


    def setTF(self, totalTerms):
        """
        Set the term frequency of the current unigram.

        Arguments:
            totalTerms(int[]): Total number of words that appear in
                               each class rating.
        """
        for i in range(1, self.MAX_RATING + 1):
            if totalTerms[i] > 0:
                self.tf[i] = self.tf[i]/totalTerms[i]


    def getTFIDF(self):
        """
        Returns:
            A copy array of the attribute tfidf.
        """
        copyArray = []
        for value in self.tfidf:
            copyArray.append(value)
        return copyArray

        
    def setTFIDF(self, idf):
        """
        Computes the tfidf (weighted score) for each class rating (1-5 stars).

        Arguments:
            idf (float): math.log( number of class ratings /
                                   getNumRatingsWordAppears() )
        """
        for i in range(1, len(self.tf)):
            self.tfidf[i] = self.tf[i] * idf
    

    def incrementFrequency(self, rating):
        """
        Increment a rating in tf by 1. This is called
        everytime the corresponding work occurs in the corpus.

        Arguments:
            rating (int): the class rating (1-5 stars) that the word appears in
        """
        self.tf[rating] += 1
