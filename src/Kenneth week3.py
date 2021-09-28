import spacy
from typing import List
nlp = spacy.load("en_core_web_sm")
doc = nlp("This is an English text")
print(type(doc))
# <class 'spacy.tokens.doc.Doc'>

token = doc[1]
print(token)
# is

print(type(token))
# <class 'spacy.tokens.token.Token'>

dir(token)

print(token.is_digit)
# False

def corpus_loader(folder: str) -> List[str]:
    """
    A corpus loader function which takes in a path to a 
    folder and returns a list of strings.
    """


