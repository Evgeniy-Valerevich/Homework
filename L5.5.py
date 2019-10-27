# ========================================
# _author_-_Khandozhko_Evgeniy_Valerevich_
# ========================================

from random import randint
total = 0

with open("file_5.txt", "w") as my_file:
    for i in range(10):
        el = randint(1, 10)
        total += el
        my_file.write(str(el) + " ")

print(f"Sum of elements: {total}")