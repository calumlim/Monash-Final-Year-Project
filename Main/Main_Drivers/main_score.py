import sys
sys.path.append("..")

from Classes.Dictionary import Dictionary
from sklearn import metrics
from preprocess import cleanSentence
import numpy as np
import os


def getDictionary(inputDataset):
    """
    Open a dataset with given ratings and written reviews, then
    extract unigrams and compute the TF-IDF.
    
    Arguments:
        inputDatset (str): The file name of the dataset text file to train
    Return:
        wordDictionary (Dictionary): Dictionary instance that stores
                                     unigrams and its information such as
                                     tf-idf score, number of appearance in
                                     different documents, etc.
    """
    wordDictionary = Dictionary(MAX_RATING)
    wordDictionary.extractWords(inputDataset)
    wordDictionary.computeTF()
    wordDictionary.computeTFIDF()
    return wordDictionary    

    
def runTest(dictionary, datasetToTestOn):
    """
    Run test with a given Dictionary instance, and a dataset to predict.
    Results will be printed out.
    
    Arguments:
        dictionary (Dictionary): Dictionary instance that has the tf-idf
                                 scores for all of the unique unigrams.
        datasetToTestOn (str): Name of a dataset text file that is used
                               to predict ratings.
    """
    actualRatings = []
    predictedRatings = []
    classLabels = [1,2,3,4,5]
    
    reviewFile = open(datasetToTestOn, "r", encoding="utf-8-sig")

    # Go through all of the reviews in the dataset to predict,
    # append the actual rating, and the predicted rating of that review
    for record in reviewFile:
        record = record.strip().split("\t")
        textReview = cleanSentence(record[1])
        actualRatings.append(int(record[0]))
        predictedRatings.append(dictionary.predictRating(textReview))
    reviewFile.close()

    # Percentage of correctly predicted ratings
    accuracy = np.sum(np.array(predictedRatings) == np.array(actualRatings))
    accuracy /= len(actualRatings)
    print("Accuracy:", round(accuracy, 2))

    # Other metrics calculated using sklearn metrics library
    print(metrics.classification_report(actualRatings,
                                        predictedRatings,
                                        classLabels))


if __name__ == "__main__":

    MAX_RATING = 5
    
    print("\nWith stop words and no lemmatization")
    preprocessedFile = os.path.join(os.getcwd(), "..", "dataset-preprocessed-01.txt") 
    wordDictionary = getDictionary(preprocessedFile)
    testDataset = os.path.join(os.getcwd(), "..", "5.txt")
    runTest(wordDictionary, testDataset)

    print("\nRemoved stop words")
    preprocessedFile = os.path.join(os.getcwd(), "..", "dataset-preprocessed-02.txt") 
    wordDictionary = getDictionary(preprocessedFile)
    testDataset = os.path.join(os.getcwd(), "..", "5.txt")
    runTest(wordDictionary, testDataset)

    print("\nWith lemmatization")
    preprocessedFile = os.path.join(os.getcwd(), "..", "dataset-preprocessed-03.txt") 
    wordDictionary = getDictionary(preprocessedFile)
    testDataset = os.path.join(os.getcwd(), "..", "5.txt")
    runTest(wordDictionary, testDataset)

    print("\nRemove stop words and has been lemmatized")
    preprocessedFile = os.path.join(os.getcwd(), "..", "dataset-preprocessed-04.txt") 
    wordDictionary = getDictionary(preprocessedFile)
    testDataset = os.path.join(os.getcwd(), "..", "5.txt")
    runTest(wordDictionary, testDataset)
