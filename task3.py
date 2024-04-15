import spacy
 
def tokenize_sentences(text, language): 
    # Load the language-specific model 
    full_model_name = f"{language}_core_news_sm"
    nlp = spacy.load(full_model_name)
     
    # Create a Doc object by processing the input text 
    doc = nlp(text) 
     
    # Extract the sentences from the Doc object 
    sentences = [sent.text for sent in doc.sents] 
     
    return sentences 
 
# Prompt the user for input text 
text = input("Enter the text to tokenize: ") 
 
# Prompt the user for the language 
language = input("Enter the language (e.g., 'fr' for French, 'de' for German): ") 
 
# Tokenize the text into sentences 
sentences = tokenize_sentences(text, language) 
 
# Print the tokenized sentences 
print("Tokenized sentences:") 
for sentence in sentences: 
    print(sentence)
