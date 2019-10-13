# =========================================
# _author_ = _Khandozhko_Evgeniy_Valerevich_
# =========================================

a = int(input("enter_an_integer - "))
b = 0
a = abs(a)

while a // 10 > 0:
    c = a % 10
    a = a // 10
    if c > b:
        b = c
        if b == 9:
            break

print("the_largest_digit_of_this_integer - ", b)
