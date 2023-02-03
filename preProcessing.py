import string


#To open the file and print the data as it is 
text = open('text.txt',encoding='utf-8').read()
#print(text)


#pre-processing level-1 converting to lower case as Apple != apple
lower_case = text.lower()
#print(lower_case)


#pre-processing level-2 removing unwanted symbols or punctuations
cleaned_text = lower_case.translate(str.maketrans('','',string.punctuation))
#print(cleaned_text)


#Tokenization of string
tokenized_words = cleaned_text.split()
#print(tokenized_words)


#Pre-processing level-3 Removing unwanted words or Stop Words
stop_words=["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]


final_words=[]

for word in tokenized_words:
    if word not in stop_words:
        final_words.append(word)
        
print(final_words)