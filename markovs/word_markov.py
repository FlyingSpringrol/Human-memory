"""
Keywords: open, with as,

"""
import string
import numpy as np
import random

class Markov(object): #add gutenberg project specific reading methods
    def __init__(self, path):
        self.path = path #path = path to file
        self.markov = dict()
        self.create_markov()
    def create_markov(self): #parse out spaces, treat punctuation as words?
        f = open(self.path, 'r')
        block = []
        for line in f.readlines(): #returns each lines
            line = self.remove_punc(line) #processes
            words = line.split(' ') #get individual words
            for word in words:
                if word == ' ':
                    words.remove(word)
            for word in words:
                block.append(word.strip())

        prefix_size = 2
        self.read_block(prefix_size,block) #first arg = size of prefix-blocks

    def read_block(self, prefix_size, block):
        #block is entire array of words
        for idx in range(len(block)-2): #sorts array?
            prefix = block[idx]
            for i in range(1,prefix_size): #create prefix
                prefix += ' ' + block[idx + i]
            if self.markov.get(prefix):
                #appends the suffix
                self.markov.get(prefix).append(block[idx+prefix_size])
            else:
                #initializes the suffix array
                self.markov[prefix] = [block[idx+prefix_size]]

    def remove_punc(self,line):
        line = line.lower().strip()
        for punc in string.punctuation:
            line = line.replace(punc, '')
        return line

    def print_dictionary(self):
        print self.markov

    def get_random_output(self, prefix_array):
        #prefix array is two word array
        prefix = ''
        for word in prefix_array:
            prefix += word + ' '
        prefix = prefix[:-1]
        possibles = self.markov.get(prefix)
        if not possibles:
            return ''
        selected = int(len(possibles) * random.random()) #random index
        return possibles[selected]

    def get_random_words(self, amount): #returns a prefix
        dict_len = len(self.markov)
        result = []
        key = random.sample(self.markov,1)
        print key
        return key[0].split(' ') #return word array

    def generate_paragraph(self, length):
        #hashing?
        random_words = self.get_random_words(2)#select randomly from dictionary
        array_len = len(random_words)
        for i in range(length):
            value = self.get_random_output(random_words[array_len-2: array_len])
            random_words.append(value)
            array_len = len(random_words)#recalculate array length
        return random_words

def main(path):
    markov1 = Markov(path)
    #markov1.print_dictionary()
    print markov1.generate_paragraph(100)

main('henry.txt')
