
n=raw_input('enter the string' )
def remove_char(str, n):
    first_part = str[:n]
    last_part = str[n + 1:]
    return first_part + last_part
print(remove_char(n,0))
print(remove_char(n,3))
print(remove_char(n,4))
