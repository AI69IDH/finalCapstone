import spacy
nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

# Determine similarity

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))



# WORKING WITH VECTORS

tokens = nlp('cat apple monkey banana mouse elephant')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))


# The interesting thing is that the similarity between banana a monkey is twice bigger than between a cat and 
# banana but less than between cat and monkey.  It shows that similarity by types (like that both are animals ) 
# is bigger than by association animals with their best feed (like banana and  monkey ).

#The biggest different between "en_core_web_sm" and 'en_core_web_md' is that "en_core_web_sm" usually use for parsing and analyzing the words while 
# 'en_core_web_md' to find similarities between words and sentences.







# WORKING WITH SENTENCES

sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)

