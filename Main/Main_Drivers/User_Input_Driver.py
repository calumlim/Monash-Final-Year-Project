import sys
sys.path.append("..")

from convert_csv_to_txt import convert
from segregate_txt_file import segregate
import preprocess
import main_score, main_svm

if __name__ == "__main__":
    
    datasetCSV = "sample_dataset.csv"
    rating_col = "A"
    review_col = "B"
    trainingFile = datasetCSV[:-3] + "txt"

    print("\nConverting .csv file to .txt")
    
    convert(datasetCSV, rating_col, review_col)

    print("\nConvert .csv file to .txt completed!")

    print("\nPreprocessing input data set file, using lemmatization only")
    
    preprocess.preprocess(trainingFile, "0010")

    print("\nPreprocessing completed!")

    dictionary = main_score.getDictionary("dataset-preprocessed-03.txt",
                                          "with lemmatization")

    tfidf_vector, tfidf_matrix = main_svm.computeTFIDF("dataset-preprocessed-03.txt",
                                                       "with lemmatization")

    print("\n===============================================================\n")

    
    N = int(input("\nEnter number of top features you would like to display: "))
    print()
    dictionary.printTopWords(N)

    while True:
        userInputReview = input("Enter written review to predict: ")


