#!/usr/bin/python3.9

def get_summ(one, two, delimiter='&'):
    return f'{one}{delimiter}{two}'

res = get_summ("Learn","python")
print(res)
print(res.upper())
