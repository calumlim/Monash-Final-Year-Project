from Dictionary import Dictionary

def getDictionary(inputDataset):
    wordDictionary = Dictionary(MAX_RATING)
    wordDictionary.extractWords(inputDataset)
    wordDictionary.computeTF()
    wordDictionary.computeTFIDF()
    
    return wordDictionary    

    
def runTest(dictionary, datasetToTestOn):
    totalRecords = 0
    correctlyPredicted = 0
    reviewFile = open(datasetToTestOn, "r", encoding="utf-8-sig")
    
    for record in reviewFile:
        totalRecords += 1
        record = record.strip().split("\t") # tab-delimited .txt file
        if dictionary.predictRating(record[1]) == int(record[0]):
            correctlyPredicted += 1  
      
    print(correctlyPredicted, totalRecords)
    print("Accuracy: ", end="")
    print(correctlyPredicted/totalRecords)
    reviewFile.close()
    

if __name__ == "__main__":

    MAX_RATING = 5
    
    print("\nWith stop words and no lemmatization")
    wordDictionary = getDictionary("dataset-preprocessed-01.txt")
    runTest(wordDictionary, "dataset-amazon.txt")

    print("\nRemoved stop words")
    wordDictionary = getDictionary("dataset-preprocessed-02.txt")
    runTest(wordDictionary, "dataset-amazon.txt")

    print("\nWith lemmatization")
    wordDictionary = getDictionary("dataset-preprocessed-03.txt")
    runTest(wordDictionary, "dataset-amazon.txt")

    print("\nRemove stop words and has been lemmatized")
    wordDictionary = getDictionary("dataset-preprocessed-04.txt")
    runTest(wordDictionary, "dataset-amazon.txt")
