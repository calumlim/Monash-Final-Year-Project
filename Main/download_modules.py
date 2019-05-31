import os

# COMMAND LINE INSTRUCTIONS TO INSTALL LIBRARIES
os.system("pip install nltk")
os.system("pip install sklearn")
os.system("pip install pandas")
os.system("pip install numpy")

import nltk

# TO INSTALL NLTK SUBPACKAGES
nltk.download("stopwords")
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
