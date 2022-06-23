# #Задание 1
#
# def odd_nums(n):
#     for i in range (1, n+1, 2):
#         yield i
#
#
# odd_to_15 = odd_nums(15)
#
# print(next(odd_to_15))
# print(next(odd_to_15))
# print(next(odd_to_15))
# print(next(odd_to_15))
# print(next(odd_to_15))
# print(next(odd_to_15))
# print(next(odd_to_15))
# print(next(odd_to_15))
# print(next(odd_to_15))

# #Задание 2
#
# num_gen = (i for i in range(1, n+1, 2))
#
# print(next(num_gen))
# print(next(num_gen))
# print(next(num_gen))


# #Задание 4
# #
# #
# # src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# # result = []
# #
# # for i in range(1, len(src)):
# #     if src[i] > src[i-1]:
# #         result.append(src[i])
# # print(result)
# #
# # res = [src[i] for i in range(1, len(src)) if src[i] > src[i-1]]
# # print(res



# # Задание 5
# #
# src1 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# src2 = src1.copy()
# result = []
# set_src = set(src1)
#
# for i in set_src:
#     if i in src1:
#         src1.remove(i)
# for i in src2:
#     if i not in src1:
#         result.append(i)
# print(result)
