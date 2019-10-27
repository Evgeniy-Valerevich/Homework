# ========================================
# _author_-_Khandozhko_Evgeniy_Valerevich_
# ========================================

with open("file_4.txt") as my_file:
    for line in my_file:
        new_line = line.split(" - ")
        if new_line[1][-1:] == "\n":
            new_line[1] = new_line[1][:-1]
        my_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
        with open("file_4_new.txt", "w") as my_new_file:
            my_new_file.writelines(my_dict[new_line[0]] + " - " + new_line[1] + "\n")