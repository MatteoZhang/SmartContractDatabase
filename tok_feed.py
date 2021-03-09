from tokenizers.simple_tokenizer import SimpleTokenizer
from tokenizers.code_tokenizer import CodeTokenizer


def double_tokenize(line):
    m = '-'
    a = '*'
    s = '/'
    simple = SimpleTokenizer()
    simple_token = simple.tokenize(line)
    clean = [x for x in simple_token.words() if (x != m and x != a and x != s)]
    cc = CodeTokenizer()
    c_token = cc.tokenize(' '.join(clean))
    final = ' '.join(c_token.words())
    return final + '\n'


def main():
    code = "tokenizers\\smart_contracts_code\\code.original"
    comment = "tokenizers\\smart_contracts_comment\\javadoc.original"

    code_token = []
    comment_token = []
    with open(code, 'r', encoding="utf8") as read_code:
        code_line = read_code.readlines()
        for i in range(len(code_line)):
            code_token.append(double_tokenize(code_line[i]))
    with open(comment, 'r', encoding="utf8") as read_comment:
        comment_line = read_comment.readlines()
        for i in range(len(comment_line)):
            comment_token.append(double_tokenize(comment_line[i]))
    tok_code = open("tokenizers\\tok_code\\" + 'code.original', 'a+', encoding="utf8")
    tok_comm = open("tokenizers\\tok_comm\\" + 'javadoc.original', 'a+', encoding="utf8")

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
