lst = [1, [2, 3, [4, 5]], (6, 7), "abc", ["pwkdw", [8, 9]], [[], [[0,[9]],[[[]]]]]]

def flatten(nested):
    if type(nested) != list:
        return "ERR0R"
    res = []
    stack = nested[::-1]
    while stack:
        elem = stack.pop()
        if type(elem) in [list,tuple,set,frozenset]:
            stack.extend(elem[::-1])
        else:
            res.append(elem)
    return res

print(flatten(lst))