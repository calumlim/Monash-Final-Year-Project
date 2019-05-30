import sys
sys.path.append("..")

from convert_csv_to_txt import convert
from segregate_txt_file import segregate
import preprocess
import main_score, main_svm, main_nb


if __name__ == "__main__":
    
    datasetCSV = "amazon_dataset.csv"
    rating_col = "A"
    review_col = "B"
    datasetTxtFile = datasetCSV[:-3] + "txt"
    trainingPercentage = 0.8
    trainingFile = "fileForTraining.txt"
    predictingFile = "fileForPredicting.txt"

    print("\nConverting .csv file to .txt")
    
    convert(datasetCSV, rating_col, review_col)

    print("\nConvert .csv file to .txt completed!")

    print("\nSegregating txt file, percentage used for training: ", trainingPercentage)

    segregate(datasetTxtFile, trainingPercentage)

    print("\nSegregating completed!")
    
    print("\nPreprocessing fileForTraining.txt, this may take a while..")
    
    preprocess.preprocess(trainingFile)

    print("\nPreprocessing complete! 4 txt files created")
  
    cmd = [main_nb.runMainNB(predictingFile),
           main_svm.runMainSVM(predictingFile),
           main_score.runMainScore(predictingFile)
          ]


