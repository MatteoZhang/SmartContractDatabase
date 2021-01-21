import os
import json
import time


class CommentSeparator:
    def __init__(self, test_line):
        self.single = '//'
        self.multiple_start = '/*'
        self.multiple_end = '*/'
        self.text_line = test_line
        self.comment = []
        self.code = []
        # natspec comments use also /** and /// with tags @
        # doxygen comments also uses the same char of natspec

    def comment_check (self, multiple_flag):
        if multiple_flag:
            return True
        elif self.test_line.startswith():

def remove_whitespace(string):




if __name__ == '__main__':
    pass