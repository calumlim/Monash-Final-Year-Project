import csv

def convert(filename, ratingCol, textReviewCol):
    """
    Convert a .csv file to .txt file

    Arguments:
        filename (str): name of .csv file
        ratingCol (str): letter of the column for rating
        textReviewCol (str): letter of the column for written review
    """
    ratingCol = ord(ratingCol.lower()) - 97
    textReviewCol = ord(textReviewCol.lower()) - 97
    
    outputTxtFilename = filename.split(".")[0] + ".txt"
    outputString = ""

    with open(filename, 'r', errors="ignore", encoding="utf-8-sig") as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            if row[ratingCol] != "" and row[textReviewCol] != "":
                outputString += row[ratingCol] + "\t" + row[textReviewCol] + "\n"
    csvFile.close()

    txtFile = open(outputTxtFilename, 'w', errors="ignore")
    txtFile.write(outputString.rstrip())
    txtFile.close()
    
    return
    
    
