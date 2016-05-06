# -*- coding: utf-8 -*-

import uuid
import numpy as np
import matplotlib.pyplot as plt


class Graphic(object):
    """Render analyze graphics"""

    def __init__(self, letters_occur, words_occur, letters_count):
        self.letters_occur = letters_occur
        self.words_occur = words_occur
        self.letters_count = letters_count
        self.letter_occur_graph_name = ""
        self.words_occur_graph_name = ""

    def graph_letter_occurrence(self):
        """Render graphic of letter occurrence"""

        letters = []
        occurrence = []
        for key, value in self.letters_occur:
            letters.append(key)
            occurrence.append(value)

        y_pos = np.arange(len(letters))

        plt.barh(y_pos, occurrence, color='red', align='center', alpha=0.5)
        plt.yticks(y_pos, letters)
        plt.title('Letters Occurrences')

        self.letter_occur_graph_name = str(uuid.uuid4()) + '.jpg'
        plt.savefig('./img/letter/' + self.letter_occur_graph_name)
        plt.close()

    def graph_words_occurrence(self):
        """Render graphic of words occurrence"""

        words = []
        occurrence = []
        for key, value in self.words_occur:
            words.append(key)
            occurrence.append(value)

        y_pos = np.arange(len(words))

        plt.barh(y_pos, occurrence, color='blue', align='center', alpha=0.5)
        plt.yticks(y_pos, words)
        plt.title('Top 5 Words Occurrences')

        self.words_occur_graph_name = str(uuid.uuid4()) + '.jpg'
        plt.savefig('./img/words/' + self.words_occur_graph_name)
        plt.close()
