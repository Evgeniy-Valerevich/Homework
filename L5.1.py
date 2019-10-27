# ========================================
# _author_-_Khandozhko_Evgeniy_Valerevich_
# ========================================

while True:
    line = input("Enter: ").split()
    if not line:
        break
    with open("file_1.txt", "a") as my_file:
        for i in range(len(line)):
            print(line[i], file=my_file)
