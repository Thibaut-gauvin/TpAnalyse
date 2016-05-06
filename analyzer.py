# -*- coding: utf-8 -*-

from time import strftime


class Analyzer(object):
    """Analyze a given text"""

    def __init__(self, text):
        self.creation_date = strftime("%m-%d-%Y %H:%M:%S")
        self.text = text
        self.words_count = 0
        self.words_occur = {}
        self.letters_nb = 0
        self.letters_nb_occur = {}
        self.most_used_words = {}

    def parse_text(self):
        """Parse text"""

        clean_text = self.text.split(" ")

        self.words_count = len(clean_text)

        for word in clean_text:
            self.letters_nb += len(word)

            if self.words_occur.has_key(word):
                self.words_occur[word] = self.words_occur.get(word) + 1
            else:
                self.words_occur[word] = 1

        return self
