# Taqi Syed
# 1863528

password = input()
result = ''

i = 0
while i < len(password):
    ch = password[i]
    if ch == 'i':
        result += '!'
    elif ch == 'a':
        result += '@'
    elif ch == 'm':
        result += 'M'
    elif ch == 'B':
        result += '8'
    elif ch == 'o':
        result += '.'
    else:
        result += ch
    i += 1
result += "q*s"
print(result)