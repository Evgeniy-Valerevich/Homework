# ========================================
# _author_-_Khandozhko_Evgeniy_Valerevich_
# ========================================

with open("file_3.txt") as my_file:
    total = []
    less = []
    line = my_file.read().split("\n")
    for i in line:
        i = i.split()
        if int(i[1]) < 20000:
            less.append(i[0])
        total.append(i[1])
print(f" Salary less 20000:\n {less}\n Average salary: {sum(map(int, total))/len(total):.2f}")

