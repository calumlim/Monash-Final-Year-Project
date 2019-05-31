import sys
sys.path.append("..")

from Classes.Dictionary import Dictionary
from sklearn import metrics
from preprocess import cleanSentence
import numpy as np
import os


def getDictionary(inputDataset, outputFileName):
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
    print("\nComputing TF-IDF values for file - ", outputFileName)
    wordDictionary = Dictionary(5)
    wordDictionary.extractWords(inputDataset)
    wordDictionary.computeTF()
    wordDictionary.computeTFIDF()
    return wordDictionary    

    
def runTests(inputDataset, reviewsToPredictFile, outputFileName):
    """
    Run test with a given Dictionary instance, and a dataset to predict.
    Results will be printed out.
    
    Arguments:
        dictionary (Dictionary): Dictionary instance that has the tf-idf
                                 scores for all of the unique unigrams.
        datasetToTestOn (str): Name of a dataset text file that is used
                               to predict ratings.
    """
    dictionary = getDictionary(inputDataset, outputFileName)
    print(len(dictionary.dictionary))
    actualRatings = []
    predictedRatings = []
    classLabels = [1,2,3,4,5]
    
    reviewFile = open(reviewsToPredictFile, "r", encoding="utf-8-sig", errors="ignore")

    # Go through all of the reviews in the dataset to predict,
    # append the actual rating, and the predicted rating of that review
    for record in reviewFile:
        record = record.strip().split("\t")
        textReview = cleanSentence(record[1])
        actualRatings.append(int(record[0]))
        predictedRatings.append(dictionary.predictRating(textReview))
    reviewFile.close()

    # output the results into a .txt file
    outputFileName = "Highest Score Algorithm - " + outputFileName + ".txt"
    outputString = outputFileName[:-3]
    accuracy = np.sum(np.array(predictedRatings) == np.array(actualRatings))
    accuracy /= len(actualRatings)
    outputString += "\nAccuracy:" + str(round(accuracy, 2)) + "\n"

    # Other metrics calculated using sklearn metrics library
    outputString += metrics.classification_report(actualRatings,
                                        predictedRatings,
                                        classLabels)
    outputFile = open(outputFileName, "w")
    outputFile.write(outputString)
    outputFile.close()

def runMainScore(testDataset):
    print("\nRunning test using Highest Score Algorithm")
    
    preprocessedFile = "dataset-preprocessed-01.txt"
    runTests(preprocessedFile, testDataset, "With stop words and no lemmatization")

    preprocessedFile = "dataset-preprocessed-02.txt"
    runTests(preprocessedFile, testDataset, "Removed stop words")

    preprocessedFile = "dataset-preprocessed-03.txt"
    runTests(preprocessedFile, testDataset, "With lemmatization")

    preprocessedFile = "dataset-preprocessed-04.txt"
    runTests(preprocessedFile, testDataset, "Remove stop words and has been lemmatized")

    print("\nCompleted! Output files starts with Highest Score Algorithm -")
    print("===================================================================")
