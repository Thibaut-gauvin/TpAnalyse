# -*- coding: utf-8 -*-

from time import strftime
import operator
import re
import json

class Analyzer(object):
    """Analyze a given text"""

    def __init__(self, text):
        self.text = text
        self.creation_date = strftime("%m-%d-%Y %H:%M:%S")
        self.words_occur = {}
        self.letters_count = 0
        self.letters_occur = {}
        self.most_used_words = {}

    def parse_text(self):
        """Parse text"""

        # format string
        escaped_text = re.sub('[^A-Za-z0-9]+', ' ', self.text)
        clean_text = escaped_text.lower().split(" ")

        print(clean_text)

        for word in clean_text:
            print(word)
            self.letters_count += len(word)

            if self.words_occur.has_key(word):
                self.words_occur[word] = self.words_occur.get(word) + 1
            else:
                self.words_occur[word] = 1

            for char in word:
                if self.letters_occur.has_key(char):
                    self.letters_occur[char] = self.letters_occur.get(char) + 1
                else:
                    self.letters_occur[char] = 1

        self.words_occur = sorted(self.words_occur.items(), key=operator.itemgetter(1))
        self.words_occur.reverse()

        self.letters_occur = sorted(self.letters_occur.items(), key=operator.itemgetter(1))
        self.letters_occur.reverse()

        self.most_used_words = self.words_occur[0:5]

        return self

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def format_before_save(self):
        """Format Analyzer object before register in database"""

        self.words_occur = ''.join(str(e) for e in self.words_occur)
        self.letters_occur = ''.join(str(e) for e in self.letters_occur)
        self.most_used_words = ''.join(str(e) for e in self.most_used_words)

        return self
