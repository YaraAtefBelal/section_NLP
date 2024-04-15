import nltk
from nltk.tokenize import word_tokenize

def pos_tagging(text):
    # Tokenize the input text into words
    words = word_tokenize(text)
    
    # Perform POS tagging using the Penn Treebank tagset
    tagged_penn = nltk.pos_tag(words)
    
    # Perform POS tagging using the Universal tagset
    tagged_universal = nltk.pos_tag(words, tagset='universal')
    
    return tagged_penn, tagged_universal

# Prompt the user for input text
text = input("Enter the text for POS tagging: ")

# Apply POS tagging using two different tagsets
tagged_penn, tagged_universal = pos_tagging(text)

# Print the tagged words using the Penn Treebank tagset
print("Tagged words (Penn Treebank tagset):")
for word, tag in tagged_penn:
    print(word, ":", tag)

# Print the tagged words using the Universal tagset
print("\nTagged words (Universal tagset):")
for word, tag in tagged_universal:
    print(word, ":", tag)