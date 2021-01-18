import os
import json

if __name__ == '__main__':

    comment_line = "//"
    comment_start = "/*"
    comment_end = "*/"
    directory = "smart_contracts"
    asterisk = '*'

    # iterate over all contracts
    for filename in os.listdir(directory):
        if filename.endswith(".sol"):
            contract = os.path.join(directory, filename)
            # example: 'smart_contracts\0x00ca5b4fcb1680c57da0a5a6c94a405822f960ab.sol'
            # print(filename)
            with open(contract, 'r', encoding="utf8") as raw:
                lines = raw.readlines()  # array of lines
                valid = lines[0]
                if valid.startswith('{'):
                    pass
                else:
                    raw_code = open(directory + "_code\\" + filename, 'a+', encoding="utf8")
                    open(directory + "_code\\" + filename, 'w', encoding="utf8").close()
                    raw_comment = open(directory + "_comment\\" + filename, 'a+', encoding="utf8")
                    open(directory + "_comment\\" + filename, 'w', encoding="utf8").close()

                    multi_comment = 0
                    single_comment = 0

                    for line in lines:
                        line = line.lower().strip()  # lower case, strip all withespace before
                        if comment_line in line and not (line.startswith(comment_line) or line.startswith(asterisk)):
                            divided = line.split(comment_line)
                            # ['uint256 public constant minimum_delay = 48 hours;', ' have to be present for 2 rebases']
                            s = ''
                            raw_code.write(s.join(divided[:-1]))
                            raw_comment.write(divided[-1] + "\n")
                        if line.startswith(comment_start):
                            multi_comment = 1
                        if line.startswith(comment_line):
                            single_comment = 1
                        if (multi_comment or single_comment) and line != '' and line != '*' and line != comment_line:
                            white = line.strip('*//')
                            raw_comment.write(white.strip()+"\n")
                        elif line != '' and line != '*' and line != comment_line:
                            raw_code.write(line+"\n")
                        if line.startswith(comment_end) or line.endswith(comment_end):
                            multi_comment = 0
                        single_comment = 0
                    raw_comment.close()
                    raw_code.close()
