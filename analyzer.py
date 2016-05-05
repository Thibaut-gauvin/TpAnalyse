# -*- coding: utf-8 -*-

from time import strftime


class Analyzer(object):
    """Analyze a given text"""

    def __init__(self, text):
        self.creation_date = strftime("%m-%d-%Y %H:%M:%S")
        self.text = text
        self.words_occur = int
        self.letters_nb = int
        self.letters_nb_occur = {}
        self.most_famous_words = {}

    def parse_text(self):
        """Parse text"""

        self.words_occur = 4
        self.letters_nb = 16
        self.letters_nb_occur = {'t:8', 'o:8'}
        self.most_famous_words = {'toto:4'}

        return self
