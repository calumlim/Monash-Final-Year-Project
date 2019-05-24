import sys
sys.path.append("..")
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn import metrics
from preprocess import cleanSentence
import numpy
import os
import pandas
     
        
def extractWords(datasetFile):
    outputArray = [""] * 5
    reviewFile = open(datasetFile, "r", encoding="utf-8-sig")
    for record in reviewFile:
        record = record.strip("\n").split("\t")
        rating = int(record[0])
        outputArray[rating - 1] += record[1] + " "
    return outputArray


def runTests(corpusToTrain, reviewsToPredictFile):
    classLabels = [1,2,3,4,5]
    tfidf_vector = TfidfVectorizer(smooth_idf = True, use_idf = True)

    tfidf_matrix = tfidf_vector.fit_transform(corpusToTrain)
    feature_names = tfidf_vector.get_feature_names()

    actual_ratings = []
    written_reviews_to_predict = []

    reviewFile = open(reviewsToPredictFile, "r", encoding="utf-8-sig")
    for record in reviewFile:
        record = record.strip().split("\t")
        textReview = cleanSentence(record[1])
        actual_ratings.append(int(record[0]))
        written_reviews_to_predict.append(textReview)

    nbModel = LinearSVC()
    nbModel.fit(tfidf_matrix, classLabels)
    
    new_tfidf_matrix = tfidf_vector.transform(written_reviews_to_predict)
    predicted = nbModel.predict(new_tfidf_matrix)

    print("Accuracy:", round(numpy.mean(predicted == actual_ratings), 2))
    print(metrics.classification_report(actual_ratings,
                                        predicted,
                                        classLabels))


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

if __name__ == "__main__":
    
    print("\nWith stop words and no lemmatization")
    preprocessedFile = os.path.join(os.getcwd(), "..", "dataset-preprocessed-01.txt")
    writtenReviews = extractWords(preprocessedFile)
    testDataset = os.path.join(os.getcwd(), "..", "34661.txt")
    runTests(writtenReviews, testDataset)

    print("\nRemoved stop words")
    preprocessedFile = os.path.join(os.getcwd(), "..", "dataset-preprocessed-02.txt")
    writtenReviews = extractWords(preprocessedFile)
    testDataset = os.path.join(os.getcwd(), "..", "34661.txt")
    runTests(writtenReviews, testDataset)

    print("\nWith lemmatization")
    preprocessedFile = os.path.join(os.getcwd(), "..", "dataset-preprocessed-03.txt")
    writtenReviews = extractWords(preprocessedFile)
    testDataset = os.path.join(os.getcwd(), "..", "34661.txt")
    runTests(writtenReviews, testDataset)

    print("\nRemove stop words and has been lemmatized")
    preprocessedFile = os.path.join(os.getcwd(), "..", "dataset-preprocessed-04.txt")
    writtenReviews = extractWords(preprocessedFile)
    testDataset = os.path.join(os.getcwd(), "..", "34661.txt")
    runTests(writtenReviews, testDataset)
