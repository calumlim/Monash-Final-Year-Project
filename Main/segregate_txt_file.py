
def segregate(txtFile, trainingPercentage = 0.8):
    """
    Segregate txt file into two text files. One for training, and the
    other for predicting.

    Arguments:
        txtFile (str): The name of the input data set .txt file
        trainingPercentage (float): the percentage of .txt file to be
                                    used for training
    """
    reviews = []
    for i in range(6):
        reviews.append([])

    # append all reviews into array
    file = open(txtFile, "r", errors="ignore", encoding="utf-8-sig")
    for record in file:
        row = record.split("\t")

        rating = int(row[0])
        review = row[1].strip()
        reviews[rating].append(review)
    file.close()

    reviewsForTraining = ""
    reviewsForPredicting = ""

    for i in range(1, 6):
        numOfRowsForTraining = int(round(trainingPercentage * len(reviews[i])))
        for j in range(numOfRowsForTraining):
            reviewsForTraining += str(i) + "\t" + reviews[i][j] + "\n"
        for j in range(numOfRowsForTraining, len(reviews[i])):
            reviewsForPredicting += str(i) + "\t" + reviews[i][j] + "\n"
            count += 1
    
    file = open("fileForTraining.txt", "w", errors="ignore")
    file.write(reviewsForTraining)
    file.close()
    
    file = open("fileForPredicting.txt", "w", errors="ignore")
    file.write(reviewsForPredicting)
    file.close()
