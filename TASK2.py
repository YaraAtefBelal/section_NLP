import csv
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

# Read the CSV file
with open('SPAM text message 20170820 - Data.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    messages = [row[1] for row in reader]

# Tokenization and stemming
stemmer = PorterStemmer()
tokenized_messages = []
for message in messages:
    tokens = word_tokenize(message)  # Tokenize the message
    stemmed_tokens = [stemmer.stem(token) for token in tokens]  # Apply stemming
    tokenized_messages.append(stemmed_tokens)

# Print the tokenized messages
for tokens in tokenized_messages:
    print(tokens)