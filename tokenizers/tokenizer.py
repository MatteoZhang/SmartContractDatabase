from tokenizers.tok_class.code_tokenizer import CodeTokenizer
from tokenizers.tok_class.simple_tokenizer import SimpleTokenizer


def double_tokenize(line):
    m = '-'
    a = '*'
    s = '/'
    p = '`'
    e = '='
    simple = SimpleTokenizer()
    simple_token = simple.tokenize(line)
    clean = [x for x in simple_token.words() if (x != m and x != a and x != s and x != p and x != e)]
    cc = CodeTokenizer()
    c_token = cc.tokenize(' '.join(clean))
    final = ' '.join(c_token.words())
    return final + '\n'


def main():
    code = "smart_contracts_code\\code.original"
    comment = "smart_contracts_comment\\doc.original"

    code_token = []
    comment_token = []
    with open(code, 'r', encoding="utf8") as read_code:
        with open(comment, 'r', encoding="utf8") as read_comment:
            code_line = read_code.readlines()
            comment_line = read_comment.readlines()
            for i in range(len(comment_line)):
                try:
                    if comment_line[i].isascii():
                        code_token.append(double_tokenize(code_line[i]))
                        comment_token.append(double_tokenize(comment_line[i]))
                    else:
                        print(comment_line[i])
                except Exception as e:
                    print(e)

    tok_code = open("smart_contracts_code\\" + 'code_tok.original', 'a+', encoding="utf8")
    tok_comm = open("smart_contracts_comment\\" + 'doc_tok.original', 'a+', encoding="utf8")

    i = 0

    while i < min(len(code_token), len(comment_token)):
        tok_comm.write(comment_token[i])
        tok_code.write(code_token[i])
        i += 1
    comment_token.clear()
    code_token.clear()

    tok_code.close()
    tok_comm.close()


if __name__ == '__main__':
    main()
