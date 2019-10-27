# ========================================
# _author_-_Khandozhko_Evgeniy_Valerevich_
# ========================================

with open("file_2.txt") as my_file:
    line = []
    word = []
    for i in my_file:
        if i[-1:] == "\n":
            i = i[:-1]
        line.append(i)
        word.append([len(i.split())])
print(f"File data:\n{line}\nLines in file: {len(line)}\nWords in lines:\n{word} ")
