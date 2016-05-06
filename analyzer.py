# -*- coding: utf-8 -*-

from time import strftime
import operator

class Analyzer(object):
    """Analyze a given text"""

    def __init__(self, text):
        self.creation_date = strftime("%m-%d-%Y %H:%M:%S")
        self.text = text
        self.word_count = 0
        self.longest_word = ""
        self.words_occur = {}
        self.letters_count = 0
        self.letters_occur = {}
        self.most_used_words = {}

    def get_analyse(self):
        print "self : {}".format(self)
        print "text : {}".format(self.text)
        for value in (self.text):
            self.word_count+=1
            current_length = len(value)
            if current_length > len(self.longest_word):
                self.longest_word = value
            if self.words_occur.has_key(value):
                self.words_occur[value] = self.words_occur.get(value) + 1
            else:
                self.words_occur[value] = 1
            for char in value:
                self.letters_count+=1
                if self.letters_occur.has_key(char):
                    self.letters_occur[char] = self.letters_occur.get(char) + 1
                else:
                    self.letters_occur[char] = 1
        print "the most longest words is : {}".format(self.longest_word)
        print "the number of words is : {}".format(self.word_count)
        print "the number of letters is : {}".format(self.letters_count)
        self.words_occur = sorted(self.words_occur.items(), key=operator.itemgetter(1))
        self.words_occur.reverse()
        i = 0
        for word, value in (self.words_occur):
            self.most_used_words[word] = value;
            print "the word '{}' appears {} times".format(word, value)
            i+=1
            if(i==5):
                break
        self.letters_occur = sorted(self.letters_occur.items(), key=operator.itemgetter(1))
        self.letters_occur.reverse()
        i = 0
        for letter, value in (self.letters_occur):
            print "the letter '{}' appears {} times".format(letter, value)
            i+=1
            if(i==5):
                break
        return self
