from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re

def cleanSentence(inputSentence):
    """
    Four regular expression rules that is used to preprocess the written
    reviews in the data set.
    1 - remove punctuations.
    2 - remove ellipsis.
    3 & 4 - Make full stops separate from words

    Arguments:
        inputSentence (str): a written review from the input data set.

    Returns:
        sentence (str): cleaned written review
    """
    sentence = inputSentence.strip()
    sentence = sentence.lower()
    
    # 1 remove punctutations
    sentence = re.sub(r'[‚,<>?/:;"{}\-_+=)()*&^%$#@!`~|\\]', r' ', sentence)

    # 2 remove any ellipsis
    sentence = re.sub(r'(\.(\.)+)', r' ', sentence) 

    # 3 separate fullstops from the preceding word
    # e.g. "Hello." --> "Hello ."
    sentence = re.sub(r'([a-z1-9]){1}\.', r'\g<1> .', sentence)

    # 4 separate fullstops from the following word
    # e.g. ".Hello" --> ". Hello"
    sentence = re.sub(r'\.([a-z1-9]){1}', r'. \g<1>', sentence)
    
    return sentence.strip()


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
    reviewFile = open("dataset-amazon.txt", "r", encoding="utf-8-sig")
    outputString01 = ""     # without removing stopwords and lemmatization
    outputString02 = ""     # remove stopwords
    outputString03 = ""     # lemmatization
    outputString04 = ""     # remove stopwords and lemmatization
    
    for record in reviewFile:
        record = record.strip().split("\t") # tab-delimited .txt file
        
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
