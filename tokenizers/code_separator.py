import os


class CommentSeparator:
    def __init__(self, lines):
        self.single = '//'
        self.multiple_start = '/*'
        self.multiple_end = '*/\n'
        self.asterisk = '*'
        # all lines
        # format ["string1","string2"]
        self.test_lines = [not_empty.strip() for not_empty in lines if not_empty != '\n']
        # if string return false if empty --> ''
        self.comment = []
        self.code = []
        self.keyword = ["function", "event", "modifier", "enum"]
        # natspec comments use also /** and /// with tags @
        # doxygen comments also uses the same char of natspec

    def run(self):
        for i in range(len(self.test_lines)):
            ''' 
            if the code start with function then separate code and comment
            example 
            /// comment
            function () {
                // comment 
                code code 
                /*comment*/
            }
            /*comment*/
            funciotn (){
                code // comment
            }
            '''
            braces_s = 0
            braces_e = 0
            key = self.test_lines[i].split()
            try:
                if key[0] in self.keyword:
                    # set counters
                    count_s = 0
                    count_m = 0
                    count_code = 0
                    count_flag = False
                    braces_s = self.test_lines[i].count('{')
                    braces_e = self.test_lines[i].count('}')

                    # set tmp
                    tmp_comment = ''
                    tmp_code = ''

                    current_line = self.test_lines[i - 1]
                    s = current_line.startswith(self.single)
                    ms = current_line.startswith(self.multiple_start)
                    me = current_line.startswith(self.multiple_end) or current_line.endswith(self.multiple_end)

                    while braces_s != braces_e and (s or ms or me):
                        count_code += 1
                        if i + count_code < len(self.test_lines):
                            try:
                                braces_s += self.test_lines[i + count_code].count('{')
                                braces_e += self.test_lines[i + count_code].count('}')
                            except Exception as e:
                                print(e)

                    if count_code > 0:
                        for j in range(count_code):
                            line = self.test_lines[i + j]
                            s2 = line.startswith(self.single)
                            split = line.split(self.single)
                            if s2:
                                tmp_comment = ' '.join([tmp_comment, line])
                            else:
                                tmp_code = ' '.join([tmp_code, line])
                            if len(split) == 2:
                                tmp_code = ' '.join([tmp_code, split[0]])
                                tmp_comment = ' '.join([tmp_comment, split[1]])
                        self.code.append(tmp_code + '\n')

                    while s:
                        count_s += 1
                        s = self.test_lines[i - count_s].startswith(self.single)
                    if me or ms:
                        while ms != 0:
                            count_m += 1
                            ms = self.test_lines[i - count_m].startswith(self.multiple_start)

                    if count_s > 0:
                        count_flag = True
                        count_s -= 1
                        tmp_comment = ' '.join(self.test_lines[i - count_s:i])

                    if count_m > 0:
                        count_flag = True
                        count_m -= 1
                        tmp_comment = ' '.join(self.test_lines[i - count_m:i])

                    if count_flag:  # inside out
                        self.comment.append(tmp_comment + '\n')

                    try:
                        del tmp_comment
                        del tmp_code
                    except Exception as e:
                        print(e)
            except Exception as e:
                print(e)
        self.test_lines.clear()

    # we need matching codes and comments
    def write_comments(self):
        return self.comment

    def write_codes(self):
        return self.code


def main():
    raw_code_dir = "../contracts_info/reader_getter_data"
    directory = "smart_contracts"
    raw_code = open(directory + "_code\\" + 'code.original', 'a+', encoding="utf8")
    open(directory + "_code\\" + 'code.original', 'w', encoding="utf8").close()
    raw_comment = open(directory + "_comment\\" + 'doc.original', 'a+', encoding="utf8")
    open(directory + "_comment\\" + 'doc.original', 'w', encoding="utf8").close()
    comments = []
    codes = []
    file_num = 0
    total = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".sol"):
                total += 1
    # print(total)

    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith(".sol"):
                contract = os.path.join(root, filename)
                # example: 'root\0x00ca5b4fcb1680c57da0a5a6c94a405822f960ab.sol'
                with open(contract, 'r', encoding="utf8") as raw:
                    lines = raw.readlines()  # array of lines
                    valid = lines[0]
                    if valid.startswith('{'):
                        # filter the source codes if json format
                        pass
                    else:
                        separator = CommentSeparator(lines)
                        separator.run()
                        comments = separator.write_comments()
                        codes = separator.write_codes()
                    lines.clear()

            i = 0
            if len(comments) == len(codes):
                while i < len(comments):
                    raw_comment.write(comments[i])
                    raw_code.write(codes[i])
                    i += 1
            comments.clear()
            codes.clear()
        file_num += 1
        print(file_num, " / ", total)

    raw_comment.close()
    raw_code.close()


if __name__ == '__main__':
    main()
