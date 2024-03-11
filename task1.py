import nltk
#nltk.download('punkt')
#from nltk import word_tokenize
#from nltk import sent_tokenize
def tokenize_words(text):
    tokens = nltk.word_tokenize(text)
    return tokens

def tokenize_sentences(text):
    sentences = nltk.sent_tokenize(text)
    return sentences

def print_output(text, choice):
    if choice == 1:
        output = tokenize_words(text)
    elif choice == 2:
        output = tokenize_sentences(text)
    elif choice == 3:
        output = text.split()
    else:
        output = []
    
    print("Output:", output)

# Example usage
input_text = "NLTK is a leading platform for building Python programs to work with human language data. NLTK is available for Windows, Mac OS X, and Linux. Best of all, NLTK is a free, open source, community-driven project."
choice = int(input("Enter your choice (1, 2, or 3): "))
print_output(input_text, choice)
