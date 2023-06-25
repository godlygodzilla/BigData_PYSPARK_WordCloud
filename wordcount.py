from pyspark.sql import SparkSession
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

# Create a SparkSession
spark = SparkSession.builder.appName('Firstprogram').getOrCreate()

# Read the input file and calculate word counts
text_file = spark.read.text("Problem statement-word count and word cloud.txt")

# FlatMap: Split lines into words
words = text_file.rdd.flatMap(lambda line: line[0].split(" "))

# Map: Assign count of 1 to each word
word_counts = words.map(lambda word: (word, 1))

# ReduceByKey: Sum the counts of each word
word_counts = word_counts.reduceByKey(lambda x, y: x + y)

# Collect word counts
output = word_counts.collect()


# Print each word with its respective count
for (word, count) in output:
    print("%s: %i" % (word, count))

#print output to a text file    
output_file = "word_count_output.txt"
with open(output_file, "w") as file:
    for (word, count) in output:
        file.write("%s: %i\n" % (word, count))

# Create a word frequency dictionary
wordcloud_data = {word: float(count) for (word, count) in output}

# Generate the word cloud
text = ' '.join([word for word, _ in output]).lower()

# Set the font path to a TrueType font file on your system
font_path = "/home/vineeth/Desktop/US101.ttf"

# Create the WordCloud object with the specified font path
wordcloud = WordCloud(
    stopwords=STOPWORDS,
    collocations=True,
    font_path=font_path,
    background_color='white'
).generate(text)

# Plot the word cloud
plt.figure(figsize=(12, 8))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

# Stop SparkSession
spark.stop()
