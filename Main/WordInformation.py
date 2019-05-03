class WordInformation:
    """
    The WordInformation class stores information about a unigram or bigram.
    Each unique n-gram in the dictionary will have a WordInformation
    object as its key in the dictionary.
    
    Attributes:
        MAX_RATING (int)        : The number of class ratings
                                  (normally 1-5 stars)

        ratingFrequency (int[]) : The number of times an n-gram appears
                                  in each class rating (1-5 stars).
                                  
        tfidf (int[])           : The weighted score given for each
                                  class rating (1-5 stars).     
    """

    
    def __init__(self):
        """
        Every WordInformation when instantiated starts with 0 values for
        all its attribute array values.
        
        - The values in ratingFrequency is incremented while the training
        data set is being read in.
        - The values in tfidf is computed after the whole training data
        set has been read.
        """
        MAX_RATING = 5
        self.ratingFrequency = [0] * (MAX_RATING + 1)
        self.tfidf = [0] * (MAX_RATING + 1)           
        

    def getNumRatingsWordAppears(self):
        """
        Get the number of documents that the word appears in. For example,
        if the word "excellent" appears in reviews that are rated 4 and 5,
        this method will return 2.
        
        Returns:
            The number of documents that has the word.
        """
        count = 0
        for frequency in self.ratingFrequency:
            if frequency != 0:
                count += 1
        return count


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
        self.tfidf = [i * idf for i in self.ratingFrequency]
    

    def incrementFrequency(self, rating):
        """
        Increment a rating in ratingFrequency by 1. This is called
        everytime the corresponding work occurs in the corpus.

        Arguments:
            rating (int): the class rating (1-5 stars) that the word appears in
        """
        self.ratingFrequency[rating] += 1
