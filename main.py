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

# programming_languages = [
#     1, "Python",
#     2, "C",
#     3, "C++",
#     4, "C#",
#     5, "Go",
#     6, "Rust",
#     7, "Php",
#     8, "JavaScript"
# ]
#
#
# def check_int(number):
#     return type(number) is int
#
#
# def check_str(el):
#     return type(el) is str
#
#
# numbers = list(filter(check_int, programming_languages))
# print(numbers)
#
# texts = list(filter(check_str, programming_languages))
# print(texts)

# ----------------------------------------------------------

# programming_languages = [
#     1, "Python",
#     2, "C",
#     3, "C++",
#     4, "C#",
#     5, "Go",
#     6, "Rust",
#     7, "Php",
#     8, "JavaScript"
# ]
#
# numbers = filter(lambda el: type(el) is int, programming_languages)
# print(list(numbers))
#
# texts = filter(lambda el: type(el) is str, programming_languages)
# print(list(texts))

# ----------------------------------------------------------








