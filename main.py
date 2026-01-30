# def summa(a, b):
#     return a + b
#
# print(summa(5, 4))
#
#
# summa = lambda a, b: a + b
# print(summa(4, 5))

# -------------------------------------------------

# numbers = ["1", "2", "3", "4"]
#
# new_nums = []
# for num in numbers:
#     new_nums.append(int(num))
#
# print(new_nums)


# -------------------------------------------------

# map(<nima ish qilinishi>, <anashu ish qaysi objectlar ustida amalga oshirilishi>)

# numbers = ["1", "2", "3", "4"]
#
# new_numbers = list(map(int, numbers))
# print(new_numbers)

# -------------------------------------------------

# harflar = ["a", "b", "c", "d"]
#
# katta_harflar = list(map(str.upper, harflar))
# print(katta_harflar)

# -------------------------------------------------



# harflar = ["a", "b", "c", "d"]


# def to_upper(harf: str):
#     return harf.upper()
#
#
# katta_harflar = list(map(to_upper, harflar))
# print(katta_harflar)

# -------------------------------------------------


# harflar = ["a", "b", "c", "d"]
#
# katta_harflar = list(map(lambda harf: harf.upper(), harflar))
# print(katta_harflar)

# -------------------------------------------------

# katta_harflar = ['A', 'B', 'C', 'D']
# kichik_harflar = ["a", "b", "c", "d"]
#
#
# def content(harf1: str, harf2: str):
#     return harf1 + harf2
#
#
# harflar = list(map(content, katta_harflar, kichik_harflar))
# print(harflar)

# -------------------------------------------------
# filter(<nima ish qilinishi>, <shu ish qaysi objectlar ustida amalga oshirilishi>)

# harflar = ['A', 'B', 'C', 'D', "a", "b", "c", "d"]
#
# katta_harflar = list(filter(str.isupper, harflar))
# print(katta_harflar)
#
# kichik_harflar = list(filter(str.islower, harflar))
# print(kichik_harflar)


# -------------------------------------------------






