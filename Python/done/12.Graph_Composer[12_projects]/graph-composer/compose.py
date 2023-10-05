import os
import re
import string
import random
from graph import Graph, Vertex

def get_words_from_text(text_path):
    with open(text_path, 'r') as file:
        text = file.read() #.decode("utf-8")

        # remove [verse 1: artist]
        # include the following line if you are doing song lyrics
        text = re.sub(r'\[(.+)\]', ' ', text)

        text = ' '.join(text.split())
        text = text.lower()
        text = text.translate(str.maketrans('', '', string.punctuation))

    words = text.split()

    # words = words[:1000]

    return words


def make_graph(words):
    g = Graph()
    prev_word = None
    # for each word
    for word in words:
        # check that word is in graph, and if not then add it
        word_vertex = g.get_vertex(word)

        # if there was a previous word, then add an edge if does not exist
        # if exists, increment weight by 1
        if prev_word:  # prev word should be a Vertex
            # check if edge exists from previous word to current word
            prev_word.increment_edge(word_vertex)

        prev_word = word_vertex

    g.generate_probability_mappings()

    return g

def compose(g, words, length=50):
    composition = []
    word = g.get_vertex(random.choice(words))
    for _ in range(length):
        composition.append(word.value)
        word = g.get_next_word(word)

    return composition


def main(artist):
    # for text
    # words = get_words_from_text('texts\hp_sorcerer_stone.txt')
    # for song
    words = []
    for song in os.listdir(f'12.Graph_Composer[12_projects]\songs\{artist}'):
        if song == '.DS_Store':
            continue
        words.extend(get_words_from_text(f'songs\{artist}\{song}'))

    g = make_graph(words)
    composition = compose(g, words, 100)
    return ' '.join(composition)


if __name__ == '__main__':
    print(main('taylor_swift'))
