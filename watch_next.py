# This programm use spacy.load('en_core_web_md'), take in the description of the movie as a parameter and return the title of the most similar movie.

import spacy

nlp = spacy.load('en_core_web_md')

with open('c:/Users/X/Dropbox/AI23020007294/Data Science (Fundamentals)/T21/movies.txt', 'r') as file:

    movies = file.readlines()


def watch_next(): # This function take in the description as a parameter and return the title of the most similar movie.

    movie_PlanetHulk = """Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and 
    launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a 
    gladiator."""

    movie_PlanetHulk_token = nlp(movie_PlanetHulk)

    dictionary = {}

    counter=0

    for token in movies:
        counter+=1
        token = nlp(token)
        simila = token.similarity (movie_PlanetHulk_token)
        dictionary.update({counter : simila}) # Create the dictionary with all similarity
        
    max_similarity = max(dictionary, key = dictionary.get, )

    return (max_similarity)



print ()

print (f"The most similar movie with Planet Hulk is: {movies [watch_next() - 1 ]}")



