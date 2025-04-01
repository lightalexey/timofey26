# a = input()
s = 'мама мыла раму!'
l = len(s)
print(s)
print('Количество символов в строке равно', l)
print(len(s))
print(s[0])
print(s[0:4])
print(s[l-1])
print(s[-1])
# s[0] = 'М' # строку изменить нельзя!!!
s = 'М' + s[1:]
print(s)
number_a = s.count(' ')
print(number_a)
s = s.replace('Мама', 'мама', 1)
print(s)
if 'папа' in s:
    print(True)
else:
    print(False)