import nltk
import random
import os
from openpyxl import Workbook
from openpyxl.styles import Alignment

def merge_dict(d1, d2, file_path):
    for c in range(len(d2)):
        d1[str(len(d1))] = d2[str(c)]

    with open(file_path, "w") as file:
        for c in d1:
            file.write(d1[c][0] + "\n")


Short_Description = "This method <verb object> and"
Return_Description = "Return <statement>"
Modifier_Description = "This method can only be called if <condition>"
Input_Description = "The inputs are <params>"
Core_Statement_Description = "<generated main action using comments>"
Call_Description = "This method is called by <function name>"

# input text
sentence = "@ dev returns the addition of two unsigned integers , reverting on overflow . counterpart to solidity ' s + operator . requirements : addition cannot overflow ."
code = "function add ( uint256 a , uint256 b ) internal pure returns ( uint256 ) { uint256 c a + b ; require ( c > a ,  Safe Math : addition overflow  ) ; return c ; }"
# token into words
tokens = sentence.split()
# parts of speech tagging
tagged = nltk.pos_tag(tokens)
# print tagged tokens
# print(tagged)

code_list = code.split()
comm_list = sentence.split()
tmp = []
flag = 0
key = ["function", "event"]
for i in code_list:
    if i in key:
        flag = 1
    if flag and i != ")":
        tmp.append(i)
    if i == ")":
        break
print(tmp)
tmp_return = []
count = 0
for i in comm_list:
    count += 1
    if i == "return" or i == "returns":
        start = count
    if i == "." or i == ",":
        finish = count
        break
for i in range(len(comm_list)):
    if start < i < finish:
        tmp_return.append(comm_list[i])

print(Short_Description.replace("<verb object> and", " ".join(tmp)) + ") and\n")
print(Return_Description.replace("<statement>", " ".join(tmp_return)) + "\n")

# filter pairs 50 pairs random selection
random_selection = [11, 2, 8, 4, 4, 4, 4, 4, 1, 8]
d = "smart_contracts"
comment_files = []
comment = []
methods = []
for root, dirs, files in os.walk(d):
    for filename in files:
        if filename.endswith("merged"):
            comment_files.append(os.path.join(root, filename))
# combine code and comments with elaborated comments
# random_list = random.sample(range(0, len(code_lines)), LINES)
for i in range(len(comment_files)):
    with open(comment_files[i], 'r', encoding="utf8") as c_raw:
        combined_lines = c_raw.readlines()  # array of comment lines
        random_list = random.sample(range(0, len(combined_lines)), random_selection[i])
        for j in random_list:
            if j % 2 == 1:
                if combined_lines[j - 1] not in comment:
                    comment.append(combined_lines[j - 1])
                    methods.append(combined_lines[j])
                else:
                    print(i)
            else:
                if combined_lines[j] not in comment:
                    comment.append(combined_lines[j])
                    methods.append(combined_lines[j + 1])
                else:
                    print(i)
print(len(comment))
print(len(methods))
workbook = Workbook()
sheet = workbook.active
with open("questionare2.txt", "w") as questionare:
    for i in range(len(comment)):
        questionare.write(comment[i])
        questionare.write(methods[i])
        sheet["A" + str(i + 1)].alignment = Alignment(wrapText=True)
        sheet["A" + str(i + 1)] = "\n".join([comment[i], methods[i]])

workbook.save(filename="questions2.xlsx")
