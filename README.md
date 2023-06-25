# BigData_PYSPARK_WordCloud
Calculation of word count and visualization of word cloud using pyspark and a fifa dataset from twitter.

About this project:
This is a Python script that uses the PySpark and wordcloud libraries to perform word count analysis on a text file and generate a word cloud visualization.

This code reads a text file, performs word count analysis using PySpark, saves the word counts to a file, and generates a word cloud visualization using the word frequencies.
Contents in this folder are:

• Readme
• wordcount.py file
• US101 file
• Corpus / Dataset

Packages Required:
SPARK VERSION – 3.4.0
PYTHON VERSION – 3.10.6
OPEN JDK VERSION – 11.0.18
wordcloud==1.9.1.1
python-apt==2.3.0+ubuntu2.1
matplotlib==3.6.2
Pillow==9.5.0

These below modules should be imported:
• from pyspark.sql import SparkSession
• from wordcloud import WordCloud, STOPWORDS
• import matplotlib.pyplot as plt

Path provided in the 9th line of the code is the path of the input corpus in txt format.
In line 32nd the path of the output file has to be changed according to your use.
The path provided in the 44th line belongs to the US101 file which Is a TrueType font file and needs to be changed accordingly
In order to execute the code successfully run the following commands:

• pip install –upgrade pip
• pip install –upgrade pillow

Run the following command on your terminal to execute the code(provided that you are in the same directory as the code)
• spark-submit wordcount.py (wordcount.py is the name of the file)
After running the code the output will get printed onto to the terminal along with a word cloud popping up in pyplot(output will also get saved in the output file)
