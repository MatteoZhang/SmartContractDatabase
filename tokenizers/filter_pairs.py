import random

SOURCECODE = 'CodeComm/code_tok.original'
COMMENT = 'CodeComm/doc_tok.original'
OUT_SOURCE = 'CodeComm/code_sampled.original'
OUT_COMM = 'CodeComm/doc_sampled.original'
LINES = 500000
MaxLen = 5000
MinLen = 10


def main():
    with open(SOURCECODE, 'r', encoding="utf8") as source:
        with open(COMMENT, 'r', encoding="utf8") as comment:
            code_lines = source.readlines()
            comm_lines = comment.readlines()
            random_list = random.sample(range(0, len(code_lines)), LINES)
            code_sample = []
            comm_sample = []
            # ==========
            for i in random_list:
                # code_lines[i] not in code_sample for unique codes
                # comm_lines[i] not in comm_sample for unique comm
                # code_lines[i] not in code_sample and comm_lines[i] not in comm_sample unique pair
                # xor same code different comm same comm different code
                x = comm_lines[i] in comm_sample
                # y = code_lines[i] in code_sample
                if not x and comm_lines[i] != '':
                    # if MinLen < len(comm_lines[i]) < MaxLen and MinLen < len(code_lines[i]) < MaxLen:
                    code_sample.append(code_lines[i])
                    comm_sample.append(comm_lines[i])
            # ======
    with open(OUT_SOURCE, 'w', encoding="utf8") as out_s:
        with open(OUT_COMM, 'w', encoding="utf8") as out_c:
            out_s.writelines(code_sample)
            out_c.writelines(comm_sample)


if __name__ == '__main__':
    main()
