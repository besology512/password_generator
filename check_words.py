import enchant
d = enchant.Dict('en_US')
print(d.check('hello'))
text = 'sdf45heymands'
found = []
for i in range(len(text)):
    for j in range(i-1):
        print(text[j:i])
        check = d.check(text[j:i])
        if check == True and i-j > 2:
            print('found one')
            found.append([j, i])
print(found)
