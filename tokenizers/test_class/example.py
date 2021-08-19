def merge_dict(d1, d2, file_path):
    for c in range(len(d2)):
        d1[str(len(d1))] = d2[str(c)]

    with open(file_path, "w") as file:
        for c in d1:
            file.write(d1[c][0] + "\n")


Short_Description = ""
Return_Description = ""
Modifier_Description = ""
Input_Description = ""
Core_Statement_Description = ""
Call_Description = ""

comment = "file.comment"
merged = comment.split(".")
print(".".join([merged[0],"merged"]))