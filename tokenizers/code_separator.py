import os


class CommentSeparator:
    def __init__(self, lines):
        self.single = '//'
        self.multiple_start = '/*'
        self.multiple_end = '*/'
        # all lines
        # format ["string1","string2"]
        self.test_lines = [not_empty.strip() for not_empty in lines if not_empty != '\n']
        self.test_lines = list(filter(None, self.test_lines))
        # if string return true if empty --> '' false
        self.comment = []
        self.code = []
        self.keyword = ["function", "event", "modifier", "enum"]
        # natspec comments use also /** and /// with tags @
        # doxygen comments also uses the same char of natspec

    def code_length(self, s, e, char_s, char_e, i):
        c = 0
        while s > e:
            c += 1
            s += self.test_lines[i + c].count(char_s)
            e += self.test_lines[i + c].count(char_e)
        return c

    def code_inside(self, code_portion):
        code = []
        for i in code_portion:
            if i.startswith(self.single):
                pass
            elif self.single in i:
                s = i.split(self.single)
                code.append(s[1])
            else:
                code.append(i)
        return ' '.join(code)

    def comment_inside(self, code_portion):
        comment = []
        for j in code_portion:
            if j.startswith(self.single):
                comment.append(j)
            elif self.single in j:
                s = j.split(self.single)
                comment.append(s[0])
        return ' '.join(comment)

    def run(self):
        for i in range(len(self.test_lines)):
            try:
                if any(self.test_lines[i].startswith(substring) for substring in self.keyword):
                    comment_present = False
                    tmp_code = ''
                    tmp_comment = ''
                    braces_s = self.test_lines[i].count('{')
                    braces_e = self.test_lines[i].count('}')
                    round_braces_s = self.test_lines[i].count('(')
                    round_braces_e = self.test_lines[i].count(')')

                    sub_code_length = self.code_length(braces_s, braces_e, '{', '}', i)
                    round_code_length = self.code_length(round_braces_s, round_braces_e, '(', ')', i)
                    above_line = self.test_lines[i - 1]
                    s = above_line.startswith(self.single)
                    ms = above_line.startswith(self.multiple_start)
                    me = above_line.startswith(self.multiple_end) or above_line.endswith(self.multiple_end)
                    above = (s or ms or me)
                    if round_braces_s == round_braces_e and round_code_length == 0 and sub_code_length == 0 and above:
                        tmp_comment = self.test_lines[i]
                        comment_present = True

                    # comment inside code
                    # /*not considered*/
                    tmp_comment = self.comment_inside(self.test_lines[i:i + sub_code_length + 1])
                    tmp_code = self.code_inside(self.test_lines[i:i + sub_code_length + 1])

                    # comment above code
                    count_s = 0
                    while s:
                        count_s += 1
                        s = self.test_lines[i - count_s].startswith(self.single)

                    count_m = 0
                    if me or ms:
                        while not ms:
                            count_m += 1
                            ms = self.test_lines[i - count_m].startswith(self.multiple_start)

                    if count_s > 0:
                        comment_present = True
                        count_s -= 1
                        tmp_comment1 = ' '.join(self.test_lines[i - count_s:i])
                        tmp_comment = ' '.join([tmp_comment1, tmp_comment])

                    if count_m > 0:
                        comment_present = True
                        # count_m -= 1
                        tmp_comment1 = ' '.join(self.test_lines[i - count_m:i])
                        tmp_comment = ' '.join([tmp_comment1, tmp_comment])

                    if comment_present and tmp_comment != '' and tmp_code != '':
                        self.comment.append(tmp_comment + '\n')
                        self.code.append(tmp_code + '\n')
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
    print(total)

    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith(".sol"):
                contract = os.path.join(root, filename)
                # print(contract)
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
                file_num += 1
            else:
                not_contract = os.path.join(root, filename)
                os.remove(not_contract)
            i = 0
            if len(comments) == len(codes):
                while i < len(comments):
                    raw_comment.write(comments[i])
                    raw_code.write(codes[i])
                    i += 1
            comments.clear()
            codes.clear()

            print(file_num, " / ", total)

    raw_comment.close()
    raw_code.close()


if __name__ == '__main__':
    main()
