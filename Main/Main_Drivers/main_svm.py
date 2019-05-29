import sys
sys.path.append("..")
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn import metrics
from preprocess import cleanSentence
import numpy
import os
import pandas
     
        
def extractWords(inputDataset):
    """
    Reads in a txt file and adds each review into different index of
    an array, based on the rating of the review. E.g. all the written
    review with 3 star rating will be combined into a string and
    stored into the 3rd index (index 2).

    Arguments:
        inputDataset (str): name of dataset txt file
    """
    outputArray = [""] * 5
    reviewFile = open(inputDataset, "r", encoding="utf-8-sig")
    for record in reviewFile:
        record = record.strip("\n").split("\t")
        rating = int(record[0])
        outputArray[rating - 1] += record[1] + " "
    reviewFile.close()
    return outputArray


def computeTFIDF(inputDataset, outputFileName):
    """
    Compute TF-IDF values.

    Arguments:
        inputDataset (str): name of the dataset txt file
    
    Returns:
        tfidf_vector : a TfidfVectorizer object
        tfidf_vector : the feature matrix of the input data set
    """
    print("\nComputing TF-IDF values for file - ", outputFileName)
    corpusToTrain = extractWords(inputDataset)
    tfidf_vector = TfidfVectorizer(smooth_idf = True, use_idf = True)
    tfidf_matrix = tfidf_vector.fit_transform(corpusToTrain)
    return [tfidf_vector, tfidf_matrix]


def runTests(inputDataset, reviewsToPredictFile, outputFileName):
    """
    Run test using the inputDataset. Prediction model being used is
    Linear Support Vector Classifier.

    Arguments:
        inputDataset (str): the input data set to be used for trainig
        reviewsToPredictFile (str): the data set file to be used for prediction
        outputFileName (str): name of the file the results will be printed to
    """
    classLabels = [1,2,3,4,5]

    tfidf_vector, tfidf_matrix = computeTFIDF(inputDataset, outputFileName)

    # fit the tf-idf values into the prediction model (SVM)
    svmModel = LinearSVC()
    svmModel.fit(tfidf_matrix, classLabels)

    # store the actual ratings and written reviews to predict
    actual_ratings = []
    written_reviews_to_predict = []

    reviewFile = open(reviewsToPredictFile, "r", encoding="utf-8-sig")
    for record in reviewFile:
        record = record.strip().split("\t")
        textReview = cleanSentence(record[1])
        actual_ratings.append(int(record[0]))
        written_reviews_to_predict.append(textReview)

    # create new matrix for the reviews to be predicted,
    # and start predicting
    new_tfidf_matrix = tfidf_vector.transform(written_reviews_to_predict)
    predicted = svmModel.predict(new_tfidf_matrix)

    # output the results into a .txt file
    outputFileName = "SVM (Linear SVC) - " + outputFileName + ".txt"
    outputString = outputFileName[:-3]
    outputString += "\nAccuracy:" + str(round(numpy.mean(predicted == actual_ratings), 2)) + "\n"
    outputString += metrics.classification_report(actual_ratings,
                                        predicted,
                                        classLabels)
    outputFile = open(outputFileName, "w")
    outputFile.write(outputString)
    outputFile.close()


def printTopWords(tfidfMatrix, featureNames, N):
    for i in range(5):
        print("Top " + str(N) + " words for class rating " + str(i + 1))
        print("--------------------------------------")
        row = numpy.squeeze(tfidfMatrix[i].toarray())

        topn_ids = numpy.argsort(row)[::-1][:N]
        top_feats = [(featureNames[j], row[j]) for j in topn_ids]
        df = pandas.DataFrame(top_feats)
        print(df)
        print()

def runMainSVM(testDataset):
    print("Running test using Linear Support Vector")
    
    preprocessedFile = os.path.join(os.getcwd(), "..", "dataset-preprocessed-01.txt")
    testDataset = os.path.join(os.getcwd(), "..", testDataset)
    runTests(preprocessedFile, testDataset, "With stop words and no lemmatization")

    preprocessedFile = os.path.join(os.getcwd(), "..", "dataset-preprocessed-02.txt")
    testDataset = os.path.join(os.getcwd(), "..", testDataset)
    runTests(preprocessedFile, testDataset, "Removed stop words")

    preprocessedFile = os.path.join(os.getcwd(), "..", "dataset-preprocessed-03.txt")
    testDataset = os.path.join(os.getcwd(), "..", testDataset)
    runTests(preprocessedFile, testDataset, "With lemmatization")

    preprocessedFile = os.path.join(os.getcwd(), "..", "dataset-preprocessed-04.txt")
    testDataset = os.path.join(os.getcwd(), "..", testDataset)
    runTests(preprocessedFile, testDataset, "Remove stop words and has been lemmatized")

    print("\nCompleted! Output files starts with SVM (Linear SVC) -")

if __name__ == "__main__":
    
    runMainSVM("5.txt")
