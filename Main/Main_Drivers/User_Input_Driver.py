import sys
sys.path.append("..")

from convert_csv_to_txt import convert
from segregate_txt_file import segregate
from sklearn.svm import LinearSVC

import preprocess
import main_score, main_svm

if __name__ == "__main__":
    """
    Script that trains a data set but only uses lemmatization, and uses
    Linear Support Vector Classifier (SVC) to predict a user input review.
    There is also a feature to print out the top N features from the
    input data set.
    """
    
    datasetCSV = "sample_dataset.csv" # csv data set to be trained
    rating_col = "A"
    review_col = "B"
    trainingFile = datasetCSV[:-3] + "txt"

    print("\nConverting .csv file to .txt")
    
    convert(datasetCSV, rating_col, review_col)

    print("\nConvert .csv file to .txt completed!")

    print("\nPreprocessing input data set file, using lemmatization only")
    
    preprocess.preprocess(trainingFile, "0010")

    print("\nPreprocessing completed!")

    print("\nFor Highest Score", end="")
    dictionary = main_score.getDictionary("dataset-preprocessed-03.txt",
                                          "with lemmatization")

    print("\nFor SVM", end="")
    tfidf_vector, tfidf_matrix = main_svm.computeTFIDF("dataset-preprocessed-03.txt",
                                                       "with lemmatization")
    classLabels = [1,2,3,4,5]
    svmModel = LinearSVC()
    svmModel.fit(tfidf_matrix, classLabels)

    print("\n===============================================================\n")

    
    N = int(input("\nEnter number of top features you would like to display: "))
    print()
    dictionary.printTopWords(N)

    while True:
        userInputReview = [input("Enter written review to predict: ")]
        new_tfidf_matrix = tfidf_vector.transform(userInputReview)
        predicted = svmModel.predict(new_tfidf_matrix)
        print("Predicted Rating: " + str(predicted[0]))
        print()
