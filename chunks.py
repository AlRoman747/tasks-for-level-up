from random import choice

lst = []
len_list = choice(range(2,100))
len_chunk = choice(range(1,len_list))
while len(lst) < len_list:
    lst.append(choice(range(0,100)))

print(lst, len_list, len_chunk, sep='\n')


def chunks(lst, n):
    res = []
    for i in range(0, len(lst), n):
        res.append(lst[i:i+n])

    return res

print(chunks(lst, len_chunk))

