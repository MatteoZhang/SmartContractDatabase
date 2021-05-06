stringa = '''// comm
            /// comment
            function () {
                // comment 1
                code code //comm 3
                /*comment
                 koko
                 2*/
            }
            
            /*
            comment 4
            */
            
            function(){
                code2 // comment 3
            }
            
            // evento ciao
            event()
            
            
            function(
            ciao ciao
            //commento ciao
            )
            
            '''


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
                if any(substring in self.test_lines[i] for substring in self.keyword):
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

                    if comment_present:
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


lines = stringa.split("\n")
separator = CommentSeparator(lines)
separator.run()
comments = separator.write_comments()
codes = separator.write_codes()
print(comments)
print(codes)

