# print("hello, world!")
#
# a = 'hello, world!'
#
# print(a)
# print(type(a))
# print(dir(a))

# first_var_1 = 15
# print(first_var_1)
# print(type(first_var_1))
# print(dir(first_var_1))

# print(help(int))

# my_list = [15, 189.5, 'hi', True]
#
# my_list.append('good')
# buf = my_list.pop()
#
# print(buf)
# print(my_list)
# print(type(my_list))
# print(dir(my_list))

# my_list = [15, 189.5, 'hi', True]
# my_list[2] = False
#
# print(my_list)
# print(my_list[1])

# # tuple
# my_list = (15, 189.5, 'hi', True)
# # my_list[2] = False
#
# print(my_list)
# print(my_list[1])
# # print(type(my_list))
# # print(dir(my_list))

a = [1, 2, 3, 4, 5]
b = [10, 20, 30, 40, 50]
c = [100, 200, 300, 400, 500]
d = [1000, 2000, 3000, 4000, 5000]
e = [10000, 20000, 30000, 40000, 50000]

# result = list(zip(a, b, c))
# print(result)

args = [a, b, c, d, e]

result = list(zip(*args))
print(result)

