# Monash-Final-Year-Project
Monash Computer Science Final Year Project: Rating prediction based on user text review.
In this project, we are predicting user ratings based on written reviews. We will be using unigrams as our main
feature extraction method. TF-IDF weighting technique will be used to weigh each unigrams. Then finally, Naive Bayes,
SVM, and a Highest Score algorithm is used to predict the rating.


## Libraries and Frameworks used
- [NLTK](https://www.nltk.org/)
- [scikit-learn](https://scikit-learn.org/stable/)
- [Pandas](https://pandas.pydata.org/)
- [Numpy](https://www.numpy.org/)


## Installation
First step is to clone, or download the software. To clone the project, type in the command "git clone https://github.com/calumlim/Monash-Final-Year-Project.git".
Or you can just download the system by downloading the ZIP file in our project's GitHub web page.

Next, to install the libraries, frameworks, and subpackages needed to run our code, execute the Python script
named "download_modules.py". However, pip needs to be installed onto your machine, which is needed
to install libraries and frameworks.

Inside the script, "download_modules.py", contains the commands to install the required tools to run exeute certain code.


## How to use
There are two main driver scripts, both located inside the folder Main_Drivers. 
1) Run_Default_Prediction_Test.py
2) User_Input_Driver.py
It is recommended to run these files using Python Shell, rather than command line (so it does not close after finish executing). 

1) Run_Default_Prediction_Test.py script is to run our experimental setup, as explained in our report. The output
wil be in txt files. The first 4 variables can be changed are:
- datasetCSV : the name of the data set (must be in .csv format)
- rating_col : the letter of the column for the rating (can be lowercase or uppercase)
- review_col : the letter of the column for the review (can be lowercase or uppercase)
- trainingPercentage: the percentage used for training (must be float <= 1.0 and > 0.0)

2) User_Input_Driver.py script is to train a given input data set. The preprocessing setting
for this will only be lemmatization only. Once the training is done, the program will
prompt the user for an integer N, to print out the top N features. This value can be 0. Then the user can
keep writing a written review, which will then be predicted using SVM.

The first 3 variables can be changed are:
- datasetCSV : the name of the data set (must be in .csv format)
- rating_col : the letter of the column for the rating (can be lowercase or uppercase)
- review_col : the letter of the column for the review (can be lowercase or uppercase)


## Unit Tests
The unit test scripts are located in the folder Unit Tests.
It is recommended to run these files using Python Shell, rather than command line (so it does not close after finish executing). 


## Credits
Credits to Dr. Soon Lay Ki, our project supervisor, for guiding us throughout our project. She played a very important 
role in the research and development of our final year project. Without her, this project may very well be not possible at all.


## License
Monash University Malaysia © Julian Chong & Calum Lim
