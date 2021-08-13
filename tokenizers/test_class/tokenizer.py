from tokenizers.tok_class.code_tokenizer import CodeTokenizer
from tokenizers.tok_class.simple_tokenizer import SimpleTokenizer
import os

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
    directory = "smart_contracts"
    code_token = []
    for root, dirs, files in os.walk(directory):
        for filename in files:
            contract = os.path.join(root, filename)
            with open(contract, 'r', encoding="utf8") as read_code:
                code_line = read_code.readlines()
                for i in range(len(code_line)):
                    try:
                        code_token.append(double_tokenize(code_line[i]))
                    except Exception as e:
                        print(e)
            name = contract.split(".")
            tok_code = open(name[0]+".tok", 'a+', encoding="utf8")

            i = 0

            while i < len(code_token):
                tok_code.write(code_token[i])
                i += 1
            code_token.clear()

            tok_code.close()


if __name__ == '__main__':
    main()
