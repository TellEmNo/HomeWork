# def sum_numbers(n, y="Your sum is: "):
#     print(y, end=" ")
#     sum_ = 0
#     for i in range(1, n+1):
#         sum_ += i
#     return sum_
#
# a = sum_numbers(8)
# print(a)

# def sum_str(*args):
#     res = ""
#     for i in args:
#         res += i
#     return res
# print(sum_str("q", "a", "l"))

# from modul_1 import max1
#
# print(max1(12, 9))

# from modul_1 import fibonacchi
#
# list1 = []
# for i in range(1, 10):
#     list1.append(fibonacchi(i))
# print(list1)

# import modul_1
#
# print(modul_1.quick_sort([14, 6, 123, 12, 45, 654]))

from modul_1 import merge_sort

list_1 = [1, 5, 2, 23, 3, 5, 8, 2, 12, 33]
print(list_1)
merge_sort(list_1)
print(list_1)