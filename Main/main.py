from WordInformation import WordInformation
from Dictionary import Dictionary

def extractWords(filename):
    dictionary = Dictionary()
    reviewFile = open(filename, "r", encoding="utf-8-sig")
    for record in reviewFile:
        record = record.strip().split("\t")     # tab-delimited .txt file 
        dictionary.scanSentence(int(record[0]), record[1])
    reviewFile.close()
    return dictionary

    
def runTest(dictionary, filename):
    totalRecords = 0
    correctlyPredicted = 0
    reviewFile = open(filename, "r", encoding="utf-8-sig")
    
    for record in reviewFile:
        record = record.strip().split("\t") # tab-delimited .txt file
        totalRecords += 1
        if dictionary.predictRating(record[1]) == int(record[0]):
            correctlyPredicted += 1  
      
    print(correctlyPredicted, totalRecords)
    print("Accuracy: ", end="")
    print(correctlyPredicted/totalRecords)
    reviewFile.close()
    

if __name__ == "__main__":

    MAX_RATING = 5

    print("\nWith stop words and no lemmatization")
    wordDictionary = extractWords("dataset-preprocessed-01.txt")
    wordDictionary.computeTFIDF(MAX_RATING)
    runTest(wordDictionary, "dataset-amazon.txt")

    print("\nRemoved stop words")
    wordDictionary = extractWords("dataset-preprocessed-02.txt")
    wordDictionary.computeTFIDF(MAX_RATING)
    runTest(wordDictionary, "dataset-amazon.txt")

    print("\nWith lemmatization")
    wordDictionary = extractWords("dataset-preprocessed-03.txt")
    wordDictionary.computeTFIDF(MAX_RATING)
    runTest(wordDictionary, "dataset-amazon.txt")

    print("\nRemove stop words and has been lemmatized")
    wordDictionary = extractWords("dataset-preprocessed-04.txt")
    wordDictionary.computeTFIDF(MAX_RATING)
    runTest(wordDictionary, "dataset-amazon.txt")
