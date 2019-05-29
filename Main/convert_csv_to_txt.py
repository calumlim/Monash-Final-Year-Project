import csv

def convert(filename, ratingCol, textReviewCol):
    ratingCol = ord(ratingCol.lower()) - 97
    textReviewCol = ord(textReviewCol.lower()) - 97
    
    outputTxtFilename = filename.split(".")[0] + ".txt"
    outputString = ""

    with open(filename, 'r', errors="ignore") as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            outputString += row[ratingCol] + "\t" + row[textReviewCol] + "\n"
    csvFile.close()

    txtFile = open(outputTxtFilename, 'w')
    txtFile.write(outputString.rstrip())
    txtFile.close()
    
    return


    
    
