import nltk
import re

# tokenise them using nltk module and make them as a dictionary

#### list of all directories #####

stopwords_docs=['./StopWords/StopWords_Auditor','./StopWords/StopWords_Currencies','./StopWords/StopWords_DatesandNumbers','./StopWords/StopWords_Generic','./StopWords/StopWords_GenericLong','./StopWords/StopWords_Geographic','./StopWords/StopWords_Names']
master_docs=['./MasterDictionary/negative-words','./MasterDictionary/positive-words']
input_docs=[]
for i in range(37,151):
    input_docs.append(str(i))


def tokenize(docs):
    tokens=[]
    for doc in docs:
        # print(doc)
        try:
            with open(doc+'.txt', 'r') as f:
                # Read the contents of the file
                text = f.read()
            # Tokenize the text
            tokens += nltk.word_tokenize(text)
        except:
            print(doc+'.txt file not found')
    final_tokens=[token for token in tokens if token not in [')','(','|',',','.','!','?']]
    return final_tokens

def tokenize_input(docs):
    final_tokens={}
    for doc in docs:
        # print(doc)
        try:
            with open('./extracted_data/'+doc+'.txt', 'r') as f:
                text = f.read()

            # Tokenize the text
            tokens = nltk.word_tokenize(text)
            final_tokens[doc]=[token for token in tokens if token not in [')','(','|',',','.','!','?']]
        except:
            print(doc+'.txt file not found')
    return final_tokens

# data extraction from stop words folder into dictionary form
final_stopwords=tokenize(stopwords_docs)
dict_tokens=dict(zip(final_stopwords,[True for i in range(len(final_stopwords))]))

# creating positive and negative dictionary from master excluding the words from stop words dictionary
# positive words
final_pos=[]
for token in tokenize([master_docs[0]]):
    try:
        if dict_tokens[token]:
            pass
    except:
        final_pos.append(token)  


Positives=dict(zip(final_pos,[1 for i in range(len(final_pos))]))


# negative words
final_neg=[]
for token in tokenize([master_docs[1]]):
    try:
        if dict_tokens[token]:
            pass
    except:
        final_neg.append(token)  

Negatives=dict(zip(final_neg,[1 for j in range(len(final_neg))]))

Input=tokenize_input(input_docs)


# for finding number of complex words,pronouns and number of sentences in a docs
complex_words={}
sentences={}
pronouns=['we','I','my','me','ours','us','he','him','she','her','they','them','you']
pronouns_counts={}
pattern = r'''/([aeiouyAEIOUY]+[^e.\s])|([aiouyAEIOUY]+\b)|(\b[^aeiouy0-9.']+e\b)/'''
for doc in input_docs:
    pronouns_count=0
    try:
        with open('./extracted_data/'+doc+'.txt', 'r') as f:
            # Read the contents of the file
            text = f.read()
        for pronoun in pronouns:
            pronouns_count+=len(re.findall(pronoun,text))
        pronouns_counts[doc]=pronouns_count
        sentences[doc]=len(re.findall('.',text))
        complex_words[doc]=len(re.findall(pattern, text))
    except:
        pass
        # print(doc+'.txt file not found')
    
    
    