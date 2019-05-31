import sys
sys.path.append("..")

from convert_csv_to_txt import convert
from segregate_txt_file import segregate
import preprocess
import main_score, main_svm, main_nb


if __name__ == "__main__":
    
    # VARIABLES CAN BE CHANGED, MORE INFO IN README.MD
    datasetCSV = "amazon_dataset.csv"
    rating_col = "A"
    review_col = "B"
    trainingPercentage = 0.8
    
    # DO NOT CHANGE THESE VARIABLES
    datasetTxtFile = datasetCSV[:-3] + "txt"
    trainingFile = "fileForTraining.txt"
    predictingFile = "fileForPredicting.txt"

    print("\nConverting .csv file to .txt")
    
    convert(datasetCSV, rating_col, review_col)

    print("\nConvert .csv file to .txt completed!")

    print("\nSegregating txt file, percentage used for training: ", trainingPercentage)

    segregate(datasetTxtFile, trainingPercentage)

    print("\nSegregating completed!")
    
    print("\nPreprocessing fileForTraining.txt, this may take a while..")
    
    preprocess.preprocess(trainingFile, "1111")

    print("\nPreprocessing complete! 4 txt files created")

    # run all 3 prediction models
    cmd = [main_nb.runMainNB(predictingFile),
           main_svm.runMainSVM(predictingFile),
           main_score.runMainScore(predictingFile)
          ]


