import os


def merge_dict(d1, d2, file_path):
    for c in range(len(d2)):
        d1[str(len(d1))] = d2[str(c)]

    with open(file_path, "w") as file:
        for c in d1:
            file.write(d1[c][0] + "\n")


def combine_lines(c_line, m_line, dir_c, dir_m):
    for cnt in range(len(c_line)):
        if m_line[cnt].startswith("event") or m_line[cnt].startswith("function"):
            world_list = c_line[cnt].split()
            if len(world_list) < 2:
                code_list = m_line[cnt].split()
                flag = 0
                sub_list = []
                for element in code_list:
                    flag += 1
                    if "(" in element:
                        sub_list = code_list[0:flag]
                        break
                c_line[cnt] = " ".join(sub_list[1:-1]) + " " + sub_list[0] + "\n"

    with open(dir_c, "w") as f:
        f.writelines(c_line)

    dir_merged = dir_c.split(".")
    with open(".".join([dir_merged[0], "solextracted"]), "r") as read:
        me_line = read.readlines()
    with open(".".join([dir_merged[0], "merged"]), "w") as merging:
        for cnt in range(len(c_line)):
            merging.write("COMMENT: " + c_line[cnt])
            merging.write("CODE: " + me_line[cnt])


if __name__ == '__main__':
    directory = "smart_contracts"
    comment = []
    methods = []
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith("comment"):
                comment.append(os.path.join(root, filename))
            if filename.endswith("tok"):
                methods.append(os.path.join(root, filename))
    # combine code and comments with elaborated comments
    for i in range(len(comment)):
        with open(comment[i], 'r', encoding="utf8") as c_raw:
            c_lines = c_raw.readlines()  # array of comment lines
        with open(methods[i], 'r', encoding="utf8") as m_raw:
            m_lines = m_raw.readlines()  # array of methods lines
        combine_lines(c_lines, m_lines, comment[i], methods[i])
