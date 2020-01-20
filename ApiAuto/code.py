# coding=utf-8


# def likes(names):
#     n = len(names)
#     return {
#         0: 'no one likes this',
#         1: '{} likes this',
#         2: '{} and {} like this',
#         3: '{}, {} and {} like this',
#         4: '{}, {} and {others} others like this'
#     }[min(4, n)].format(*names[:3], others=n-2)
#
#
# print(likes(['a', 'b', 'c', 'd']))


# def likes(names):
#     length = len(names)
#     others = length -2
#     d = {
#         0: "no one likes this",
#         1: f"{names[0]} likes this",
#         2: f"{names[0]} and {names[1]} like this",
#         3: f"{names[0]}, {names[1]} and {names[2]} like this",
#         4: f"{names[0]}, {names[1]} and {others} others like this"
#     }
#     print(d[min(4, length)])

#
# likes(['a', 'a', 'a', 'a', 'a'])

# def printer_error(s):
#     # your code
#     length = len(s)
#     error = 0
#     for i in s:
#         if i > 'm':
#             error += 1
#     result = f"{error}/{length}"
#     print(result)
#
#
# printer_error("123")


# def find_missing_letter(chars):
#     length = len(chars)
#     for i in range(length):
#         if ord(chars[i]) != ord(chars[i+1]) - 1:
#             return chr(ord(chars[i])+1)
#
#
# print(find_missing_letter(['a','c']))
#
#
# def find_missing_letter(c):
#     return next(chr(ord(c[i])+1) for i in range(len(c)-1) if ord(c[i])+1 != ord(c[i+1]))
#
#
# print(find_missing_letter(['a', 'b', 'd']))

# print(chr(99))
# print(ord('A'))


# def scramble(s1, s2):
#     # your code here
#     for i in s2:
#         if i in s1:
#             s1 = s1.replace(i, '', 1)
#             print(s1)
#         else:
#             return False
#     return True
#
#
# print(scramble('scriptjava', 'javascript'))


# def filter_list(l):
#     result = []
#     for i in l:
#         if type(i) == int:
#             if i >= 0:
#                 result.append(i)
#     return result
#
#
# print(filter_list([1, 33, 'a', 'b', 66]))


def tickets(l):
    money = []
    for i in l:
        if i == 25:
            money.append(i)
        elif i == 50:
            if 25 not in money:
                return 'NO'
        elif i == 100:
            if 25 and 50 not in money:
                if l.count(25) < 3:
                    return 'NO'
    return 'YES'


print(tickets([25, 25, 50]))
print(tickets([25, 100]))
print(tickets([25, 25, 50, 50, 100]))

# l = [25,25,25]
# print(l.count(25))
# if l.count(25) > 3:
#     print(1)