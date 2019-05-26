from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.stem.wordnet import WordNetLemmatizer
from nltk import word_tokenize, pos_tag
from collections import defaultdict
import re

def removeUselessRows(rawDatasetFilename):
    """
    Filter out any rows that do not have a given rating, or a
    do not have a text review (empty review). It OVERRIDES the
    old dataset file with a new cleaned one.
    Arguments:
        rawDatasetFilename (str): the dataset file in .txt format
    """
    outputString = ""
    file = open(rawDatasetFilename, "r", encoding="utf-8-sig", errors="ignore")
    
    for record in file:
        record = record.strip().split("\t")
        # if record has a given rating, and # if the text review is not empty
        if len(record) == 2 and len(record[1]) > 0: 
            outputString += record[0] + "\t" + record[1] + "\n"
                
    file.close()

    newCleanedFile = open(rawDatasetFilename, "w", encoding="utf-8-sig")
    newCleanedFile.write(outputString.rstrip())
    newCleanedFile.close()


def cleanSentence(inputSentence):
    """
    First change all uppercase characters to lowercase. Then, three regular
    expression rules that is used to preprocess the written reviews in the data set.
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
    sentence = re.sub(r'[.‚,<>?/:;"{}\-_+=)()*&^%$#@!`~|\\\'\[\]]', r' ', sentence)

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
    Lemmatize all the words in a given sentence.
    
    Arguments:
        inputSentence (str): A written review
        
    Returns:
        outputSentence (str): A written review with the words lemmatized
    """
    tag_map = defaultdict(lambda : wordnet.NOUN)
    tag_map['J'] = wordnet.ADJ
    tag_map['V'] = wordnet.VERB
    tag_map['R'] = wordnet.ADV
    
    outputSentence = []
    inputSentence = word_tokenize(inputSentence)

    for token, tag in pos_tag(inputSentence):
        lemma = lemmatizer.lemmatize(token, tag_map[tag[0]])
        outputSentence.append(lemma)

    return " ".join(outputSentence)


def preprocess(rawDatasetFilename):
    """
    Reads in a text file that is tab-delimited, which is information
    separated by a tab, and one record per line. Any text review that
    is empty after being mutated by cleanSentence(), will be excluded
    from the output text file.
    Arguments:
        rawDatasetFile (str): the dataset file in .txt format
    """
    rawDatasetFile = open(rawDatasetFilename, "r", encoding="utf-8-sig")
    outputString01 = ""     # without removing stopwords and lemmatization
    outputString02 = ""     # remove stopwords
    outputString03 = ""     # lemmatization
    outputString04 = ""     # remove stopwords and lemmatization
    
    for record in rawDatasetFile:
        record = record.strip().split("\t") # tab-delimited .txt file
        
        cleanedWriting = cleanSentence(record[1])

        # if the text review is not empty after cleaning, and after removing stop words
        if len(cleanedWriting) > 0 and len(removeStopWords(cleanedWriting)) > 0:     
            outputString01 += record[0] + "\t" + cleanedWriting + "\n"
            outputString02 += record[0] + "\t" + removeStopWords(cleanedWriting) + "\n"
            outputString03 += record[0] + "\t" + lemmatizeSentence(cleanedWriting) + "\n"
            outputString04 += record[0] + "\t" + lemmatizeSentence(removeStopWords(cleanedWriting)) + "\n"

    rawDatasetFile.close()
    
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
    removeUselessRows("5.txt")
    preprocess("5.txt")
