a = '1234'
b = '7653'

sum = [] 
for i, item in enumerate(a):
    sum.append( int(item) + int(b[i]) )

print(sum)
print(''.join(sum))
