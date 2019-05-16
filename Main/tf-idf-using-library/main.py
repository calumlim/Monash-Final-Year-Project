from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn import metrics
import numpy
import os
     
        
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
        actual_ratings.append(int(record[0]))
        written_reviews_to_predict.append(record[1])

    nbModel = MultinomialNB()
    nbModel.fit(tfidf_matrix, classLabels)
    
    new_tfidf_matrix = tfidf_vector.transform(written_reviews_to_predict)
    predicted = nbModel.predict(new_tfidf_matrix)

    totalReviews = 0
    correctlyPredicted = 0
    i = 0
    dic = zip(written_reviews_to_predict, predicted)
    for predictedReview in dic:
        if predictedReview[1] == actual_ratings[i]:
            correctlyPredicted += 1
        totalReviews += 1
        i += 1
        
    print(totalReviews, correctlyPredicted)
    print(correctlyPredicted / totalReviews)
    #print(numpy.mean(predicted == actual_ratings))
    print(metrics.classification_report(actual_ratings,
                                        predicted,
                                        classLabels))
    

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
