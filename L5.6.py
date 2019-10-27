# ========================================
# _author_-_Khandozhko_Evgeniy_Valerevich_
# ========================================

with open("file_6.txt") as my_file:
    new_list = []
    subjects = {}
    for line in my_file:
        subject, other = line.split(":")
        new_list = other.split()
        if len(new_list) == 6:
            subjects[subject] = int(new_list[1]) + int(new_list[3]) + int(new_list[5])
        elif len(new_list) == 4:
            subjects[subject] = int(new_list[1]) + int(new_list[3])
        elif len(new_list) == 2:
            subjects[subject] = int(new_list[1])
        else:
            subjects[subject] = 0

print(subjects)
