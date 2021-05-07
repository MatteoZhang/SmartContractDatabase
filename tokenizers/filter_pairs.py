import random

SOURCECODE = 'smart_contracts_code/code_tok.original'
COMMENT = 'smart_contracts_comment/doc_tok.original'
OUT_SOURCE = 'smart_contracts_code/code_sampled.original'
OUT_COMM = 'smart_contracts_comment/doc_sampled.original'
LINES = 6000


def main():
    with open(SOURCECODE, 'r', encoding="utf8") as source:
        with open(COMMENT, 'r', encoding="utf8") as comment:
            code_lines = source.readlines()
            comm_lines = comment.readlines()
            random_list = random.sample(range(0, len(code_lines)), LINES)
            code_sample = []
            comm_sample = []
            for i in random_list:
                code_sample.append(code_lines[i])
                comm_sample.append(comm_lines[i])
    with open(OUT_SOURCE, 'w', encoding="utf8") as out_s:
        with open(OUT_COMM, 'w', encoding="utf8") as out_c:
            out_s.writelines(code_sample)
            out_c.writelines(comm_sample)


if __name__ == '__main__':
    main()
