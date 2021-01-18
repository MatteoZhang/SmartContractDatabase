from tokenizers.simple_tokenizer import SimpleTokenizer
from tokenizers.code_tokenizer import CodeTokenizer

if __name__ == '__main__':
    line_to_tok = "@dev CammelCase snake_snaky for {my friend;} \t @param"
    a_tokens = SimpleTokenizer()
    token = a_tokens.tokenize(line_to_tok)
    print(token.words())
    c_tokens = CodeTokenizer()
    ctoken = c_tokens.tokenize(' '.join(token.words()))
    print(ctoken.words())
    final = ' '.join(ctoken.words())
    print(final)
