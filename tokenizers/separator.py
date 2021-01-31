import os
import json
import time


class CommentSeparator:
    def __init__(self, test_lines):
        self.single = '//'
        self.multiple_start = '/*'
        self.multiple_end = '*/'
        self.asterisk = '*'
        self.test_lines = test_lines
        self.comment = []
        self.code = []
        # natspec comments use also /** and /// with tags @
        # doxygen comments also uses the same char of natspec

    def run(self):
        for line in self.test_lines:
            print(line)

    # we need matching codes and comments
    def write_comments(self):
        return self.comment

    def write_codes(self):
        return self.code


def main():
    # TODO  take file separate comment from code
    # comment and code must be list of string
    # all comment inside a function is taken to the outside
    # the main keyword is function

    directory = "smart_contracts"
    raw_code = open(directory + "_code\\" + 'code.original', 'a+', encoding="utf8")
    open(directory + "_code\\" + 'code.original', 'w', encoding="utf8").close()
    raw_comment = open(directory + "_comment\\" + 'javadoc.original', 'a+', encoding="utf8")
    open(directory + "_comment\\" + 'javadoc.original', 'w', encoding="utf8").close()
    comments = []
    codes = []

    for filename in os.listdir(directory):
        if filename.endswith(".sol"):
            contract = os.path.join(directory, filename)
            # example: 'smart_contracts\0x00ca5b4fcb1680c57da0a5a6c94a405822f960ab.sol'
            with open(contract, 'r', encoding="utf8") as raw:
                lines = raw.readlines()  # array of lines
                valid = lines[0]
                if valid.startswith('{'):
                    # filter the source codes
                    pass
                else:
                    separator = CommentSeparator(lines)
                    separator.run()
                    comments = separator.write_comments()
                    codes = separator.write_codes()

        i = 0
        while i < max([len(comments), len(codes)]):
            raw_comment.write(comments[i])
            raw_code.write(codes[i])
            i += 1

        comments.clear()
        codes.clear()

    raw_comment.close()
    raw_code.close()


if __name__ == '__main__':
    main()
