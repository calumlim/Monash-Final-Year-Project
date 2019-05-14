from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re

def cleanSentence(inputSentence):
    """
    First change all uppercase characters to lowercase. Then, three regular expression rules that is used to 
    preprocess the written reviews in the data set.
    1 - Remove punctuations.
    2 - Remove any two or more whitespaces together
    3 - Remove any whitespace from the start or end of a sentence

    Arguments:
        inputSentence (str): a written review from the input data set.

    Returns:
        sentence (str): cleaned written review
    """
    sentence = inputSentence.strip()
    sentence = sentence.lower()
    
    # 1 remove punctutations
    sentence = re.sub(r'[.‚,<>?/:;"{}\-_+=)()*&^%$#@!`~|\\]', r' ', sentence)

    # 2 remove two or more whitespaces that are together
    sentence = re.sub(r'[ ]{2,}', r' ', sentence)

    # 3 remove whitespace from start or end of sentence
    sentence = re.sub('(^ )|( $)*', r'', sentence)
    
    return sentence


def removeStopWords(inputSentence):
    """
    Arguments:
        inputSentence (str): A written review

    Returns:
        outputSentence (str): The written review with stop words filtered out
    """
    outputSentence = []
    inputSentence = inputSentence.split()

    for word in inputSentence:
        if word not in stop_words:
            outputSentence.append(word)
    
    return " ".join(outputSentence)


def lemmatizeSentence(inputSentence):
    """
    Arguments:
        inputSentence (str): A written review
        
    Returns:
        outputSentence (str): A written review with the words lemmatized
    """
    outputSentence = []
    inputSentence = inputSentence.split()

    for word in inputSentence:
        outputSentence.append(lemmatizer.lemmatize(word))

    return " ".join(outputSentence)


def preprocess():
    reviewFile = open("amazon-consumer-review.txt", "r", encoding="latin-1")
    outputString01 = ""     # without removing stopwords and lemmatization
    outputString02 = ""     # remove stopwords
    outputString03 = ""     # lemmatization
    outputString04 = ""     # remove stopwords and lemmatization
    
    for record in reviewFile:
        record = record.strip().split("\t") # tab-delimited .txt file
        if len(record)==2:
            outputString01 += record[0] + "\t"  
            outputString02 += record[0] + "\t"   
            outputString03 += record[0] + "\t"  
            outputString04 += record[0] + "\t"

            cleanedWriting = cleanSentence(record[1])
            outputString01 += cleanedWriting + "\n"
            outputString02 += removeStopWords(cleanedWriting) + "\n"
            outputString03 += lemmatizeSentence(cleanedWriting) + "\n"
            outputString04 += lemmatizeSentence(removeStopWords(cleanedWriting)) + "\n"

    reviewFile.close()
    
    outputFile = open("dataset-preprocessed-01.txt", "w", encoding="utf-8-sig")
    outputFile.write(outputString01.rstrip())
    outputFile.close()

    outputFile = open("dataset-preprocessed-02.txt", "w", encoding="utf-8-sig")
    outputFile.write(outputString02.rstrip())
    outputFile.close()

    outputFile = open("dataset-preprocessed-03.txt", "w", encoding="utf-8-sig")
    outputFile.write(outputString03.rstrip())
    outputFile.close()

    outputFile = open("dataset-preprocessed-04.txt", "w", encoding="utf-8-sig")
    outputFile.write(outputString04.rstrip())
    outputFile.close()


if __name__ == "__main__":
    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer() 
    preprocess()
